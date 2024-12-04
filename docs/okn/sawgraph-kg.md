# The PFAS specific concepts that extend ContaminOSO

the Contaminant Observation and Samples Ontology (ContaminOSO) developed as part of the AIKnowsPFAS and SAWGraph projects.

URI: sawgraph-kg

Name: sawgraph-kg



## Schema Diagram

```mermaid
erDiagram
ContaminosoAggregateContaminantMeasurement {
    uri meegad_validationQualifier  
    uri contaminoso_resultAnnotation  
    uri meegad_validationLevel  
    uri qudt_quantityValue  
    string rdfs_label  
    uri rdfs_label  
}
ContaminosoAnalysisMethod {

}
ContaminosoContaminantConcentrationMeasurement {

}
ContaminosoContaminantMeasurement {
    uri meegad_validationQualifier  
    uri contaminoso_resultAnnotation  
    uri meegad_validationLevel  
    uri qudt_quantityValue  
    string rdfs_label  
    uri rdfs_label  
}
ContaminosoContaminantObservation {
    date contaminoso_analysisDate  
    date contaminoso_sampleTime  
    uri contaminoso_analyzedSample  
    uri contaminoso_hasTemporalCoverage  
    uri contaminoso_ofSubstance  
    date sosa_resultTime  
    uri contaminoso_hasAggregationPeriod  
    string rdfs_label  
    uri rdfs_label  
    string http___sawgraph.spatialai.org_v1_us_epa_ghg#GHG_Subpart  
    uri contaminoso_sampledFeature  
    uri sosa_observedProperty  
    date contaminoso_sampledTime  
}
ContaminosoContaminantVolumeMeasurement {

}
ContaminosoFeature {
    string usfrs_hasGHGId  
    uri http___stko_kwg.geog.ucsb.edu_lod_ontology_spatialRelation  
    date ussdwis_lastReport  
    uri geo_hasGeometry  
    string ussdwis_pwsName  
    string ussdwis_hasPWSID  
    date ussdwis_firstReport  
    string ussdwis_hasOwnership  
    string ussdwis_sizeCategory  
    string rdfs_label  
    uri rdfs_label  
    string ussdwis_primarySource  
    string ilisgs_hasOwner  
    integer ussdwis_populationServed  
    string ussdwis_hasActivity  
    string ilisgs_hasISWSId  
    string ussdwis_hasName  
    date ussdwis_deactivationDate  
    integer ussdwis_serviceConnections  
    uri http___stko_kwg.geog.ucsb.edu_lod_ontology_sfWithin  
}
ContaminosoMaterialSample {
    uri meegad_sampleCollectionMethod  
    uri contaminoso_ofSampleMaterialType  
    string meegad_sampleID  
    uri contaminoso_sampleAnnotation  
    uri meegad_sampleTreatmentStatus  
    string ussdwis_sampleID  
    uri contaminoso_fromSamplePoint  
    uri meegad_sampleCollectionLocation  
    string rdfs_label  
    uri rdfs_label  
}
ContaminosoMaterialType {
    string rdfs_label  
    uri rdfs_label  
}
ContaminosoMaximumConcentration {

}
ContaminosoMinimumConcentration {

}
ContaminosoObservationAnnotation {
    string rdfs_label  
    uri rdfs_label  
}
ContaminosoPoint {
    string ussdwis_SamplePointID  
    integer meegad_samplePointNumber  
    uri http___stko_kwg.geog.ucsb.edu_lod_ontology_spatialRelation  
    string meegad_samplePointWebName  
    uri geo_hasGeometry  
    uri http___stko_kwg.geog.ucsb.edu_lod_ontology_sfWithin  
    string rdfs_label  
    uri rdfs_label  
}
ContaminosoReleaseContaminantObservation {

}
ContaminosoReleaseFeature {

}
ContaminosoReleasePoint {

}
ContaminosoResultQualifier {
    uri contaminoso_resultAnnotation  
    string meegad_parameterGroup  
    string rdfs_label  
    uri rdfs_label  
    decimal qudt_numericValue  
    double qudt_numericValue  
}
ContaminosoSampleAnnotation {
    string rdfs_label  
    uri rdfs_label  
}
ContaminosoSampleContaminantObservation {

}
ContaminosoSampleMaterialType {

}
ContaminosoSamplePoint {

}
ContaminosoSampledFeature {

}
ContaminosoSampledFeaure {

}
ContaminosoSingleContaminantMeasurement {

}
ContaminosoSingleContaminantObservation {

}
ContaminosoSubstance {
    string http___sawgraph.spatialai.org_v1_us_epa_ghg#chemicalFormula  
    string http___sawgraph.spatialai.org_v1_me_egad_data#dep_chemicalID  
    string rdfs_label  
    uri rdfs_label  
    string contaminoso_substanceID  
    string meegad_parameterName  
    string http___sawgraph.spatialai.org_v1_us_epa_ghg#casNumber  
    string meegad_parameterAbbreviation  
    string contaminoso_casNumber  
}
GeoFeature {

}
GeoGeometry {

}
GeoSpatialObject {

}
GeoDggsLiteral {

}
GeoGeoJSONLiteral {

}
GeoGmlLiteral {

}
GeoKmlLiteral {

}
GeoWktLiteral {

}
HttpQudt.orgVocabUnitUnit {
    string rdfs_label  
    uri rdfs_label  
}
HttpSawgraph.spatialai.orgV1Stad#Quantity {
    uri https___qudt.org_schema_qudt_unit  
    float https___qudt.org_schema_qudt_numericValue  
}
HttpSawgraph.spatialai.orgV1Stad#SingleData {
    uri https___qudt.org_schema_qudt_unit  
    float https___qudt.org_schema_qudt_numericValue  
}
HttpSawgraph.spatialai.orgV1Stad#StatisticalAggregateData {
    uri https___qudt.org_schema_qudt_unit  
    float https___qudt.org_schema_qudt_numericValue  
}
HttpSawgraph.spatialai.orgV1Stad#StatisticalQuantityKind {

}
HttpSawgraph.spatialai.orgV1Us-epa-ghg#Amount {
    uri https___qudt.org_schema_qudt_unit  
    float https___qudt.org_schema_qudt_numericValue  
}
HttpSawgraph.spatialai.orgV1Us-epa-ghg#Chemical {

}
HttpSawgraph.spatialai.orgV1Us-epa-ghg#Measurement {

}
HttpSawgraph.spatialai.orgV1Us-epa-ghg#ReleaseObservation {

}
HttpStko-kwg.geog.ucsb.eduLodOntologyS2CellLevel13 {
    uri http___stko_kwg.geog.ucsb.edu_lod_ontology_spatialRelation  
}
HttpWww.opengis.netOntSf#Point {

}
HttpsQudt.orgSchemaQudtQuantityValue {

}
IlisgsISGS-Well {

}
IlisgsWellDepthInFt {
    float https___qudt.org_schema_qudt_numericValue  
    uri https___qudt.org_schema_qudt_unit  
}
IlisgsWellPurpose {
    string rdfs_label  
    uri rdfs_label  
}
IlisgsWellYield {
    uri https___qudt.org_schema_qudt_unit  
    float https___qudt.org_schema_qudt_numericValue  
}
MeegadEGAD-AggregatePFAS-Concentration {

}
MeegadEGAD-AnalysisMethod {
    string rdfs_label  
    uri rdfs_label  
}
MeegadEGAD-LabQualifier {
    uri contaminoso_resultAnnotation  
    string meegad_parameterGroup  
    string rdfs_label  
    uri rdfs_label  
    decimal qudt_numericValue  
    double qudt_numericValue  
}
MeegadEGAD-MethodDetectionLimit {

}
MeegadEGAD-PFAS-Observation {

}
MeegadEGAD-PFAS-ParameterName {

}
MeegadEGAD-ReportingLimit {

}
MeegadEGAD-ResultType {
    string rdfs_label  
    uri rdfs_label  
}
MeegadEGAD-Sample {

}
MeegadEGAD-SampleCollectionMethod {
    string rdfs_label  
    uri rdfs_label  
}
MeegadEGAD-SampleDetailedLocation {
    string rdfs_label  
    uri rdfs_label  
}
MeegadEGAD-SampleMaterialType {
    string rdfs_label  
    uri rdfs_label  
}
MeegadEGAD-SamplePoint {

}
MeegadEGAD-SamplePointType {
    string rdfs_label  
    uri rdfs_label  
}
MeegadEGAD-SampleTreatmentStatus {
    string rdfs_label  
    uri rdfs_label  
}
MeegadEGAD-SampledFeature {

}
MeegadEGAD-SinglePFAS-Concentration {

}
MeegadEGAD-Site {
    string http___sawgraph.spatialai.org_v1_sdwis#pwsidNumber  
    integer meegad_siteNumber  
    uri http___stko_kwg.geog.ucsb.edu_lod_ontology_spatialRelation  
    string meegad_siteName  
    uri geo_hasGeometry  
    uri http___stko_kwg.geog.ucsb.edu_lod_ontology_sfWithin  
    string rdfs_label  
    uri rdfs_label  
}
MeegadEGAD-SiteType {
    string http___www.w3.org_2008_05_skos#definition  
    string rdfs_label  
    uri rdfs_label  
}
MeegadEGAD-ValidationLevel {
    uri contaminoso_resultAnnotation  
    string meegad_parameterGroup  
    string rdfs_label  
    uri rdfs_label  
    decimal qudt_numericValue  
    double qudt_numericValue  
}
MeegadEGAD-ValidationQualifier {
    uri contaminoso_resultAnnotation  
    string meegad_parameterGroup  
    string rdfs_label  
    uri rdfs_label  
    decimal qudt_numericValue  
    double qudt_numericValue  
}
MemgsMGS-Well {

}
MemgsWellDepthInFt {
    uri https___qudt.org_schema_qudt_unit  
    float https___qudt.org_schema_qudt_numericValue  
}
MemgsWellOverburdenThicknessInFt {
    uri https___qudt.org_schema_qudt_unit  
    float https___qudt.org_schema_qudt_numericValue  
}
MemgsWellType {

}
MemgsWellUse {

}
OwlNamedIndividual {

}
PfasAggregatePFASAmountMeasurement {

}
PfasAggregatePFASConcentrationMeasurement {

}
PfasAnalysisMethod {

}
PfasMethodDetectionLimit {
    uri contaminoso_resultAnnotation  
    string meegad_parameterGroup  
    string rdfs_label  
    uri rdfs_label  
    decimal qudt_numericValue  
    double qudt_numericValue  
}
PfasPFAS-ConcentrationMeasurement {

}
PfasPFAS-ContaminantObservation {

}
PfasPFAS-ReleaseContaminantObservation {

}
PfasPFAS-SampleContaminantObservation {

}
PfasPFAS-VolumeMeasurement {

}
PfasQuantitationLimit {
    uri contaminoso_resultAnnotation  
    string meegad_parameterGroup  
    string rdfs_label  
    uri rdfs_label  
    decimal qudt_numericValue  
    double qudt_numericValue  
}
PfasReportingLimit {
    uri contaminoso_resultAnnotation  
    string meegad_parameterGroup  
    string rdfs_label  
    uri rdfs_label  
    decimal qudt_numericValue  
    double qudt_numericValue  
}
PfasSinglePFASConcentrationMeasurement {

}
ProvOrganization {
    string rdfs_label  
    uri rdfs_label  
}
RdfList {

}
SosaFeatureOfInterest {

}
SosaObservableProperty {

}
SosaObservation {

}
SosaProcedure {

}
SosaResult {

}
SosaSample {

}
UsfrsFRS-Facility {

}
UssdwisAmount {
    uri https___qudt.org_schema_qudt_unit  
    float https___qudt.org_schema_qudt_numericValue  
}
UssdwisCombinedDistributionSystem {

}
UssdwisPWS-Observation {

}
UssdwisPWS-PFAS {

}
UssdwisPWS-PFASConcentration {

}
UssdwisPWS-Sample {

}
UssdwisPWS-SamplePoint {

}
UssdwisPublicWaterSystem {

}
UssdwisPublicWaterSystem-CWS {

}
UssdwisPublicWaterSystem-GW {

}
UssdwisPublicWaterSystem-NTNCWS {

}
UssdwisPublicWaterSystem-SW {

}
UssdwisPublicWaterSystem-TNCWS {

}
UssdwisSampledFeature {

}

ContaminosoAggregateContaminantMeasurement ||--|o ContaminosoResultQualifier : "meegad_validationQualifier"
ContaminosoAggregateContaminantMeasurement ||--|o ContaminosoResultQualifier : "meegad_labQualifier"
ContaminosoAggregateContaminantMeasurement ||--|o ContaminosoResultQualifier : "contaminoso_resultAnnotation"
ContaminosoAggregateContaminantMeasurement ||--|o ContaminosoResultQualifier : "meegad_validationLevel"
ContaminosoAggregateContaminantMeasurement ||--|o HttpSawgraph.spatialai.orgV1Stad#Quantity : "https___qudt.org_schema_qudt_quantityKind"
ContaminosoContaminantMeasurement ||--|o ContaminosoResultQualifier : "meegad_validationQualifier"
ContaminosoContaminantMeasurement ||--|o ContaminosoResultQualifier : "meegad_labQualifier"
ContaminosoContaminantMeasurement ||--|o ContaminosoResultQualifier : "contaminoso_resultAnnotation"
ContaminosoContaminantMeasurement ||--|o ContaminosoResultQualifier : "meegad_validationLevel"
ContaminosoContaminantMeasurement ||--|o UssdwisAmount : "https___qudt.org_schema_qudt_quantityValue"
ContaminosoContaminantObservation ||--|o ContaminosoAggregateContaminantMeasurement : "contaminoso_hasResult"
ContaminosoContaminantObservation ||--|o MeegadEGAD-AnalysisMethod : "contaminoso_analysisMethod"
ContaminosoContaminantObservation ||--|o ContaminosoFeature : "contaminoso_hasFeatureOfInterest"
ContaminosoContaminantObservation ||--|o ProvOrganization : "contaminoso_analyzedBy"
ContaminosoContaminantObservation ||--|o ContaminosoFeature : "sosa_hasFeatureOfInterest"
ContaminosoContaminantObservation ||--|o ContaminosoMaterialSample : "meegad_analyzedSample"
ContaminosoContaminantObservation ||--|o ContaminosoFeature : "contaminoso_fromSampledFeature"
ContaminosoContaminantObservation ||--|o ContaminosoMaterialSample : "contaminoso_analyzedSample"
ContaminosoContaminantObservation ||--|o ContaminosoSubstance : "contaminoso_ofSubstance"
ContaminosoContaminantObservation ||--|o ContaminosoContaminantMeasurement : "sosa_hasResult"
ContaminosoContaminantObservation ||--|o ContaminosoAggregateContaminantMeasurement : "sosa_hasResult"
ContaminosoContaminantObservation ||--|o ContaminosoPoint : "contaminoso_observedAtSamplePoint"
ContaminosoContaminantObservation ||--|o ContaminosoFeature : "contaminoso_sampledFeature"
ContaminosoContaminantObservation ||--|o ContaminosoObservationAnnotation : "meegad_resultType"
ContaminosoContaminantObservation ||--|o ContaminosoSubstance : "sosa_observedProperty"
ContaminosoContaminantObservation ||--|o ContaminosoObservationAnnotation : "contaminoso_observationAnnotation"
ContaminosoFeature ||--|o MeegadEGAD-SamplePointType : "meegad_sampledFeatureType"
ContaminosoFeature ||--|o ContaminosoFeature : "http___stko-kwg.geog.ucsb.edu_lod_ontology_spatialRelation"
ContaminosoFeature ||--|o HttpStko-kwg.geog.ucsb.eduLodOntologyS2CellLevel13 : "http___stko-kwg.geog.ucsb.edu_lod_ontology_spatialRelation"
ContaminosoFeature ||--|o MeegadEGAD-Site : "http___stko-kwg.geog.ucsb.edu_lod_ontology_spatialRelation"
ContaminosoFeature ||--|o ContaminosoPoint : "http___stko-kwg.geog.ucsb.edu_lod_ontology_spatialRelation"
ContaminosoFeature ||--|o ContaminosoFeature : "ussdwis_inCombinedSystem"
ContaminosoFeature ||--|o GeoSpatialObject : "geo_hasGeometry"
ContaminosoFeature ||--|o GeoGeometry : "geo_hasGeometry"
ContaminosoFeature ||--|o IlisgsWellPurpose : "ilisgs_wellPurpose"
ContaminosoFeature ||--|o GeoGeometry : "geo_hasDefaultGeometry"
ContaminosoFeature ||--|o IlisgsWellDepthInFt : "ilisgs_wellDepth"
ContaminosoFeature ||--|o IlisgsWellYield : "ilisgs_wellYield"
ContaminosoFeature ||--|o GeoGeometry : "geo_defaultGeometry"
ContaminosoFeature ||--|o HttpStko-kwg.geog.ucsb.eduLodOntologyS2CellLevel13 : "http___stko-kwg.geog.ucsb.edu_lod_ontology_sfWithin"
ContaminosoFeature ||--|o GeoWktLiteral : "geo_hasSerialization"
ContaminosoMaterialSample ||--|o ContaminosoSampleAnnotation : "meegad_sampleCollectionMethod"
ContaminosoMaterialSample ||--|o ContaminosoMaterialType : "contaminoso_ofSampleMaterialType"
ContaminosoMaterialSample ||--|o ContaminosoSampleAnnotation : "contaminoso_sampleAnnotation"
ContaminosoMaterialSample ||--|o ContaminosoSampleAnnotation : "meegad_sampleTreatmentStatus"
ContaminosoMaterialSample ||--|o ContaminosoPoint : "contaminoso_fromSamplePoint"
ContaminosoMaterialSample ||--|o ContaminosoSampleAnnotation : "meegad_sampleCollectionLocation"
ContaminosoPoint ||--|o MeegadEGAD-SamplePointType : "meegad_samplePointType"
ContaminosoPoint ||--|o MeegadEGAD-Site : "meegad_associatedSite"
ContaminosoPoint ||--|o ContaminosoFeature : "http___stko-kwg.geog.ucsb.edu_lod_ontology_spatialRelation"
ContaminosoPoint ||--|o HttpStko-kwg.geog.ucsb.eduLodOntologyS2CellLevel13 : "http___stko-kwg.geog.ucsb.edu_lod_ontology_spatialRelation"
ContaminosoPoint ||--|o MeegadEGAD-Site : "http___stko-kwg.geog.ucsb.edu_lod_ontology_spatialRelation"
ContaminosoPoint ||--|o ContaminosoPoint : "http___stko-kwg.geog.ucsb.edu_lod_ontology_spatialRelation"
ContaminosoPoint ||--|o ContaminosoFeature : "contaminoso_pointFromFeature"
ContaminosoPoint ||--|o GeoSpatialObject : "geo_hasGeometry"
ContaminosoPoint ||--|o GeoGeometry : "geo_hasGeometry"
ContaminosoPoint ||--|o HttpStko-kwg.geog.ucsb.eduLodOntologyS2CellLevel13 : "http___stko-kwg.geog.ucsb.edu_lod_ontology_sfWithin"
ContaminosoPoint ||--|o GeoGeometry : "geo_hasDefaultGeometry"
ContaminosoPoint ||--|o GeoWktLiteral : "geo_hasSerialization"
ContaminosoReleaseFeature ||--|o GeoWktLiteral : "geo_hasSerialization"
ContaminosoReleasePoint ||--|o GeoWktLiteral : "geo_hasSerialization"
ContaminosoResultQualifier ||--|o ContaminosoResultQualifier : "meegad_reportingLimit"
ContaminosoResultQualifier ||--|o ContaminosoResultQualifier : "meegad_methodDetectionLimit"
ContaminosoResultQualifier ||--|o ContaminosoResultQualifier : "contaminoso_resultAnnotation"
ContaminosoSamplePoint ||--|o GeoWktLiteral : "geo_hasSerialization"
ContaminosoSampledFeaure ||--|o GeoWktLiteral : "geo_hasSerialization"
GeoFeature ||--|o GeoWktLiteral : "geo_hasSerialization"
GeoGeometry ||--|o GeoWktLiteral : "geo_hasSerialization"
GeoGeometry ||--|o GeoWktLiteral : "geo_asWKT"
GeoSpatialObject ||--|o GeoWktLiteral : "geo_hasSerialization"
HttpStko-kwg.geog.ucsb.eduLodOntologyS2CellLevel13 ||--|o ContaminosoFeature : "http___stko-kwg.geog.ucsb.edu_lod_ontology_spatialRelation"
HttpStko-kwg.geog.ucsb.eduLodOntologyS2CellLevel13 ||--|o HttpStko-kwg.geog.ucsb.eduLodOntologyS2CellLevel13 : "http___stko-kwg.geog.ucsb.edu_lod_ontology_spatialRelation"
HttpStko-kwg.geog.ucsb.eduLodOntologyS2CellLevel13 ||--|o MeegadEGAD-Site : "http___stko-kwg.geog.ucsb.edu_lod_ontology_spatialRelation"
HttpStko-kwg.geog.ucsb.eduLodOntologyS2CellLevel13 ||--|o ContaminosoPoint : "http___stko-kwg.geog.ucsb.edu_lod_ontology_spatialRelation"
HttpStko-kwg.geog.ucsb.eduLodOntologyS2CellLevel13 ||--|o ContaminosoFeature : "http___stko-kwg.geog.ucsb.edu_lod_ontology_sfContains"
HttpStko-kwg.geog.ucsb.eduLodOntologyS2CellLevel13 ||--|o MeegadEGAD-Site : "http___stko-kwg.geog.ucsb.edu_lod_ontology_sfContains"
HttpStko-kwg.geog.ucsb.eduLodOntologyS2CellLevel13 ||--|o ContaminosoPoint : "http___stko-kwg.geog.ucsb.edu_lod_ontology_sfContains"
IlisgsISGS-Well ||--|o GeoWktLiteral : "geo_hasSerialization"
MeegadEGAD-LabQualifier ||--|o ContaminosoResultQualifier : "meegad_reportingLimit"
MeegadEGAD-LabQualifier ||--|o ContaminosoResultQualifier : "meegad_methodDetectionLimit"
MeegadEGAD-LabQualifier ||--|o ContaminosoResultQualifier : "contaminoso_resultAnnotation"
MeegadEGAD-SamplePoint ||--|o GeoWktLiteral : "geo_hasSerialization"
MeegadEGAD-Site ||--|o ContaminosoFeature : "http___stko-kwg.geog.ucsb.edu_lod_ontology_spatialRelation"
MeegadEGAD-Site ||--|o HttpStko-kwg.geog.ucsb.eduLodOntologyS2CellLevel13 : "http___stko-kwg.geog.ucsb.edu_lod_ontology_spatialRelation"
MeegadEGAD-Site ||--|o MeegadEGAD-Site : "http___stko-kwg.geog.ucsb.edu_lod_ontology_spatialRelation"
MeegadEGAD-Site ||--|o ContaminosoPoint : "http___stko-kwg.geog.ucsb.edu_lod_ontology_spatialRelation"
MeegadEGAD-Site ||--|o GeoSpatialObject : "geo_hasGeometry"
MeegadEGAD-Site ||--|o GeoGeometry : "geo_hasGeometry"
MeegadEGAD-Site ||--|o HttpStko-kwg.geog.ucsb.eduLodOntologyS2CellLevel13 : "http___stko-kwg.geog.ucsb.edu_lod_ontology_sfWithin"
MeegadEGAD-Site ||--|o GeoGeometry : "geo_hasDefaultGeometry"
MeegadEGAD-ValidationLevel ||--|o ContaminosoResultQualifier : "meegad_reportingLimit"
MeegadEGAD-ValidationLevel ||--|o ContaminosoResultQualifier : "meegad_methodDetectionLimit"
MeegadEGAD-ValidationLevel ||--|o ContaminosoResultQualifier : "contaminoso_resultAnnotation"
MeegadEGAD-ValidationQualifier ||--|o ContaminosoResultQualifier : "meegad_reportingLimit"
MeegadEGAD-ValidationQualifier ||--|o ContaminosoResultQualifier : "meegad_methodDetectionLimit"
MeegadEGAD-ValidationQualifier ||--|o ContaminosoResultQualifier : "contaminoso_resultAnnotation"
MemgsMGS-Well ||--|o GeoWktLiteral : "geo_hasSerialization"
PfasMethodDetectionLimit ||--|o ContaminosoResultQualifier : "meegad_reportingLimit"
PfasMethodDetectionLimit ||--|o ContaminosoResultQualifier : "meegad_methodDetectionLimit"
PfasMethodDetectionLimit ||--|o ContaminosoResultQualifier : "contaminoso_resultAnnotation"
PfasQuantitationLimit ||--|o ContaminosoResultQualifier : "meegad_reportingLimit"
PfasQuantitationLimit ||--|o ContaminosoResultQualifier : "meegad_methodDetectionLimit"
PfasQuantitationLimit ||--|o ContaminosoResultQualifier : "contaminoso_resultAnnotation"
PfasReportingLimit ||--|o ContaminosoResultQualifier : "meegad_reportingLimit"
PfasReportingLimit ||--|o ContaminosoResultQualifier : "meegad_methodDetectionLimit"
PfasReportingLimit ||--|o ContaminosoResultQualifier : "contaminoso_resultAnnotation"
UsfrsFRS-Facility ||--|o GeoWktLiteral : "geo_hasSerialization"
UssdwisCombinedDistributionSystem ||--|o GeoWktLiteral : "geo_hasSerialization"
UssdwisPWS-SamplePoint ||--|o GeoWktLiteral : "geo_hasSerialization"
UssdwisPublicWaterSystem ||--|o GeoWktLiteral : "geo_hasSerialization"
UssdwisPublicWaterSystem-CWS ||--|o GeoWktLiteral : "geo_hasSerialization"
UssdwisPublicWaterSystem-GW ||--|o GeoWktLiteral : "geo_hasSerialization"
UssdwisPublicWaterSystem-NTNCWS ||--|o GeoWktLiteral : "geo_hasSerialization"
UssdwisPublicWaterSystem-SW ||--|o GeoWktLiteral : "geo_hasSerialization"
UssdwisPublicWaterSystem-TNCWS ||--|o GeoWktLiteral : "geo_hasSerialization"

```


## IRI prefixes

* contaminoso: http://sawgraph.spatialai.org/v1/contaminoso#
* dct: http://purl.org/dc/terms/
* geo: http://www.opengis.net/ont/geosparql#
* ilisgs: http://sawgraph.spatialai.org/v1/il-isgs#
* linkml: https://w3id.org/linkml/
* meegad: http://sawgraph.spatialai.org/v1/me-egad#
* memgs: http://sawgraph.spatialai.org/v1/me-mgs#
* owl: http://www.w3.org/2002/07/owl#
* pfas: http://sawgraph.spatialai.org/v1/pfas#
* prov: http://www.w3.org/ns/prov#
* qudt: http://qudt.org/schema/qudt/
* rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
* rdfs: http://www.w3.org/2000/01/rdf-schema#
* schema: https://schema.org/
* skos: http://www.w3.org/2004/02/skos/core#
* sosa: http://www.w3.org/ns/sosa/
* usfrs: http://sawgraph.spatialai.org/v1/us-frs#
* usfrsdata: http://sawgraph.spatialai.org/v1/us-frs-data#
* ussdwis: http://sawgraph.spatialai.org/v1/us-sdwis#
* xsd: http://www.w3.org/2001/XMLSchema#



## Classes

| Class | Description |
| --- | --- |
| [ContaminosoAnalysisMethod](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/ContaminosoAnalysisMethod.md) | No type description provided<br/>Class with 0 occurences.| 
| [ContaminosoMaterialType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/ContaminosoMaterialType.md) | No type description provided<br/>Class with 97 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeegadEGAD-SampleMaterialType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeegadEGAD-SampleMaterialType.md) | No type description provided<br/>Class with 97 occurences.| 
| [ContaminosoObservationAnnotation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/ContaminosoObservationAnnotation.md) | No type description provided<br/>Class with 12 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeegadEGAD-ResultType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeegadEGAD-ResultType.md) | No type description provided<br/>Class with 12 occurences.| 
| [ContaminosoResultQualifier](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/ContaminosoResultQualifier.md) | No type description provided<br/>Class with 283825 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeegadEGAD-LabQualifier](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeegadEGAD-LabQualifier.md) | No type description provided<br/>Class with 56 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeegadEGAD-ValidationLevel](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeegadEGAD-ValidationLevel.md) | No type description provided<br/>Class with 10 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeegadEGAD-ValidationQualifier](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeegadEGAD-ValidationQualifier.md) | No type description provided<br/>Class with 56 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PfasMethodDetectionLimit](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/PfasMethodDetectionLimit.md) | No type description provided<br/>Class with 141607 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PfasQuantitationLimit](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/PfasQuantitationLimit.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PfasReportingLimit](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/PfasReportingLimit.md) | No type description provided<br/>Class with 142152 occurences.| 
| [ContaminosoSampleAnnotation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/ContaminosoSampleAnnotation.md) | No type description provided<br/>Class with 160 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeegadEGAD-SampleCollectionMethod](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeegadEGAD-SampleCollectionMethod.md) | No type description provided<br/>Class with 113 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeegadEGAD-SampleDetailedLocation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeegadEGAD-SampleDetailedLocation.md) | No type description provided<br/>Class with 43 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeegadEGAD-SampleTreatmentStatus](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeegadEGAD-SampleTreatmentStatus.md) | No type description provided<br/>Class with 4 occurences.| 
| [ContaminosoSampleMaterialType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/ContaminosoSampleMaterialType.md) | No type description provided<br/>Class with 0 occurences.| 
| [GeoDggsLiteral](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/GeoDggsLiteral.md) | No type description provided<br/>Class with 0 occurences.| 
| [GeoGeoJSONLiteral](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/GeoGeoJSONLiteral.md) | No type description provided<br/>Class with 0 occurences.| 
| [GeoGmlLiteral](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/GeoGmlLiteral.md) | No type description provided<br/>Class with 0 occurences.| 
| [GeoKmlLiteral](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/GeoKmlLiteral.md) | No type description provided<br/>Class with 0 occurences.| 
| [GeoSpatialObject](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/GeoSpatialObject.md) | No type description provided<br/>Class with 691381 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContaminosoFeature](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/ContaminosoFeature.md) | No type description provided<br/>Class with 568821 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContaminosoPoint](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/ContaminosoPoint.md) | No type description provided<br/>Class with 8480 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContaminosoReleaseFeature](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/ContaminosoReleaseFeature.md) | No type description provided<br/>Class with 8 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContaminosoReleasePoint](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/ContaminosoReleasePoint.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContaminosoSampledFeaure](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/ContaminosoSampledFeaure.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContaminosoSamplePoint](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/ContaminosoSamplePoint.md) | No type description provided<br/>Class with 8480 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeoFeature](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/GeoFeature.md) | No type description provided<br/>Class with 577301 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeoGeometry](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/GeoGeometry.md) | No type description provided<br/>Class with 8389 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[IlisgsISGS-Well](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/IlisgsISGS-Well.md) | No type description provided<br/>Class with 379496 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeegadEGAD-SamplePoint](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeegadEGAD-SamplePoint.md) | No type description provided<br/>Class with 8324 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MemgsMGS-Well](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MemgsMGS-Well.md) | No type description provided<br/>Class with 1000 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UsfrsFRS-Facility](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/UsfrsFRS-Facility.md) | No type description provided<br/>Class with 8 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UssdwisCombinedDistributionSystem](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/UssdwisCombinedDistributionSystem.md) | No type description provided<br/>Class with 52 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UssdwisPublicWaterSystem](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/UssdwisPublicWaterSystem.md) | No type description provided<br/>Class with 33717 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UssdwisPublicWaterSystem-CWS](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/UssdwisPublicWaterSystem-CWS.md) | No type description provided<br/>Class with 3636 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UssdwisPublicWaterSystem-GW](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/UssdwisPublicWaterSystem-GW.md) | No type description provided<br/>Class with 31412 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UssdwisPublicWaterSystem-NTNCWS](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/UssdwisPublicWaterSystem-NTNCWS.md) | No type description provided<br/>Class with 2092 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UssdwisPublicWaterSystem-SW](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/UssdwisPublicWaterSystem-SW.md) | No type description provided<br/>Class with 1891 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UssdwisPublicWaterSystem-TNCWS](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/UssdwisPublicWaterSystem-TNCWS.md) | No type description provided<br/>Class with 27833 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UssdwisPWS-SamplePoint](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/UssdwisPWS-SamplePoint.md) | No type description provided<br/>Class with 156 occurences.| 
| [GeoWktLiteral](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/GeoWktLiteral.md) | No type description provided<br/>Class with 0 occurences.| 
| [HttpQudt.orgVocabUnitUnit](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpQudt.orgVocabUnitUnit.md) | No type description provided<br/>Class with 3 occurences.| 
| [HttpSawgraph.spatialai.orgV1Stad#Quantity](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpSawgraph.spatialai.orgV1Stad#Quantity.md) | No type description provided<br/>Class with 785696 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpSawgraph.spatialai.orgV1Stad#SingleData](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpSawgraph.spatialai.orgV1Stad#SingleData.md) | No type description provided<br/>Class with 757937 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[IlisgsWellDepthInFt](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/IlisgsWellDepthInFt.md) | No type description provided<br/>Class with 376687 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[IlisgsWellYield](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/IlisgsWellYield.md) | No type description provided<br/>Class with 265368 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MemgsWellDepthInFt](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MemgsWellDepthInFt.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MemgsWellOverburdenThicknessInFt](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MemgsWellOverburdenThicknessInFt.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpSawgraph.spatialai.orgV1Stad#StatisticalAggregateData](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpSawgraph.spatialai.orgV1Stad#StatisticalAggregateData.md) | No type description provided<br/>Class with 27759 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpSawgraph.spatialai.orgV1Us-epa-ghg#Amount](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpSawgraph.spatialai.orgV1Us-epa-ghg#Amount.md) | No type description provided<br/>Class with 733 occurences.| 
| [HttpSawgraph.spatialai.orgV1Stad#StatisticalQuantityKind](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpSawgraph.spatialai.orgV1Stad#StatisticalQuantityKind.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContaminosoMaximumConcentration](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/ContaminosoMaximumConcentration.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContaminosoMinimumConcentration](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/ContaminosoMinimumConcentration.md) | No type description provided<br/>Class with 0 occurences.| 
| [HttpStko-kwg.geog.ucsb.eduLodOntologyS2CellLevel13](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpStko-kwg.geog.ucsb.eduLodOntologyS2CellLevel13.md) | No type description provided<br/>Class with 86332 occurences.| 
| [HttpWww.opengis.netOntSf#Point](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpWww.opengis.netOntSf#Point.md) | No type description provided<br/>Class with 5395 occurences.| 
| [HttpsQudt.orgSchemaQudtQuantityValue](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpsQudt.orgSchemaQudtQuantityValue.md) | No type description provided<br/>Class with 283780 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeegadEGAD-MethodDetectionLimit](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeegadEGAD-MethodDetectionLimit.md) | No type description provided<br/>Class with 141607 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeegadEGAD-ReportingLimit](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeegadEGAD-ReportingLimit.md) | No type description provided<br/>Class with 142152 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UssdwisAmount](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/UssdwisAmount.md) | No type description provided<br/>Class with 21 occurences.| 
| [IlisgsWellPurpose](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/IlisgsWellPurpose.md) | No type description provided<br/>Class with 33 occurences.| 
| [MeegadEGAD-SamplePointType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeegadEGAD-SamplePointType.md) | No type description provided<br/>Class with 109 occurences.| 
| [MeegadEGAD-Site](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeegadEGAD-Site.md) | No type description provided<br/>Class with 957 occurences.| 
| [MeegadEGAD-SiteType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeegadEGAD-SiteType.md) | No type description provided<br/>Class with 62 occurences.| 
| [MemgsWellType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MemgsWellType.md) | No type description provided<br/>Class with 0 occurences.| 
| [MemgsWellUse](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MemgsWellUse.md) | No type description provided<br/>Class with 0 occurences.| 
| [OwlNamedIndividual](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OwlNamedIndividual.md) | No type description provided<br/>Class with 1848 occurences.| 
| [ProvOrganization](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/ProvOrganization.md) | No type description provided<br/>Class with 300 occurences.| 
| [RdfList](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/RdfList.md) | No type description provided<br/>Class with 1 occurences.| 
| [SosaFeatureOfInterest](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/SosaFeatureOfInterest.md) | No type description provided<br/>Class with 8196 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContaminosoSampledFeature](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/ContaminosoSampledFeature.md) | No type description provided<br/>Class with 8196 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeegadEGAD-SampledFeature](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeegadEGAD-SampledFeature.md) | No type description provided<br/>Class with 8040 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UssdwisSampledFeature](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/UssdwisSampledFeature.md) | No type description provided<br/>Class with 156 occurences.| 
| [SosaObservableProperty](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/SosaObservableProperty.md) | No type description provided<br/>Class with 169 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContaminosoSubstance](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/ContaminosoSubstance.md) | No type description provided<br/>Class with 169 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpSawgraph.spatialai.orgV1Us-epa-ghg#Chemical](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpSawgraph.spatialai.orgV1Us-epa-ghg#Chemical.md) | No type description provided<br/>Class with 75 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeegadEGAD-PFAS-ParameterName](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeegadEGAD-PFAS-ParameterName.md) | No type description provided<br/>Class with 93 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UssdwisPWS-PFAS](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/UssdwisPWS-PFAS.md) | No type description provided<br/>Class with 1 occurences.| 
| [SosaObservation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/SosaObservation.md) | No type description provided<br/>Class with 143064 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContaminosoContaminantObservation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/ContaminosoContaminantObservation.md) | No type description provided<br/>Class with 143064 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContaminosoReleaseContaminantObservation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/ContaminosoReleaseContaminantObservation.md) | No type description provided<br/>Class with 733 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContaminosoSampleContaminantObservation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/ContaminosoSampleContaminantObservation.md) | No type description provided<br/>Class with 142331 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContaminosoSingleContaminantObservation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/ContaminosoSingleContaminantObservation.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpSawgraph.spatialai.orgV1Us-epa-ghg#ReleaseObservation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpSawgraph.spatialai.orgV1Us-epa-ghg#ReleaseObservation.md) | No type description provided<br/>Class with 733 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeegadEGAD-PFAS-Observation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeegadEGAD-PFAS-Observation.md) | No type description provided<br/>Class with 142175 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PfasPFAS-ContaminantObservation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/PfasPFAS-ContaminantObservation.md) | No type description provided<br/>Class with 142175 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PfasPFAS-ReleaseContaminantObservation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/PfasPFAS-ReleaseContaminantObservation.md) | No type description provided<br/>Class with 733 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PfasPFAS-SampleContaminantObservation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/PfasPFAS-SampleContaminantObservation.md) | No type description provided<br/>Class with 156 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UssdwisPWS-Observation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/UssdwisPWS-Observation.md) | No type description provided<br/>Class with 156 occurences.| 
| [SosaProcedure](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/SosaProcedure.md) | No type description provided<br/>Class with 1249 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeegadEGAD-AnalysisMethod](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeegadEGAD-AnalysisMethod.md) | No type description provided<br/>Class with 1249 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PfasAnalysisMethod](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/PfasAnalysisMethod.md) | No type description provided<br/>Class with 1249 occurences.| 
| [SosaResult](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/SosaResult.md) | No type description provided<br/>Class with 143064 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContaminosoAggregateContaminantMeasurement](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/ContaminosoAggregateContaminantMeasurement.md) | No type description provided<br/>Class with 27026 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContaminosoContaminantConcentrationMeasurement](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/ContaminosoContaminantConcentrationMeasurement.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContaminosoContaminantMeasurement](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/ContaminosoContaminantMeasurement.md) | No type description provided<br/>Class with 143064 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContaminosoContaminantVolumeMeasurement](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/ContaminosoContaminantVolumeMeasurement.md) | No type description provided<br/>Class with 733 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContaminosoSingleContaminantMeasurement](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/ContaminosoSingleContaminantMeasurement.md) | No type description provided<br/>Class with 115882 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpSawgraph.spatialai.orgV1Us-epa-ghg#Measurement](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpSawgraph.spatialai.orgV1Us-epa-ghg#Measurement.md) | No type description provided<br/>Class with 733 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeegadEGAD-AggregatePFAS-Concentration](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeegadEGAD-AggregatePFAS-Concentration.md) | No type description provided<br/>Class with 26293 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeegadEGAD-SinglePFAS-Concentration](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeegadEGAD-SinglePFAS-Concentration.md) | No type description provided<br/>Class with 115882 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PfasAggregatePFASAmountMeasurement](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/PfasAggregatePFASAmountMeasurement.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PfasAggregatePFASConcentrationMeasurement](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/PfasAggregatePFASConcentrationMeasurement.md) | No type description provided<br/>Class with 26293 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PfasPFAS-ConcentrationMeasurement](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/PfasPFAS-ConcentrationMeasurement.md) | No type description provided<br/>Class with 156 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PfasPFAS-VolumeMeasurement](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/PfasPFAS-VolumeMeasurement.md) | No type description provided<br/>Class with 733 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PfasSinglePFASConcentrationMeasurement](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/PfasSinglePFASConcentrationMeasurement.md) | No type description provided<br/>Class with 115882 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UssdwisPWS-PFASConcentration](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/UssdwisPWS-PFASConcentration.md) | No type description provided<br/>Class with 156 occurences.| 
| [SosaSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/SosaSample.md) | No type description provided<br/>Class with 23180 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContaminosoMaterialSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/ContaminosoMaterialSample.md) | No type description provided<br/>Class with 23180 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeegadEGAD-Sample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeegadEGAD-Sample.md) | No type description provided<br/>Class with 23024 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UssdwisPWS-Sample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/UssdwisPWS-Sample.md) | No type description provided<br/>Class with 156 occurences.| 





## Slots

| Slot | Description |
| --- | --- |
| [contaminoso_analysisDate](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/contaminoso_analysisDate.md) | No slot description provided<br/>142853 occurrences with subject type contaminoso_ContaminantObservation and object type date.|
| [contaminoso_analysisMethod](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/contaminoso_analysisMethod.md) | No slot description provided<br/>142429 occurrences with subject type contaminoso_ContaminantObservation and object type meegad_EGAD-AnalysisMethod.|
| [contaminoso_analyzedBy](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/contaminoso_analyzedBy.md) | No slot description provided<br/>142175 occurrences with subject type contaminoso_ContaminantObservation and object type prov_Organization.|
| [contaminoso_analyzedSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/contaminoso_analyzedSample.md) | No slot description provided<br/>142331 occurrences with subject type contaminoso_ContaminantObservation and object type contaminoso_MaterialSample.|
| [contaminoso_casNumber](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/contaminoso_casNumber.md) | No slot description provided<br/>75 occurrences with subject type contaminoso_Substance and object type string.|
| [contaminoso_fromSampledFeature](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/contaminoso_fromSampledFeature.md) | No slot description provided<br/>142261 occurrences with subject type contaminoso_ContaminantObservation and object type contaminoso_Feature.|
| [contaminoso_fromSamplePoint](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/contaminoso_fromSamplePoint.md) | No slot description provided<br/>18128 occurrences with subject type contaminoso_MaterialSample and object type contaminoso_Point.|
| [contaminoso_hasAggregationPeriod](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/contaminoso_hasAggregationPeriod.md) | No slot description provided<br/>733 occurrences with subject type contaminoso_ContaminantObservation and object type uri.|
| [contaminoso_hasFeatureOfInterest](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/contaminoso_hasFeatureOfInterest.md) | No slot description provided<br/>733 occurrences with subject type contaminoso_ContaminantObservation and object type contaminoso_Feature.|
| [contaminoso_hasResult](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/contaminoso_hasResult.md) | No slot description provided<br/>733 occurrences with subject type contaminoso_ContaminantObservation and object type contaminoso_AggregateContaminantMeasurement.|
| [contaminoso_hasTemporalCoverage](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/contaminoso_hasTemporalCoverage.md) | No slot description provided<br/>733 occurrences with subject type contaminoso_ContaminantObservation and object type uri.|
| [contaminoso_mUnit](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/contaminoso_mUnit.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [contaminoso_mValue](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/contaminoso_mValue.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [contaminoso_observationAnnotation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/contaminoso_observationAnnotation.md) | No slot description provided<br/>142175 occurrences with subject type contaminoso_ContaminantObservation and object type contaminoso_ObservationAnnotation.|
| [contaminoso_observedAnalyte](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/contaminoso_observedAnalyte.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [contaminoso_observedAtSamplePoint](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/contaminoso_observedAtSamplePoint.md) | No slot description provided<br/>142261 occurrences with subject type contaminoso_ContaminantObservation and object type contaminoso_Point.|
| [contaminoso_ofSampleMaterialType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/contaminoso_ofSampleMaterialType.md) | No slot description provided<br/>23025 occurrences with subject type contaminoso_MaterialSample and object type contaminoso_MaterialType.|
| [contaminoso_ofSubstance](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/contaminoso_ofSubstance.md) | No slot description provided<br/>143027 occurrences with subject type contaminoso_ContaminantObservation and object type contaminoso_Substance.<br/>37 occurrences with subject type contaminoso_ContaminantObservation and object type uri.|
| [contaminoso_pointFromFeature](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/contaminoso_pointFromFeature.md) | No slot description provided<br/>8040 occurrences with subject type contaminoso_Point and object type contaminoso_Feature.|
| [contaminoso_resultAnnotation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/contaminoso_resultAnnotation.md) | No slot description provided<br/>180161 occurrences with subject type contaminoso_ContaminantMeasurement and object type contaminoso_ResultQualifier.<br/>44340 occurrences with subject type contaminoso_AggregateContaminantMeasurement and object type contaminoso_ResultQualifier.<br/>535 occurrences with subject type contaminoso_ContaminantMeasurement and object type uri.<br/>72 occurrences with subject type contaminoso_AggregateContaminantMeasurement and object type uri.<br/>283759 occurrences with subject type contaminoso_ResultQualifier and object type contaminoso_ResultQualifier.|
| [contaminoso_resultQualifier](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/contaminoso_resultQualifier.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [contaminoso_sampleAnnotation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/contaminoso_sampleAnnotation.md) | No slot description provided<br/>55252 occurrences with subject type contaminoso_MaterialSample and object type contaminoso_SampleAnnotation.<br/>9263 occurrences with subject type contaminoso_MaterialSample and object type uri.|
| [contaminoso_sampledFeature](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/contaminoso_sampledFeature.md) | No slot description provided<br/>156 occurrences with subject type contaminoso_ContaminantObservation and object type contaminoso_Feature.|
| [contaminoso_sampledTime](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/contaminoso_sampledTime.md) | No slot description provided<br/>142175 occurrences with subject type contaminoso_ContaminantObservation and object type date.|
| [contaminoso_sampleTime](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/contaminoso_sampleTime.md) | No slot description provided<br/>156 occurrences with subject type contaminoso_ContaminantObservation and object type date.|
| [contaminoso_substanceID](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/contaminoso_substanceID.md) | No slot description provided<br/>75 occurrences with subject type contaminoso_Substance and object type string.|
| [contaminoso_usedProcedure](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/contaminoso_usedProcedure.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [dct_contributor](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/dct_contributor.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [dct_created](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/dct_created.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [dct_creator](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/dct_creator.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [dct_description](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/dct_description.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [dct_issued](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/dct_issued.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [dct_license](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/dct_license.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [dct_modified](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/dct_modified.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [dct_publisher](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/dct_publisher.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [dct_replaces](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/dct_replaces.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [dct_rights](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/dct_rights.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [dct_source](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/dct_source.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [dct_title](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/dct_title.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [geo_asWKT](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/geo_asWKT.md) | No slot description provided<br/>379496 occurrences with untyped subjects and object type http://www.opengis.net/ont/geosparql#wktLiteral.<br/>5395 occurrences with subject type geo_Geometry and object type geo_wktLiteral.|
| [geo_defaultGeometry](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/geo_defaultGeometry.md) | No slot description provided<br/>999 occurrences with subject type contaminoso_Feature and object type geo_Geometry.|
| [geo_hasDefaultGeometry](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/geo_hasDefaultGeometry.md) | No slot description provided<br/>4511 occurrences with subject type contaminoso_Point and object type geo_Geometry.<br/>884 occurrences with subject type meegad_EGAD-Site and object type geo_Geometry.<br/>999 occurrences with subject type contaminoso_Feature and object type geo_Geometry.|
| [geo_hasGeometry](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/geo_hasGeometry.md) | No slot description provided<br/>4511 occurrences with subject type contaminoso_Point and object type geo_Geometry.<br/>841 occurrences with subject type meegad_EGAD-Site and object type geo_SpatialObject.<br/>884 occurrences with subject type meegad_EGAD-Site and object type geo_Geometry.<br/>2994 occurrences with subject type contaminoso_Feature and object type geo_Geometry.<br/>80056 occurrences with subject type contaminoso_Feature and object type geo_SpatialObject.<br/>379496 occurrences with subject type contaminoso_Feature and object type uri.<br/>24794 occurrences with untyped subjects and object type http://www.opengis.net/ont/geosparql#SpatialObject.|
| [geo_hasSerialization](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/geo_hasSerialization.md) | No slot description provided<br/>379496 occurrences with untyped subjects and object type http://www.opengis.net/ont/geosparql#wktLiteral.<br/>105691 occurrences with subject type geo_SpatialObject and object type geo_wktLiteral.<br/>8389 occurrences with subject type geo_Geometry and object type geo_wktLiteral.|
| [http___proton.semanticweb.org_protonsys#transitiveOver](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___proton.semanticweb.org_protonsys#transitiveOver.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [http___purl.org_vocab_vann_preferredNamespacePrefix](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___purl.org_vocab_vann_preferredNamespacePrefix.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [http___purl.org_vocab_vann_preferredNamespaceUri](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___purl.org_vocab_vann_preferredNamespaceUri.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [http___sawgraph.spatialai.org_v1_me_egad_data#dep_chemicalID](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___sawgraph.spatialai.org_v1_me_egad_data#dep_chemicalID.md) | No slot description provided<br/>4 occurrences with subject type contaminoso_Substance and object type string.<br/>3 occurrences with untyped subjects and object type string.|
| [http___sawgraph.spatialai.org_v1_sdwis#pwsidNumber](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___sawgraph.spatialai.org_v1_sdwis#pwsidNumber.md) | Uniquely identifies the water system within a specific state<br/>61 occurrences with subject type meegad_EGAD-Site and object type string.|
| [http___sawgraph.spatialai.org_v1_us_epa_ghg#casNumber](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___sawgraph.spatialai.org_v1_us_epa_ghg#casNumber.md) | No slot description provided<br/>76 occurrences with subject type contaminoso_Substance and object type string.|
| [http___sawgraph.spatialai.org_v1_us_epa_ghg#chemicalFormula](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___sawgraph.spatialai.org_v1_us_epa_ghg#chemicalFormula.md) | No slot description provided<br/>56 occurrences with subject type contaminoso_Substance and object type string.|
| [http___sawgraph.spatialai.org_v1_us_epa_ghg#GHG_Subpart](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___sawgraph.spatialai.org_v1_us_epa_ghg#GHG_Subpart.md) | No slot description provided<br/>733 occurrences with subject type contaminoso_ContaminantObservation and object type string.|
| [http___stko_kwg.geog.ucsb.edu_lod_ontology_sfContains](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___stko_kwg.geog.ucsb.edu_lod_ontology_sfContains.md) | No slot description provided<br/>166097 occurrences with untyped subjects and object type http://sawgraph.spatialai.org/v1/contaminoso#Feature.<br/>83049 occurrences with subject type http___stko-kwg.geog.ucsb.edu_lod_ontology_S2Cell_Level13 and object type contaminoso_Feature.<br/>4502 occurrences with subject type http___stko-kwg.geog.ucsb.edu_lod_ontology_S2Cell_Level13 and object type contaminoso_Point.<br/>883 occurrences with subject type http___stko-kwg.geog.ucsb.edu_lod_ontology_S2Cell_Level13 and object type meegad_EGAD-Site.<br/>4509 occurrences with untyped subjects and object type http://sawgraph.spatialai.org/v1/contaminoso#Point.<br/>883 occurrences with untyped subjects and object type http://sawgraph.spatialai.org/v1/me-egad#EGAD-Site.|
| [http___stko_kwg.geog.ucsb.edu_lod_ontology_sfOverlaps](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___stko_kwg.geog.ucsb.edu_lod_ontology_sfOverlaps.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [http___stko_kwg.geog.ucsb.edu_lod_ontology_sfTouches](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___stko_kwg.geog.ucsb.edu_lod_ontology_sfTouches.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [http___stko_kwg.geog.ucsb.edu_lod_ontology_sfWithin](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___stko_kwg.geog.ucsb.edu_lod_ontology_sfWithin.md) | No slot description provided<br/>4502 occurrences with subject type contaminoso_Point and object type http___stko-kwg.geog.ucsb.edu_lod_ontology_S2Cell_Level13.<br/>4509 occurrences with subject type contaminoso_Point and object type uri.<br/>883 occurrences with subject type meegad_EGAD-Site and object type http___stko-kwg.geog.ucsb.edu_lod_ontology_S2Cell_Level13.<br/>883 occurrences with subject type meegad_EGAD-Site and object type uri.<br/>166097 occurrences with subject type contaminoso_Feature and object type uri.<br/>83049 occurrences with subject type contaminoso_Feature and object type http___stko-kwg.geog.ucsb.edu_lod_ontology_S2Cell_Level13.|
| [http___stko_kwg.geog.ucsb.edu_lod_ontology_spatialRelation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___stko_kwg.geog.ucsb.edu_lod_ontology_spatialRelation.md) | No slot description provided<br/>4502 occurrences with subject type contaminoso_Point and object type http___stko-kwg.geog.ucsb.edu_lod_ontology_S2Cell_Level13.<br/>4509 occurrences with subject type contaminoso_Point and object type uri.<br/>883 occurrences with subject type meegad_EGAD-Site and object type http___stko-kwg.geog.ucsb.edu_lod_ontology_S2Cell_Level13.<br/>883 occurrences with subject type meegad_EGAD-Site and object type uri.<br/>166097 occurrences with subject type contaminoso_Feature and object type uri.<br/>83049 occurrences with subject type contaminoso_Feature and object type http___stko-kwg.geog.ucsb.edu_lod_ontology_S2Cell_Level13.<br/>166097 occurrences with untyped subjects and object type http://sawgraph.spatialai.org/v1/contaminoso#Feature.<br/>83049 occurrences with subject type http___stko-kwg.geog.ucsb.edu_lod_ontology_S2Cell_Level13 and object type contaminoso_Feature.<br/>4502 occurrences with subject type http___stko-kwg.geog.ucsb.edu_lod_ontology_S2Cell_Level13 and object type contaminoso_Point.<br/>883 occurrences with subject type http___stko-kwg.geog.ucsb.edu_lod_ontology_S2Cell_Level13 and object type meegad_EGAD-Site.<br/>4509 occurrences with untyped subjects and object type http://sawgraph.spatialai.org/v1/contaminoso#Point.<br/>883 occurrences with untyped subjects and object type http://sawgraph.spatialai.org/v1/me-egad#EGAD-Site.|
| [http___www.w3.org_2008_05_skos#definition](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___www.w3.org_2008_05_skos#definition.md) | No slot description provided<br/>62 occurrences with subject type meegad_EGAD-SiteType and object type string.|
| [https___qudt.org_schema_qudt_numericValue](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/https___qudt.org_schema_qudt_numericValue.md) | No slot description provided<br/>376687 occurrences with subject type ilisgs_WellDepthInFt and object type float.<br/>265368 occurrences with subject type ilisgs_WellYield and object type float.<br/>733 occurrences with subject type http___sawgraph.spatialai.org_v1_stad#Quantity and object type float.<br/>22 occurrences with subject type ussdwis_Amount and object type float.|
| [https___qudt.org_schema_qudt_quantityKind](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/https___qudt.org_schema_qudt_quantityKind.md) | No slot description provided<br/>733 occurrences with subject type contaminoso_AggregateContaminantMeasurement and object type http___sawgraph.spatialai.org_v1_stad#Quantity.|
| [https___qudt.org_schema_qudt_quantityValue](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/https___qudt.org_schema_qudt_quantityValue.md) | No slot description provided<br/>21 occurrences with subject type contaminoso_ContaminantMeasurement and object type ussdwis_Amount.|
| [https___qudt.org_schema_qudt_unit](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/https___qudt.org_schema_qudt_unit.md) | No slot description provided<br/>265368 occurrences with subject type ilisgs_WellYield and object type uri.<br/>733 occurrences with subject type http___sawgraph.spatialai.org_v1_stad#Quantity and object type uri.<br/>21 occurrences with subject type ussdwis_Amount and object type uri.|
| [ilisgs_hasISWSId](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/ilisgs_hasISWSId.md) | No slot description provided<br/>152051 occurrences with subject type contaminoso_Feature and object type string.|
| [ilisgs_hasOwner](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/ilisgs_hasOwner.md) | No slot description provided<br/>377323 occurrences with subject type contaminoso_Feature and object type string.|
| [ilisgs_wellDepth](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/ilisgs_wellDepth.md) | No slot description provided<br/>376687 occurrences with subject type contaminoso_Feature and object type ilisgs_WellDepthInFt.|
| [ilisgs_wellPurpose](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/ilisgs_wellPurpose.md) | No slot description provided<br/>379496 occurrences with subject type contaminoso_Feature and object type ilisgs_WellPurpose.|
| [ilisgs_wellYield](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/ilisgs_wellYield.md) | No slot description provided<br/>265368 occurrences with subject type contaminoso_Feature and object type ilisgs_WellYield.|
| [meegad_analyzedSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/meegad_analyzedSample.md) | No slot description provided<br/>142175 occurrences with subject type contaminoso_ContaminantObservation and object type contaminoso_MaterialSample.|
| [meegad_associatedSite](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/meegad_associatedSite.md) | No slot description provided<br/>8405 occurrences with subject type contaminoso_Point and object type meegad_EGAD-Site.|
| [meegad_dep_chemicalID](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/meegad_dep_chemicalID.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [meegad_labQualifier](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/meegad_labQualifier.md) | No slot description provided<br/>40705 occurrences with subject type contaminoso_ContaminantMeasurement and object type contaminoso_ResultQualifier.<br/>13237 occurrences with subject type contaminoso_AggregateContaminantMeasurement and object type contaminoso_ResultQualifier.|
| [meegad_methodDetectionLimit](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/meegad_methodDetectionLimit.md) | No slot description provided<br/>141607 occurrences with subject type contaminoso_ResultQualifier and object type contaminoso_ResultQualifier.|
| [meegad_parameterAbbreviation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/meegad_parameterAbbreviation.md) | Abbreviation of the PFAS parameter (single chemical or aggregate set of chemi...<br/>93 occurrences with subject type contaminoso_Substance and object type string.|
| [meegad_parameterGroup](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/meegad_parameterGroup.md) | No slot description provided<br/>56 occurrences with subject type contaminoso_ResultQualifier and object type string.|
| [meegad_parameterName](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/meegad_parameterName.md) | Name of the PFAS parameter (single chemical or aggregate set of chemicals) me...<br/>93 occurrences with subject type contaminoso_Substance and object type string.|
| [meegad_reportingLimit](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/meegad_reportingLimit.md) | No slot description provided<br/>142152 occurrences with subject type contaminoso_ResultQualifier and object type contaminoso_ResultQualifier.|
| [meegad_resultType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/meegad_resultType.md) | No slot description provided<br/>142175 occurrences with subject type contaminoso_ContaminantObservation and object type contaminoso_ObservationAnnotation.|
| [meegad_sampleCollectionLocation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/meegad_sampleCollectionLocation.md) | No slot description provided<br/>7354 occurrences with subject type contaminoso_MaterialSample and object type uri.<br/>15692 occurrences with subject type contaminoso_MaterialSample and object type contaminoso_SampleAnnotation.|
| [meegad_sampleCollectionMethod](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/meegad_sampleCollectionMethod.md) | No slot description provided<br/>22824 occurrences with subject type contaminoso_MaterialSample and object type contaminoso_SampleAnnotation.<br/>216 occurrences with subject type contaminoso_MaterialSample and object type uri.|
| [meegad_sampledFeatureType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/meegad_sampledFeatureType.md) | No slot description provided<br/>8040 occurrences with subject type contaminoso_Feature and object type meegad_EGAD-SamplePointType.|
| [meegad_sampleID](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/meegad_sampleID.md) | Sample identifier in the EGAD dataset from the state of Maine<br/>23031 occurrences with subject type contaminoso_MaterialSample and object type string.|
| [meegad_samplePointNumber](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/meegad_samplePointNumber.md) | Sample point number in the EGAD dataset from the state of Maine<br/>8040 occurrences with subject type contaminoso_Point and object type integer.|
| [meegad_samplePointType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/meegad_samplePointType.md) | No slot description provided<br/>8324 occurrences with subject type contaminoso_Point and object type meegad_EGAD-SamplePointType.|
| [meegad_samplePointWebName](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/meegad_samplePointWebName.md) | Sample point web name in the EGAD dataset from the state of Maine<br/>8040 occurrences with subject type contaminoso_Point and object type string.|
| [meegad_sampleTreatmentStatus](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/meegad_sampleTreatmentStatus.md) | No slot description provided<br/>1693 occurrences with subject type contaminoso_MaterialSample and object type uri.<br/>16736 occurrences with subject type contaminoso_MaterialSample and object type contaminoso_SampleAnnotation.|
| [meegad_siteName](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/meegad_siteName.md) | Site name in the EGAD dataset from the state of Maine<br/>957 occurrences with subject type meegad_EGAD-Site and object type string.|
| [meegad_siteNumber](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/meegad_siteNumber.md) | Site number in the EGAD dataset from the state of Maine<br/>957 occurrences with subject type meegad_EGAD-Site and object type integer.|
| [meegad_siteType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/meegad_siteType.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [meegad_validationLevel](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/meegad_validationLevel.md) | No slot description provided<br/>113547 occurrences with subject type contaminoso_ContaminantMeasurement and object type contaminoso_ResultQualifier.<br/>26147 occurrences with subject type contaminoso_AggregateContaminantMeasurement and object type contaminoso_ResultQualifier.<br/>490 occurrences with subject type contaminoso_ContaminantMeasurement and object type uri.<br/>64 occurrences with subject type contaminoso_AggregateContaminantMeasurement and object type uri.|
| [meegad_validationQualifier](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/meegad_validationQualifier.md) | No slot description provided<br/>60592 occurrences with subject type contaminoso_ContaminantMeasurement and object type contaminoso_ResultQualifier.<br/>17314 occurrences with subject type contaminoso_AggregateContaminantMeasurement and object type contaminoso_ResultQualifier.<br/>45 occurrences with subject type contaminoso_ContaminantMeasurement and object type uri.<br/>8 occurrences with subject type contaminoso_AggregateContaminantMeasurement and object type uri.|
| [memgs_hasUse](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/memgs_hasUse.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [memgs_ofWellType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/memgs_ofWellType.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [memgs_wellDepth](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/memgs_wellDepth.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [memgs_wellOverburden](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/memgs_wellOverburden.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [owl_allValuesFrom](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/owl_allValuesFrom.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [owl_differentFrom](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/owl_differentFrom.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [owl_disjointWith](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/owl_disjointWith.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [owl_equivalentClass](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/owl_equivalentClass.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [owl_equivalentProperty](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/owl_equivalentProperty.md) | No slot description provided<br/>36 occurrences with untyped subjects and object type uri.|
| [owl_imports](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/owl_imports.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [owl_inverseOf](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/owl_inverseOf.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [owl_onProperty](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/owl_onProperty.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [owl_propertyDisjointWith](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/owl_propertyDisjointWith.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [owl_subPropertyOf](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/owl_subPropertyOf.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [owl_topObjectProperty](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/owl_topObjectProperty.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [owl_versionInfo](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/owl_versionInfo.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [owl_versionIRI](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/owl_versionIRI.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [qudt_numericValue](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/qudt_numericValue.md) | No slot description provided<br/>142927 occurrences with untyped subjects and object type decimal.<br/>127 occurrences with untyped subjects and object type http://www.w3.org/2001/XMLSchema#double.<br/>280289 occurrences with subject type contaminoso_ResultQualifier and object type decimal.<br/>570 occurrences with subject type contaminoso_ResultQualifier and object type double.|
| [qudt_quantityValue](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/qudt_quantityValue.md) | No slot description provided<br/>115882 occurrences with subject type contaminoso_ContaminantMeasurement and object type uri.<br/>26293 occurrences with subject type contaminoso_AggregateContaminantMeasurement and object type uri.|
| [qudt_unit](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/qudt_unit.md) | No slot description provided<br/>29743 occurrences with untyped subjects and object type http://qudt.org/vocab/unitUnit.<br/>112812 occurrences with untyped subjects and object type uri.|
| [rdf__1](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/rdf__1.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [rdf_first](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/rdf_first.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [rdf_object](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/rdf_object.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [rdf_predicate](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/rdf_predicate.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [rdf_rest](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/rdf_rest.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [rdf_subject](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/rdf_subject.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [rdf_value](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/rdf_value.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [rdfs_comment](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/rdfs_comment.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [rdfs_domain](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/rdfs_domain.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [rdfs_isDefinedBy](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/rdfs_isDefinedBy.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [rdfs_label](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/rdfs_label.md) | No slot description provided<br/>66 occurrences with subject type contaminoso_ResultQualifier and object type string.<br/>33 occurrences with subject type ilisgs_WellPurpose and object type string.<br/>109 occurrences with subject type meegad_EGAD-SamplePointType and object type string.<br/>94 occurrences with subject type contaminoso_Substance and object type string.<br/>12 occurrences with subject type contaminoso_ObservationAnnotation and object type string.<br/>160 occurrences with subject type contaminoso_SampleAnnotation and object type string.<br/>97 occurrences with subject type contaminoso_MaterialType and object type string.<br/>1249 occurrences with subject type meegad_EGAD-AnalysisMethod and object type string.<br/>3 occurrences with subject type http___qudt.org_vocab_unitUnit and object type string.<br/>300 occurrences with subject type prov_Organization and object type string.<br/>115887 occurrences with subject type contaminoso_ContaminantMeasurement and object type string.<br/>26294 occurrences with subject type contaminoso_AggregateContaminantMeasurement and object type string.<br/>23031 occurrences with subject type contaminoso_MaterialSample and object type string.<br/>8324 occurrences with subject type contaminoso_Point and object type string.<br/>171069 occurrences with subject type contaminoso_Feature and object type string.<br/>957 occurrences with subject type meegad_EGAD-Site and object type string.<br/>62 occurrences with subject type meegad_EGAD-SiteType and object type string.<br/>142181 occurrences with subject type contaminoso_ContaminantObservation and object type string.|
| [rdfs_range](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/rdfs_range.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [rdfs_seeAlso](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/rdfs_seeAlso.md) | No slot description provided<br/>136 occurrences with untyped subjects and object type uri.|
| [schema_affiliation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/schema_affiliation.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [schema_email](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/schema_email.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [schema_name](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/schema_name.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [schema_url](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/schema_url.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [skos_definition](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/skos_definition.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [skos_example](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/skos_example.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [skos_note](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/skos_note.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [skos_prefLabel](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/skos_prefLabel.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [skos_scopeNote](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/skos_scopeNote.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [sosa_hasFeatureOfInterest](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/sosa_hasFeatureOfInterest.md) | No slot description provided<br/>156 occurrences with subject type contaminoso_ContaminantObservation and object type contaminoso_Feature.|
| [sosa_hasResult](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/sosa_hasResult.md) | No slot description provided<br/>116038 occurrences with subject type contaminoso_ContaminantObservation and object type contaminoso_ContaminantMeasurement.<br/>26293 occurrences with subject type contaminoso_ContaminantObservation and object type contaminoso_AggregateContaminantMeasurement.|
| [sosa_isSampleOf](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/sosa_isSampleOf.md) | No slot description provided<br/>No occurrences of this slot in the graph.|
| [sosa_observedProperty](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/sosa_observedProperty.md) | No slot description provided<br/>143027 occurrences with subject type contaminoso_ContaminantObservation and object type contaminoso_Substance.<br/>37 occurrences with subject type contaminoso_ContaminantObservation and object type uri.|
| [sosa_resultTime](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/sosa_resultTime.md) | No slot description provided<br/>142853 occurrences with subject type contaminoso_ContaminantObservation and object type date.|
| [usfrs_hasGHGId](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/usfrs_hasGHGId.md) | No slot description provided<br/>8 occurrences with subject type contaminoso_Feature and object type string.|
| [ussdwis_deactivationDate](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/ussdwis_deactivationDate.md) | No slot description provided<br/>26536 occurrences with subject type contaminoso_Feature and object type date.|
| [ussdwis_firstReport](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/ussdwis_firstReport.md) | No slot description provided<br/>33561 occurrences with subject type contaminoso_Feature and object type date.|
| [ussdwis_hasActivity](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/ussdwis_hasActivity.md) | No slot description provided<br/>33561 occurrences with subject type contaminoso_Feature and object type string.|
| [ussdwis_hasName](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/ussdwis_hasName.md) | No slot description provided<br/>156 occurrences with subject type contaminoso_Feature and object type string.|
| [ussdwis_hasOwnership](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/ussdwis_hasOwnership.md) | No slot description provided<br/>19616 occurrences with subject type contaminoso_Feature and object type string.|
| [ussdwis_hasPWSID](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/ussdwis_hasPWSID.md) | No slot description provided<br/>156 occurrences with subject type contaminoso_Feature and object type string.|
| [ussdwis_inCombinedSystem](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/ussdwis_inCombinedSystem.md) | No slot description provided<br/>590 occurrences with subject type contaminoso_Feature and object type contaminoso_Feature.|
| [ussdwis_lastReport](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/ussdwis_lastReport.md) | No slot description provided<br/>33530 occurrences with subject type contaminoso_Feature and object type date.|
| [ussdwis_populationServed](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/ussdwis_populationServed.md) | No slot description provided<br/>33717 occurrences with subject type contaminoso_Feature and object type integer.|
| [ussdwis_primarySource](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/ussdwis_primarySource.md) | No slot description provided<br/>33303 occurrences with subject type contaminoso_Feature and object type string.|
| [ussdwis_pwsName](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/ussdwis_pwsName.md) | No slot description provided<br/>33394 occurrences with subject type contaminoso_Feature and object type string.|
| [ussdwis_sampleID](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/ussdwis_sampleID.md) | No slot description provided<br/>156 occurrences with subject type contaminoso_MaterialSample and object type string.|
| [ussdwis_SamplePointID](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/ussdwis_SamplePointID.md) | No slot description provided<br/>156 occurrences with subject type contaminoso_Point and object type string.|
| [ussdwis_serviceConnections](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/ussdwis_serviceConnections.md) | No slot description provided<br/>33561 occurrences with subject type contaminoso_Feature and object type integer.|
| [ussdwis_sizeCategory](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/ussdwis_sizeCategory.md) | No slot description provided<br/>156 occurrences with subject type contaminoso_Feature and object type string.|







