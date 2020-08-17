# Units
## Types of units
* note: I try to describe the units in a traditional, physical sense; however, it might be that the structure should be different because of cultural conventions in the climate context that I do not know yet.
* I list only those I have encountered in climate contexts so far.
### mass
* g of different gases or elements
* unit in the traditional sense does not contain which gas or element, i.e. not the answer to the question "what?", but only part of the answer to the question "how much?"
* full statement would be something like m(NO2) = 2345 kg
* in some contexts, masses can be converted between different quantities, for example in gas contexts m(CO2) = 1 g can approximately be converted to m(C) = 12/44 g
### emissions = mass / time
* typical unit is "g / y"
* full statement would be something like e(CO2) = 2345 kg / y
### warming potential
* typical unit is "g CO2eq"
* mass can be converted to warming potential, where m(CO2) = 1 g converts to wp = 1 CO2eq by definition. Other gases or elements have other conversion factors, which depend on the context (global warming potentials of the gases).
* I am not totally sure warming potential can usefully be regarded as a unit. What's the difference between m(CO2) = 1 g and wp = 1 g CO2eq ? Why define a new dimension which is only mass in disguise? If I want to actually calculate warming from warming potential, I have to start up a climate model anyway, don't I?
### emission of warming potential = warming potential / time
* typical unit is "g CO2eq / y"
* emissions can be converted to emissions of warming potential just like mass can be converted to warming potential.
### money
* typical unit is "$" or such
* is kind of fancy, because conversions between different money units like $ and € depend on time (or more), and inflation is going on as well.
* there are inflation-adjusted money things, which may or may not be an own unit.
### purchase power
* typical unit is also $ or something
* conversion between money and purchase power depends on time and area, so is very fancy.
### population
* without unit
* quantities can be humans, or sheep or any other clearly countable organism.
### energy
* SI unit is J, but other units like kWh or oil equivalents are also in use.
### power
* SI unit is W, but any other energy unit over any time unit is also in use, like kWh / y or whatever
### temperature
* SI unit is K, °C is also often used
* In climate context, temperature differences are also often used, which also have the unit K or °C, and where 1 K = 1 °C.
### area = length x length
* m², (km)², hectares
### radiative forcing = power / area
* any power unit over any area unit
* often also as a delta instead of an absolute value
### time
* typically s
* absolute time is more difficult, because of timezones and different calendars and stuff.
* absolute time is generally represented as a time difference from some defined point in time (like years since 1 AD or seconds since January 1st, 1970).
* has very funny larger units than seconds. neither days, months, nor years have the same length each, instead their length depends on the absolute time. Often, approximate conversions between different larger units can still be done (like a year in seconds), because the error is small.
## unit conversions in use cases
* storing use cases: Units have to be stored together with the data
* discovery: depending on the type of search, a dimension between units or even dimensions might be desirable. Searching for "the largest emitters" might entail automatically converting masses to warming potentials using a given conversion context.
* publishing: units should be published alongside the data format so that it is very hard to miss them.
* data normalization: it could be desirable to standardize on a set of units (e.g., use SI units for dimensions where they are available), wich would make unit conversions frequently necessary during data normalization
* quality assurance: if a standard set of units is defined, qa could check if these units are used and warn if other units are used.
* selecting data: here, unit conversions are frequently needed
* filling in data: if the other dataset is in another unit, data should be converted to the unit of the to-be-filled-in dataset before filling.
* arithmetic: here, unit conversion is frequently needed, and it should be possible to specify a unit conversion context for the whole calculation.
* visualization: units should be indicated in generated visualization.
* tidy format: conversion to tidy format (if necessary) should conserve units.

