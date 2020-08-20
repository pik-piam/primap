# Evaluation criteria for data structures
## representation
* load all example data sets into the data structure at once
* measure memory use
* export the data sets to CSV
* reimport from CSV
* export the data sets to some kind of native storage format
* reimport from the native storage format

## interactive analysis and plotting
* add / subtract / divide / multiply compatible, overlapping data sets
* timeit
* plot a historical time series, and something akin to gapminder (countries on a gdp vs emissions plot)
* select datasets which contain data on the NO2 emissions of Finland
* in a selected dataset, select years in which the NO2 emissions of Finland were above the 1950-2000 average
* resample non-yearly dataset to yearly dataset
* convert a dataset to tidy format

## units
* add unit information to two datasets, with compatible but different units
* add both datasets together correctly
* store and re-load the result, preserving units

## tracing
* I would *not* look into traceability of data points right now, because I think there is no ready-made solution for any of the libraries.

## metadata conversions
* delete some data points from a data set and fill them in using linear interpolation
