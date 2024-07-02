# SOC KG

## Prefixess Used

- RDF prefixes are abbreviated using the shorthand provided by [rdflib.namespace](https://rdflib.readthedocs.io/en/stable/apidocs/rdflib.namespace.html) except for the following:
- SOC. may be an abbreviation for [neo4j://graph.schema#] (neo4j://graph.schema#) 
- WD. is an abbreviation for [http://www.wikidata.org/entity/](http://www.wikidata.org/entity/)

Domains and ranges of predicates are provided in sockg_ontology.ttl

## Node Types

- SOC.Amendment
- SOC.BookChapter
- SOC.City
- SOC.Country
- SOC.County
- SOC.Department
- SOC.Experiment
- SOC.ExperimentalUnit
- SOC.Field
- SOC.Harvest
- SOC.MiscellaneousMeasurement
- SOC.Organization
- SOC.Person
- SOC.Pesticide
- SOC.PlantingEvent
- SOC.Project
- SOC.Publication
- SOC.ResearchUnit
- SOC.Rotation
- SOC.Site
- SOC.Soil
- SOC.SoilBiologicalSample
- SOC.SoilChemicalSample
- SOC.SoilPhysicalSample
- SOC.State
- SOC.Tillage
- SOC.Treatment
- SOC.Version
- SOC.WeatherObservation
- SOC.WeatherStation

## Predicates

- SOC.appliedInExpUnit
- SOC.appliedInField
- SOC.departmentOf
- SOC.fundsExperiment
- SOC.happenedAtResearchUnit
- SOC.happenedInSite
- SOC.hasAmendment
- SOC.hasBioSample
- SOC.hasChemSample
- SOC.hasCity
- SOC.hasCounty
- SOC.hasField
- SOC.hasMiscellaneousMeasurement
- SOC.hasPesticide 
- SOC.hasPhySample
- SOC.hasRotation
- SOC.hasState
- SOC.hasTillage
- SOC.isHarvested
- SOC.isPartOfPublication
- SOC.locatedInCity
- SOC.locatedInCountry
- SOC.locatedInCounty
- SOC.locatedInField
- SOC.locatedInState
- SOC.plantingAt
- SOC.recordsWeatherForSite
- SOC.studiesSite
- SOC.usedInExpUnit
- SOC.weatherAtField
- SOC.weatherRecordedAt
- SOC.weatherRecordedBy
- SOC.worksAtDepartment
- SOC.worksFor
- SOC.worksIn