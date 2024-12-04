# WEN

## Schema Diagram

```mermaid
erDiagram
GeoWktLiteral {

}
HttpsStko-kwg.geog.ucsb.eduLodOntologyS2Cell {

}
SchemaGeoCoordinates {
    double schema_longitude  
    double schema_elevation  
    double schema_latitude  
}
SchemaGeoShape {

}
SchemaPlace {
    uri schema_additionalType  
    string schema_additionalType  
    string schema_name  
    string schema_description  
}
SchemaPropertyValue {
    uri schema_additionalType  
    string schema_additionalType  
    string schema_unitCode  
    string schema_name  
    string schema_description  
    string schema_propertyID  
    string schema_unitText  
    string schema_value  
    double schema_value  
}

SchemaGeoShape ||--|o GeoWktLiteral : "geo_asWKT"
SchemaGeoShape ||--|o SchemaPropertyValue : "schema_identifier"
SchemaPlace ||--|o SchemaGeoCoordinates : "schema_geo"
SchemaPlace ||--|o SchemaGeoShape : "schema_geo"
SchemaPlace ||--|o SchemaPropertyValue : "schema_variableMeasured"
SchemaPlace ||--|o SchemaPropertyValue : "schema_identifier"

```


## IRI prefixes

* geo: http://www.opengis.net/ont/geosparql#
* linkml: https://w3id.org/linkml/
* rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
* schema: https://schema.org/



## Classes

| Class | Description |
| --- | --- |
| [GeoWktLiteral](https://github.com/frink-okn/graph-descriptions/blob/main/ufokn-kg/classes/GeoWktLiteral.md) | None<br/>| 
| [HttpsStko-kwg.geog.ucsb.eduLodOntologyS2Cell](https://github.com/frink-okn/graph-descriptions/blob/main/ufokn-kg/classes/HttpsStko-kwg.geog.ucsb.eduLodOntologyS2Cell.md) | No type description provided<br/>Class with 11717916 occurences.| 
| [SchemaGeoCoordinates](https://github.com/frink-okn/graph-descriptions/blob/main/ufokn-kg/classes/SchemaGeoCoordinates.md) | The geographic coordinates of a place or event.<br/>Class with 5858958 occurences.| 
| [SchemaGeoShape](https://github.com/frink-okn/graph-descriptions/blob/main/ufokn-kg/classes/SchemaGeoShape.md) | The geographic shape of a place. A GeoShape can be described using several properties whose values are based on latitude/longitude pairs. Either whitespace or commas can be used to separate latitude and longitude; whitespace should be used when writing a list of several such points.<br/>Class with 5858958 occurences.| 
| [SchemaPlace](https://github.com/frink-okn/graph-descriptions/blob/main/ufokn-kg/classes/SchemaPlace.md) | Entities that have a somewhat fixed, physical extension.<br/>Class with 5839329 occurences.| 
| [SchemaPropertyValue](https://github.com/frink-okn/graph-descriptions/blob/main/ufokn-kg/classes/SchemaPropertyValue.md) | A property-value pair, e.g. representing a feature of a product or place. Use the 'name' property for the name of the property. If there is an additional human-readable version of the value, put that into the 'description' property.\n\n Always use specific schema.org properties when a) they exist and b) you can populate them. Using PropertyValue as a substitute will typically not trigger the same effect as using the original, specific property.
    <br/>Class with 41012706 occurences.| 





## Slots

| Slot | Description |
| --- | --- |
| [geo_asWKT](https://github.com/frink-okn/graph-descriptions/blob/main/ufokn-kg/slots/geo_asWKT.md) | No slot description provided<br/>5858958 occurrences with subject type schema_GeoShape and object type geo_wktLiteral.|
| [schema_additionalType](https://github.com/frink-okn/graph-descriptions/blob/main/ufokn-kg/slots/schema_additionalType.md) | No slot description provided<br/>11717916 occurrences with subject type schema_PropertyValue and object type uri.<br/>5839332 occurrences with subject type schema_Place and object type string.|
| [schema_description](https://github.com/frink-okn/graph-descriptions/blob/main/ufokn-kg/slots/schema_description.md) | No slot description provided<br/>17576874 occurrences with subject type schema_PropertyValue and object type string.<br/>5846397 occurrences with subject type schema_Place and object type string.|
| [schema_elevation](https://github.com/frink-okn/graph-descriptions/blob/main/ufokn-kg/slots/schema_elevation.md) | No slot description provided<br/>5858958 occurrences with subject type schema_GeoCoordinates and object type double.|
| [schema_geo](https://github.com/frink-okn/graph-descriptions/blob/main/ufokn-kg/slots/schema_geo.md) | No slot description provided<br/>5858958 occurrences with subject type schema_Place and object type schema_GeoCoordinates.<br/>5858958 occurrences with subject type schema_Place and object type schema_GeoShape.|
| [schema_identifier](https://github.com/frink-okn/graph-descriptions/blob/main/ufokn-kg/slots/schema_identifier.md) | No slot description provided<br/>11717916 occurrences with subject type schema_GeoShape and object type schema_PropertyValue.<br/>23435832 occurrences with subject type schema_Place and object type schema_PropertyValue.|
| [schema_latitude](https://github.com/frink-okn/graph-descriptions/blob/main/ufokn-kg/slots/schema_latitude.md) | No slot description provided<br/>5858958 occurrences with subject type schema_GeoCoordinates and object type double.|
| [schema_longitude](https://github.com/frink-okn/graph-descriptions/blob/main/ufokn-kg/slots/schema_longitude.md) | No slot description provided<br/>5858958 occurrences with subject type schema_GeoCoordinates and object type double.|
| [schema_name](https://github.com/frink-okn/graph-descriptions/blob/main/ufokn-kg/slots/schema_name.md) | No slot description provided<br/>41012706 occurrences with subject type schema_PropertyValue and object type string.<br/>5839329 occurrences with subject type schema_Place and object type string.|
| [schema_propertyID](https://github.com/frink-okn/graph-descriptions/blob/main/ufokn-kg/slots/schema_propertyID.md) | No slot description provided<br/>5858958 occurrences with subject type schema_PropertyValue and object type string.|
| [schema_unitCode](https://github.com/frink-okn/graph-descriptions/blob/main/ufokn-kg/slots/schema_unitCode.md) | No slot description provided<br/>5858958 occurrences with subject type schema_PropertyValue and object type string.|
| [schema_unitText](https://github.com/frink-okn/graph-descriptions/blob/main/ufokn-kg/slots/schema_unitText.md) | No slot description provided<br/>5858958 occurrences with subject type schema_PropertyValue and object type string.|
| [schema_value](https://github.com/frink-okn/graph-descriptions/blob/main/ufokn-kg/slots/schema_value.md) | No slot description provided<br/>35153748 occurrences with subject type schema_PropertyValue and object type string.<br/>5858958 occurrences with subject type schema_PropertyValue and object type double.|
| [schema_variableMeasured](https://github.com/frink-okn/graph-descriptions/blob/main/ufokn-kg/slots/schema_variableMeasured.md) | No slot description provided<br/>5858958 occurrences with subject type schema_Place and object type schema_PropertyValue.|







