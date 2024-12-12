# Query Knowledge Graphs in FRINK

## FRINK Query Page

FRINK offers a query page that enables anyone to query specific Theme 1 graphs or query across graphs (i.e., a federated query). The FRINK Query Page is located at [https://frink.apps.renci.org](https://frink.apps.renci.org).

### Query Specific Graphs
The query page allows selection of a single knowledge graph or multiple knowledge graphs to query. 

From the **Sources** drop-down menu (shown below)

<img src="../../assets/images/Sources-DropDown-Empty.png" width="400"> 

You can select one or many of the graphs comprising FRINK.

<img src="../../assets/images/SourcesDropDown2.png" width="400">

Then you can construct a query in SPARQL using the **SPARQL Query** pane and run the query against the data sources you selected in the **Sources** drop down. Click the **Run Query** button to execute the query.

<img src="../../assets/images/SPARQLQueryPane.png" width="400">

### Query Using Examples
In the **EXAMPLES** pane, you can select a pre-formulated SPARQL query from the list. The **EXAMPLES** pane includes queries from distinct Theme 1 graphs as well as from other graphs that are used in the OKN (e.g., Ubergraph), with each example query clearly labeled. 

<img src="../../assets/images/ExamplesPane.png" width="400">

### Query Across Graphs

If the you wish to query over all available data sources, select FRINK Federated SPARQL from the Sources drop down. Be sure to deselect all other sources. This will submit the query to a server-side endpoint federating all sources.

<img src="../../assets/images/Federated.png" width="400">

### Saving Queries and Downloading Output

In the **SPARQL Query** pane, you can click the **Save Query** button to save your query. It will appear in the **SAVED** panel as shown below.

<img src="../../assets/images/Saved.png" width="400">

In the **RESULTS** pane, you can click the blue download button to download the output of your query. The button is circled in red below.

<img src="../../assets/images/Results2.png" width="400">

## SPARQL Endpoints

FRINK deploys standardized API endpoints for each hosted knowledge graph. Currently FRINK provides the following kinds of APIs:

- [SPARQL](https://www.w3.org/TR/sparql11-query/): SPARQL is the standard graph querying language for RDF datasets.

- [TPF](https://linkeddatafragments.org/specification/triple-pattern-fragments/): TPF (Triple Pattern Fragments) is a low-cost interface to RDF datasets that supports querying a single triple pattern at a time.

The FRINK API endpoints can be used progammatically (see below), or else accessed using the FRINK SPARQL query page, built on the [Comunica](https://comunica.dev/) knowledge graph querying framework.

### Theme 1 Specific Endpoints

The following knowledge graphs are currently available within FRINK. The SPARQL endpoints are service endpoints only (no user interface). You can query them via the FRINK query page, or using a third party SPARQL tool such as [Yasgui](https://yasgui.triply.cc). The TPF endpoints are service endpoints but also provide a browser UI.

- climatepub4-kg
    - SPARQL: `https://frink.apps.renci.org/climatepub4kg/sparql`
    - TPF: `https://frink.apps.renci.org/ldf/climatepub4kg`
- DREAM-KG
    - SPARQL: `https://frink.apps.renci.org/dreamkg/sparql`
    - TPF: `https://frink.apps.renci.org/ldf/dreamkg`
- FIO-KG
    - SPARQL: `https://frink.apps.renci.org/fiokg/sparql`
    - TPF: `https://frink.apps.renci.org/ldf/fiokg`
- Geoconnex
    - SPARQL: `https://frink.apps.renci.org/geoconnex/sparql`
    - TPF: `https://frink.apps.renci.org/ldf/geoconnex`
- Hydrology KG
    - SPARQL: `https://frink.apps.renci.org/hydrologykg/sparql`
    - TPF: `https://frink.apps.renci.org/ldf/hydrologykg`
- SCALES
    - SPARQL: `https://frink.apps.renci.org/scales/sparql`
    - TPF: `https://frink.apps.renci.org/ldf/scales`
- Secure Chain KG
    - SPARQL: `https://frink.apps.renci.org/securechainkg/sparql`
    - TPF: `https://frink.apps.renci.org/ldf/securechainkg`
- SemOpenAlex (via CollabNext)
    - SPARQL: `https://frink.apps.renci.org/semopenalex/sparql`
    - TPF: `https://frink.apps.renci.org/ldf/semopenalex`
- SOC-KG
    - SPARQL: `https://frink.apps.renci.org/sockg/sparql`
    - TPF: `https://frink.apps.renci.org/ldf/sockg`
- Spatial KG
    - SPARQL: `https://frink.apps.renci.org/spatialkg/sparql`
    - TPF: `https://frink.apps.renci.org/ldf/spatialkg`
- SPOKE-KG
    - SPARQL: `https://frink.apps.renci.org/spoke/sparql`
    - TPF: `https://frink.apps.renci.org/ldf/spoke`
- SUD-OKN
    - SPARQL: `https://frink.apps.renci.org/sudokn/sparql`
    - TPF: `https://frink.apps.renci.org/ldf/sudokn`
- UF-OKN
    - SPARQL: `https://frink.apps.renci.org/ufokn/sparql`
    - TPF: `https://frink.apps.renci.org/ldf/ufokn`
- Ubergraph
    - SPARQL: `https://frink.apps.renci.org/ubergraph/sparql`
    - TPF: `https://frink.apps.renci.org/ldf/ubergraph`
- Wildlife-KG
    - SPARQL: `https://frink.apps.renci.org/wildlifekg/sparql`
    - TPF: `https://frink.apps.renci.org/ldf/wildlifekg`
- Wikidata
    - SPARQL: `https://frink.apps.renci.org/wikidata/sparql`
    - TPF: `https://frink.apps.renci.org/ldf/wikidata`

### Federated query endpoint
- SPARQL: `https://frink.apps.renci.org/federation/sparql`
