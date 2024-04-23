# Querying knowledge graphs in FRINK

FRINK deploys standardized API endpoints for each hosted knowledge graph. Currently FRINK provides the following kinds of APIs:

- [SPARQL](https://www.w3.org/TR/sparql11-query/): SPARQL is the standard graph querying language for RDF datasets.
- [TPF](https://linkeddatafragments.org/specification/triple-pattern-fragments/): TPF (Triple Pattern Fragments) is a low-cost interface to RDF datasets that supports querying a single triple pattern at a time.

The FRINK API endpoints can be used progammatically (see below), or else accessed using the FRINK SPARQL query page, built on the [Comunica](https://comunica.dev/) knowledge graph querying framework. The query page can be accessed at [https://frink.apps.renci.org](https://frink.apps.renci.org).

## FRINK SPARQL query page

The [FRINK query interface](https://frink.apps.renci.org) is under active development, and currently provides a bare bones tool to submit SPARQL queries, either to a single data source or to a combination of sources (federated query).

###  Data Sources

The query page allows selection of a single knowledge graph or multiple knowledge graphs to query. This selection can be
done using the data source selection dropdown as seen below. 

<img src="../../assets/images/query-page-datasource-dropdown.png" width="600">

### Querying 

The query page is configured with a few examples that span a few different knowledge sources and their combination. The example
queries can be selected using the `pick a query` dropdown. In addition to these examples, users can opt to write their own query and execute it against the data sources selected. Once ready, clicking on the `Execute` button triggers the query. The query can be stopped using `Stop execution` button which shows up in place of `Execute`, once querying starts. 

<img src="../../assets/images/query-page-datasource-query-box.png" width="600">

#### Federated query (query over multiple sources)

As stated above, multiple data sources can be selected prior to querying. When querying over multiple sources, the query engine executes the query within the user's browser, accessing data from each source's TPF endpoint. This will typically be slower than submitting a SPARQL query to a single endpoint; however there is no query timeout. If the user wishes to query over all available data sources, a faster option is to select the source labelled "FRINK Federated SPARQL" (and deselect all other sources). This will submit the query to a server-side endpoint federating all sources. In the future we plan to allow arbitrary combinations of sources to execute using the faster server-side query engine.

### Query Results

Results of the query will be shown in the `Query results` section of the page. Use the `Download` button to download a file of all results.

## API endpoints

The following knowledge graphs are currently available within FRINK. The SPARQL endpoints are service endpoints only (no user interface). You can query them via the FRINK query page, or using a third party SPARQL tool such as [Yasgui](https://yasgui.triply.cc). The TPF endpoints are service endpoints but also provide a browser UI.

- DREAM-KG
    - SPARQL: `https://frink.apps.renci.org/dreamkg/sparql`
    - TPF: `https://frink.apps.renci.org/ldf/dreamkg`
- SCALES
    - SPARQL: `https://frink.apps.renci.org/scales/sparql`
    - TPF: `https://frink.apps.renci.org/ldf/scales`
- SemOpenAlex (via CollabNext)
    - SPARQL: `https://frink.apps.renci.org/semopenalex/sparql`
    - TPF: `https://frink.apps.renci.org/ldf/semopenalex`
- SOC-KG
    - SPARQL: `https://frink.apps.renci.org/sockg/sparql`
    - TPF: `https://frink.apps.renci.org/ldf/sockg`
- SUD-OKN
    - SPARQL: `https://frink.apps.renci.org/sudokn/sparql`
    - TPF: `https://frink.apps.renci.org/ldf/sudokn`
- UF-OKN
    - SPARQL: `https://frink.apps.renci.org/ufokn/sparql`
    - TPF: `https://frink.apps.renci.org/ldf/ufokn`
- Ubergraph
    - SPARQL: `https://frink.apps.renci.org/ubergraph/sparql`
    - TPF: `https://frink.apps.renci.org/ldf/ubergraph`
- Wikidata
    - SPARQL: `https://frink.apps.renci.org/wikidata/sparql`
    - TPF: `https://frink.apps.renci.org/ldf/wikidata`

### Federated query
- SPARQL: `https://frink.apps.renci.org/federation/sparql`
