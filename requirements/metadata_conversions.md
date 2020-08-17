# Metadata conversions
## in previously described use cases
* here, a `category` is any metadata with a finite set of possible values, such as IPCCC categories or countries.
### data normalization
In data normalization, a lot of different metadata conversions are necessary:
* translation: bijective translation of categories. Example: Long-form country names to country codes.
* restriction: dropping some categories.
* arithmetic generation: generating new categories by adding, subtracting, multiplying, or dividing existing categories.
* downscaling of extensive quantities: splitting existing categories using predetermined shares, shares calculated from other data, or individual factors calculated from other data. Examples: the emissions of formerly united countries which split at some time are downscaled for the time before the split using the emission shares after the split; alternatively, the emissions of regions might be downscaled into constituent countries using a population share and an area share, depending on the category.
* upscaling of intensive quantities: upscaling existing categories is best done by multiplying with the relevant data to generate extensive quantities, which can be upscaled by summation.
* resampling of time: for example, interpolation between 10-year steps to generate 1-year steps.

### quality assurance
Upscaling could be used in quality assurance to ensure that sums of smaller categories are consistent to the larger category.

### selecting data
Selecting data by extensive categories might not be useful, so a conversion to intensive categories is necessary.

### filling in missing data
As in data normalization, a lot of different metadata conversions might be necessary.

### visualization
In visualizations, a conversion of categories or time resampling might be necessary to aid visual goals. For example, if there are too many categories to plot while maintaining visibility, upscaling into a category "other" might be necessary.

### traceability
traceability will be complicated by metadata conversions, because many metadata conversions lead to the need to trace individual data points instead of whole datasets.
