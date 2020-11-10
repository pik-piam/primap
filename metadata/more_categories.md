# Dealing with additional dimensions, multiple hierarchies

## Problem statement
The current approach in PRIMAP suffers from two key problems:
1. The used metadata terminology/hierarchy (e.g. IPC2006 sectoral categories) is not cleanly represented. For some values, it is encoded in a prefix (e.g. `CATEGORY: IPC1`), for others it has to be guessed (e.g. `TYPE: GOAT`).
2. It is not possible to store arbitrary sub-categories and dimensions (e.g. the aggregate state of fuels, or the animal species). Commonly, the `CLASS` and `TYPE` are used for this purpose, but even when bending the rules, no more than two additional dimensions can be introduced.

## Proposals

### 1. Descriptive, explicit names + metadata
Any dimension (`sector`, `animal species`) and terminology (e.g. `IPC2006`) gets a dedicated, descriptive name, e.g. `sector (IPC 2006 categories)`. Additional metadata on a higher granularity maps generic names to the explicit names (e.g. `sector: "sector (IPC 2006 categories)"` and `sector_terminology: "IPC 2006"`). Accessors will be provided to comfortably select directly using the generic names.

New dimensions can be introduced anonymously (without defined terminology and without additional metadata), but if they are used more commonly or multiple terminologies need to be used, a defined terminology and a generic name can be introduced later.

We would need to discuss if we should immediately introduce generic names for the temporal and spatial dimensions. This would for example support storing temporal information in the dimension `years`, coupled with the metadata `time: "years"`.

Advantages:
* In contexts without metadata (simple CSV files, quick display, plotting with dimension names as axis labels), no information is lost.
* Access using generic names is possible via indirection / special accessors.
* Future expansion like a spatial data type with multiple columns (example from REMIND/Magpie universe: data about trade, which has an exporting and an importing country instead of only one country) are easier to integrate because there is already a mechanism to store this meta-metadata.

Disadvantages:
* Even with dedicated accessors, some special work/syntax is necessary to use generic names. Example: Instead of `ds.groupby("sector")`, it will be probably be necessary to write something like `ds.groupby(ds.col_mapping["sector"])` or so. Maybe we can invent shorter names than `col_mapping` or do a little black magic to make groupby using the generic name possible, but the abstraction will leak a bit. So functions / applications that don't care which terminology is used have to pay a price.

### 2. Generic names + metadata
Dimensions are added with their generic names (`sector`, `animal species`). Additional metadata on a higher granularity maps generic names to the used terminology (e.g. `sector_terminology: "IPC 2006"`).

New dimensions are introduced with arbitrary generic names, and if a dimension is used more commonly or a terminology should be explicitly defined, the "canonical" generic name is defined somwhere and the terminology metadata is added.

Advantages:
* Functions or applications which don't care for the terminology don't have to deal with it at all.
* Direct access using standard accessors and indexing using generic names is straight forward and efficient.

Disadvantages:
* Easy to do wrong computations (adding up sector 5 from one dataset with sector 5 from the other dataset, disregarding one uses IPC 2006 categories, the other IPC 1994 categories).
* Future expansion like the trade data example might require "breaking" changes, where naive functions can't access the spatial information anymore.







## Detailed thoughts, including other rejected ideas

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
* **optional, descriptive metadata columns with meta-metadata:** For each category hierarchy and dimension, an own optional metadata column is defined. So what is named `CATEGORY` in PRIMAP would become `sector (IPC 2006)` and `sector (IPC 1994)`. Additionally, in the attribute `sector` the name of the sectoral category is saved, and accessors are provided to easily access the sectoral category.

**claims (IMHO):**
* no string processing. String processing kills performance for little gain. Also, repeating the category hierarchy in each value is unnormalized and gives the opportunity for inconsistent columns with differing prefixes.
* optional meta data columns over required columns filled with default values. Forcing the user to state a sectoral category for data which does not have one (e.g. population data) makes it easier to write code which *requires* sectoral categories for proper function, but this code will probably fail if everything is filled with a dummy category, and will produce garbage. If the data set does not have a sectoral category and some function tries to access it, it will fail early and fast instead of producing garbage.