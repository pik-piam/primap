# Data import
## use cases
### data normalization
Data sources use very different formats and metadata categorizations.
Normalization can include:
* simple meta data mapping
* translation of categories, with up- or down-scaling of intensive and extensive quantities
* conservative and non-conservative meta data translation
* unit conversion
* addition of derived meta data
* normalization of data using a base year or reference data sets
* interpolation and extrapolation on a temporal scale

### quality assurance
When importing data, internal consistency and plausibility of the data can be checked automatically. A researcher can verify warnings by hand, and either silence the warning or correct the error.

### archiving
A researcher notices that a data set is obsolete. They archive the data set to hide it from standard querying functions, but it remains available when explicitly querying for archived data sets.

## major data sources
### UNFCCC CRF
* source: https://unfccc.int/process-and-meetings/transparency-and-reporting/reporting-and-review-under-the-convention/greenhouse-gas-inventories-annex-i-parties/inventory-review-reports-2020
* format: collections of excel files in a custom, defined format
* updated at least annually

### UNFCCC detailed data by party
* source: https://unfccc.int/process-and-meetings/transparency-and-reporting/greenhouse-gas-data/ghg-data-unfccc/ghg-data-from-unfccc
* format: collections of json data files
* updated at least annually
* there exists a library for downloading and reading: https://github.com/openclimatedata/unfccc-detailed-data-by-party

### UNFCCC BURs
* source: https://unfccc.int/BURs
* format: standardized proprietary excel files
* partly updated bi-annually

### British Petroleum
* source: https://www.bp.com/en/global/corporate/energy-economics/statistical-review-of-world-energy.html
* format: csv
* updated roughly annually
* data from same source also used in madrad universe

### EDGAR
* source: https://edgar.jrc.ec.europa.eu/
* format: collection of excel files
* data from same source also used in madrad universe
* there exists a library for downloading and reading: https://github.com/openclimatedata/edgar

### CDIAC
* source: https://cdiac.ess-dive.lbl.gov/
* format: csv
* data from same source also used in madrad universe
* there exists a library for downloading and reading: https://github.com/openclimatedata/cdiac-co2-fossil-national

### FAOstat
* source: http://www.fao.org/faostat/en/#home
* format: collection of csv files
* data from same source also used in madrad universe

### Andrew Cement
* source: https://zenodo.org/record/3380081
* format: single xls file in country-year format
* there exists a library for downloading and reading: https://github.com/openclimatedata/co2-emissions-cement

### RCPs
* source: http://www.iiasa.ac.at/web-apps/tnt/RcpDb
* format: collection of xls files
* RCP data also used in madrad universe

### SSPs
* source: https://tntcat.iiasa.ac.at/SspDb/dsd?Action=htmlpage&page=about
* SSP data also available in madrad universe

## other data sources
### EDGAR-HYDE
* source: https://themasites.pbl.nl/tridion/en/themasites/edgar/emission_data/edgar-hyde-100yr/index-2.html
* format: collection of xls files

### IEA World Energy Outlook
* source: https://www.iea.org/topics/world-energy-outlook
* data from same source in newer version also used in madrad universe

### Houghton 2008
* source: https://cdiac.ess-dive.lbl.gov/trends/landuse/houghton/houghton
* format: excel file

### US EPA 2012
* source: ?

TODO

## other emissions projection
### Match 2008
* source: ?

TODO

### MAGAVIATION
* source: https://www.cate.mmu.ac.uk/omega-overview/ (?)

TODO

### further unidentified:
* QUANTIFY2009
* EYRING2005
* IMO2009
* IMO2014
* SAGEHYDE

## Non-emission data
### UN world population
* source: https://population.un.org/wpp/
* format: csv
* data from same source also used in madrad universe

### Penn world table
* source: https://www.rug.nl/ggdc/productivity/pwt/?lang=en
* format: proprietary excel file
* data from same source also used in madrad universe

### Maddison historical statistics
* source: https://www.rug.nl/ggdc/historicaldevelopment/maddison/?lang=en
* format: proprietary excel file

### World Development Indicators
* source: https://databank.worldbank.org/source/world-development-indicators
* format: csv
* data from same source also used in madrad universe

### further unidentified:
* GEIGER2017
* GEIGER2018
* HYDE32

also used in madrad universe:
* USDA2013O
* USDA2015
* IMFWEO2012A

### madrad universe data sources
on the cluster: `/p/projects/rd3mod/inputdata/sources`
