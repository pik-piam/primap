# Metadata in PRIMAP
## metadata types
* time (when?)
* area (where?)
* dimension (what?)
* activity / category (why?)
* unit
* measured / projected / derived
* source:
  - publication
  - url / doi
  - model
  - scenario
  - contact for questions
  - provenance
  - legal permissions
* description
* uncertainty (maybe rather data, not metadata)
* provenance for derived data
* name

## metadata properties
| property | metadata types |
| ---      | ----           |
| possibility to query for metadata | all |
| finite set of values | area, dimension, activity, unit, measured/projected/derived, source |
| infinite set of values |  time, description, uncertainty, provenance |
| imported / provided by the user |  all but provenance, uncertainty |
| aggregation / upscaling required |  time, area, dimension, activity / category |
| downscaling required |  time, area, dimension, activity / category |
| typically matching arithmetic |  time, area |
| automatically calculable in arithmetic |  dimension, unit, uncertainty, provenance |
| application-dependent arithmetic |  activity / category, measured/projected/derived, source, description |
| continuous set of values |  time, uncertainty |
| free-form |  description, name |
| derived |  provenance, (uncertainty) |
| conversion using universal rules |  unit |
| can not be NaN | all |

* provenance is a generalization of source
* source is a compound data type with lots of data points having the same source
* maybe a generalization of both is a "label"?
* maybe measured / projected / derived is also an information coupled to the source?
* name is formed from other metadata in the current PRIMAPDB

## typically coupled metadata
* dimension ⇨ unit
* source ⇨ measured / projected / derived
* source ⇨ description

## how many different meta data values in all of PRIMAPs current data
| metadata types | number of values |
| ---      | ----           |
| time | approx 2000 years (1-2100) |
| area | approx 250 countries/regions |
| dimension | approx 50 |
| activity / category | approx 250 |
| unit | approx 10 |
| m/p/d | hist/projected |
| source | 15 in minDB, ~50 in total(?) |
| description | ~1000 in minDB, ~15000 in total(?) |
