# Storage and Sharing
## Use Cases
### personal storage
A researcher stores the result of a computation on hard disk, and loads this result the next day to continue working.
### persistent storage
A researcher stores results on hard disk. Another researcher loads this result 5 years later to build on the previous results in a new analysis.
### data shuttling
A researcher performs a long-running computation on the cluster. The resulting single dataset is stored on the cluster and transferred to the personal laptop of the researcher. The researcher opens the dataset and all metadata is restored.
### intermediate results
A researcher curates data from an outside source into a more usable, standardized format. The processing includes correcting errors in the original data, and getting this pre-processing right is therefore non-trivial. The resulting datasets are useful to other researchers and are therefore distributed privately.
### intermediate results with updates
A researcher curates data from an outside source, which is non-trivial. The resulting datasets are useful to other researchers and are therefore distributed privately. Later, another researcher discovers a minor error in the pre-processing. They correct the error and re-run the data pre-processing. All researchers using the datasets get the updated version of the datasets.
### intermediate results with updates; earlier version
As in the previous use case, but a researcher needs to access an earlier version of the updated data set to reproduce a specific result. Given a reference date, the version of the data set at that point in time is returned.
### intermediate results; data not distributable
A researcher curates data from an outside source which does not allow re-distribution of the data. The resulting datasets are nevertheless useful to other researchers. The pre-processing scripts are distributed without the data to other researchers, who can run the scripts themselves to access the resulting datasets. Locally, intermediate results are cached to speed up processing and downloading.
### discovery
A researcher searches for datasets containing information about a specific set of countries in a specific timespan. They get a list of datasets containing the used information, some of these curated and made accessible by other researchers.
### publishing
A group of researchers prepares a data set which is useful for the public. The data set is published, and other researchers load the data set using their own software.
### publishing with updates
A group of researchers continuously update a data set which is useful for the public. Users can choose to load the most recent version or earlier versions of the data using persistent identifiers.

## Example data sets
### PRIMAP-hist
* `example_data_sets/PRIMAP-hist_v2.1_09-Nov-2019.csv`
* source: https://www.pik-potsdam.de/paris-reality-check/primap-hist/
* temporal resolution: 1 year
* spatial resolution: iso countries
* other axes: scenario, category, entity
* other meta data: unit
* size: approx. 5 million data points

PRIMAP-hist is a standardized and curated data set of moderate size.

### PRIMAP standard data base
* `example_data_sets/PRIMAPDB.mat`
* source: `svn/PRIMAP/trunk/primap_functions/data_shelves`
* temporal resolution: 1 year
* spatial resolution: PRIMAP countries, based on iso countries
* other axes: scenario, category, entity, source, class
* other meta data: unit, description, subsource, name of researcher who read in the data
* size: approx. 2 billion data points

The PRIMAP standard data base contains about 3500 standardized and curated data sets from about 15 different sources.

### FAOstat Emissions Agriculture Total
* `example_data_sets/Emissions_Agriculture_Agriculture_total_E_All_Data.csv`
* source: http://www.fao.org/faostat/en/#data/GT
* temporal resolution: 1 year
* spatial resolution: iso countries
* other axes: Element, Item
* other meta data: unit, "flag" indicating data provenance
* size: approx. 1 million data points

The FAOstat Emissions Agriculture Total data set is of moderate size and is curated by FAO, but does not conform to PRIMAP standards.
