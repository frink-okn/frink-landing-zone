# Learn More about the Knowledge Graphs in PROTO-OKN

The information provided about Theme 1 graphs was obtained from an analysis of the graphs that were deposited in the FRINK Landing zone, using [LinkML schema](https://linkml.io/linkml/schemas/index.html) to generate the schema and using a modification of [this documentation generator](https://linkml.io/linkml/generators/markdown.html) to produce readable pages with class diagrams from that schema.

Need to correct your graph's information? Please contact [Mahir Morshed](mailto:mmorshed@scripps.edu).

- [Biobricks](biobricks-ice-kg.md)
- [Climate Models](climate-kg.md)
- [DREAM KG](dream-kg.md)
- [Neighborhood Information](neighborhood-kg.md)
- [Rural Resilience](rural-kg.md)
- [SAW Graph](sawgraph-kg.md)
- [SCALES](scales-kg.md)
- [Secure Chain](secure-chain-kg.md)
- [SOC KG](soc-kg.md)
- [SUDOKN](sudokn-kg.md)
- [WEN KG](wen-kg.md)

<bold>IRI prefixes</bold>
The following IRI prefixes have been identified in the Theme 1 graphs and are documented for each graph where applicable.

| prefix | IRI | 
| --- | --- | 
| sosa: | http://www.w3.org/ns/sosa/ |  
| umls: | https://identifiers.org/umls: |  
| niehs: | https://ice.ntp.niehs.nih.gov/property/ |  
| semsci: | http://semanticscience.org/resource/SIO_ |  
| dc: | http://purl.org/dc/elements/1.1/ |  
| sockg: | http://www.semanticweb.org/zzy/ontologies/2024/0/soil-carbon-ontology/ | 
| dreamkg: | http://www.semanticweb.org/dreamkg/ijcai/ | 
| dct: | http://purl.org/dc/terms/ |  
| xsd: | http://www.w3.org/2001/XMLSchema# |  
| geo: | http://www.opengis.net/ont/geosparql# |  
| cheminf: | http://purl.obolibrary.org/obo/CHEMINF_ |  
| obo: | http://purl.obolibrary.org/obo/ |  
| owl: | http://www.w3.org/2002/07/owl# |  
| rdf: | http://www.w3.org/1999/02/22-rdf-syntax-ns# |  
| scales: | http://schemas.scales-okn.org/rdf/scales# | 
| hsdo: | http://schema.org/ | 
| schema: | https://schema.org/ |  
| neo4j: | neo4j://graph.schema# |
| rural: | http://sail.ua.edu/ruralkg/ | 
| example: | http://example.org/ns# | 
| securechain: | https://w3id.org/secure-chain/ | 
| prov: | http://www.w3.org/ns/prov# | 
| io: | https://spec.industrialontologies.org/ontology/core/Core/ |  
| iosc: | https://spec.industrialontologies.org/ontology/supplychain/SupplyChain/ |  
| sudokn: | http://asu.edu/semantics/SUDOKN/ | 
| sudokn2: | Utilities:communication/ | 
| sudokn3: | Utilities:water/ | 
| usfrsdata: | http://sawgraph.spatialai.org/v1/us-frs-data# | 
| usfrs: | http://sawgraph.spatialai.org/v1/us-frs# | 
| naics: | http://sawgraph.spatialai.org/v1/fio/naics# | 
| skos: | http://www.w3.org/2004/02/skos/core# |  
| rdfs: | http://www.w3.org/2000/01/rdf-schema# |  
| bao: | http://www.bioassayontology.org/bao#BAO_ |  
| edam: | http://edamontology.org/ | 
| qudt: | http://qudt.org/schema/qudt/ |  
| ilisgs: | http://sawgraph.spatialai.org/v1/il-isgs# | 
| meegad: | http://sawgraph.spatialai.org/v1/me-egad# | 
| memgs: | http://sawgraph.spatialai.org/v1/me-mgs# | 
| ussdwis: | http://sawgraph.spatialai.org/v1/us-sdwis# | 
| pfas: | http://sawgraph.spatialai.org/v1/pfas# | 
| contaminoso: | http://sawgraph.spatialai.org/v1/contaminoso# |  
| relation: | http://relation.org/ | 
| attribute: | http://attribute.org/ | 
| phila: | https://metadata.phila.gov/ |  


### Ontology (owl:Ontology)

Currently, a single HDT file is assumed to represent an entire unit of data modeled in a specific way. As a result, exactly one type of entity has been inferred to exist in the Theme 1 graphs: [owl:Ontology]( http://www.w3.org/2002/07/owl#Ontology) 

Consequently, triples for an entity with a CURIE of `example:myOntology` will have the following effects:

- example:myOntology [dct:title](http://purl.org/dc/terms/title) "Title of the ontology"
- example:myOntology [dct:description](http://purl.org/dc/terms/description) "Description of the ontology"
- example:myOntology [dct:hasVersion](http://purl.org/dc/terms/title) "0.0.1"
- example:myOntology [dct:created](http://purl.org/dc/terms/created) "2024-10-30T00:00:00Z"^^xsd:dateTime

### Classes (owl:Class or rdfs:Class)

Entities are assumed to be either an [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class) or an [owl:Class](http://www.w3.org/2002/07/owl#Class). Consequently, triples for an entity with a CURIE of `example:myClass"` will either be represented as `rdfs:Class` or `owl:Class`. Triples will have the following effects:

- example:myClass [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) "ClassName"
- example:myClass [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) "Description of this class"
- example:myClass [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) <https://example.com/schema/that/defines/this/class.html>
- example:myClass [rdfs:subClassOf](http://www.w3.org/2000/01/rdf-schema#subClassOf) example:mySuperClass

### Predicates

Predicates, e.g., `example:myPredicate` will be represented with at least one of the following triples as appropriate:

- example:myPredicate a [rdf:Property](http://www.w3.org/1999/02/22-rdf-syntax-ns#Property)
- example:myPredicate a [rdfs:ContainerMembershipProperty](http://www.w3.org/2000/01/rdf-schema#ContainerMembershipProperty)
- example:myPredicate a [owl:DatatypeProperty](http://www.w3.org/2002/07/owl#DatatypeProperty)
- example:myPredicate a [owl:AnnotationProperty](http://www.w3.org/2002/07/owl#AnnotationProperty)
- example:myPredicate a [owl:ObjectProperty](http://www.w3.org/2002/07/owl#ObjectProperty)
- example:myPredicate a [owl:SymmetricProperty](http://www.w3.org/2002/07/owl#SymmetricProperty)
- example:myPredicate a [owl:TransitiveProperty](http://www.w3.org/2002/07/owl#TransitiveProperty)

In turn, these triples will have the following effects:

- example:myPredicate [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) "PredicateName"
- example:myPredicate [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) "Description of this class"
- example:myPredicate [skos:definition](http://www.w3.org/2004/02/skos/core#definition) "Description of this class"
- example:myPredicate [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) example:oneDomainType, example:anotherDomainTypeIfNeeded
- example:myPredicate [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) example:RangeType
- example:myPredicate [rdfs:subPropertyOf](http://www.w3.org/2000/01/rdf-schema#subPropertyOf) example:mySuperClass
