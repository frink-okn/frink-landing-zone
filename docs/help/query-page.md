# Query FRINK using Comunica

FRINK  has a query page that is built using [Comunica](https://comunica.dev/), a knowledge graph querying framework.
The query page can be accessed at [https://frink.apps.renci.org](https://frink.apps.renci.org).

###  Data Sources

The Query page allows selection of a single knowledge graph or multiple knowledge graphs to query. This selection can be
done using the data source selection dropdown as seen below. 

<img src="../../assets/images/query-page-datasource-dropdown.png" width="600">


### Querying 

The query is configured with a few examples that span few different knowledge sources and their combination. The example
queries could be selected using `pick a query` dropdown. In addition to these examples, users can opt to write their own query
and execute it against the data sources selected. Once ready , clicking on the `Execute` button triggers the query. The
query can be stopped using `Stop execution` button which show's up in place of `Execute`, once querying starts. 

<img src="../../assets/images/query-page-datasource-query-box.png" width="600">


### Query Results and Execution Log

Results of the execution will be shown in the `Query results` section of the page. We have added support for exporting 
results to csv file , this can be done using `Download CSV` button. Similarly, the execution logs can be downloaded using
the `Download Log` button. 

<img src="../../assets/images/query-page-query-results-exec-logs.png" width="600">
