**requirement:** Traditionally, there is a single `CATEGORY` metadata column in PRIMAP, which is filled e.g. by the IPC sector categories. There are two additional requirements:
* There exists multiple category hierarchies in use (e.g. traditional vs updated IPC sector categories), and we need a mechanism to denote which category hierarchy is in use.
* Additional dimensions which are orthogonal to the primary categorization exist in some data types. Examples are datasets which list emissions and removals separately, agricultural datasets which contain data on animal species separately, etc.

**current solution:** In PRIMAP, this is solved using two different approaches:
* Regarding different category hierarchies, a prefix is used, so that `CAT5A` and `IPC5A` are distinct. Using string processing, the applicable hierarchy can be extracted.
* Regarding additional dimensions, two additional metadata columns `CLASS` and `TYPE` are introduced, so that a maximum of two additional dimensions can be introduced.

**problems with the current solution:** Prefixes suffer from the problem that string processing is necessary, complicating querying.
Additional dimensions using generic metadata columns suffer from the problem that the dimension is encoded only implicitly (it has to be deduced from the fact that "goat" and "camel" are used that the dimension is likely "animal species") and the number of additional dimensions is limited to two.

**possible approaches:**
* **optional, descriptive metadata columns:** For each category hierarchy and dimension, an own optional metadata column is defined. So what is named `CATEGORY` in PRIMAP would become `sector (IPC 2006)` and `sector (IPC 1994)`, where each dataset usually only has one. This would also enable that datasets where the sector is not applicable (e.g. population data sets) do not have to include this metadata column at all. For additional dimensions, appropriate optional metadata columns are introduced, e.g. `animal species`.
* **category hierarchy meta-meta data + generic columns:** For each category column, store which hierarchy is used. So there is something like `category 1` and `category hierarchy 1`, which would be for example `5A` and `IPC 2006`. If additional dimensions are necessary, `category 2` and `category hierarchy 2` are introduced.
* **sectoral hierarchy meta-meta data + optional columns:** To standardize on `sector` for the common case of a single categorical dimension, use `sector` and `sector hierarchy` to replace the current `CATEGORY` and use optional, descriptive columns as in the first approach for other dimensions.

**claims (IMHO):**
* no string processing. String processing kills performance for little gain. Also, repeating the category hierarchy in each value is unnormalized and gives the opportunity for inconsistent columns with differing prefixes.
* optional meta data columns over required columns filled with default values. Forcing the user to state a sectoral category for data which does not have one (e.g. population data) makes it easier to write code which *requires* sectoral categories for proper function, but this code will probably fail if everything is filled with a dummy category, and will produce garbage. If the data set does not have a sectoral category and some function tries to access it, it will fail early and fast instead of producing garbage.