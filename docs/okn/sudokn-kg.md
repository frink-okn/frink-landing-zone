# SUDOKN
Supply and Demand Open Knowledge Network 

SUDOKN Ontology is developed at the Semantic Computing Lab ast ASU. SUDOKN provides the necessary semantics for describing the capabilities of manufacturing companies. SUDOKN used BFO as the top-level ontology and IOF Core and IOF Supply Chain as the mid-level ontologies

## Schema Diagram

```mermaid
erDiagram
IoGroupOfPersons {

}
IoIdentifier {

}
IoInformationContentEntity {

}
IoManufacturer {
    uri sudokn_manufactures  
    uri sudokn_hasCertificate  
    uri sudokn_hasProcessCapability  
    string sudokn_hasOrganizationYearOfEstablishment  
    uri sudokn_hasPostalAddress  
    integer sudokn_hasNumberOfEmployees  
    uri sudokn_hasNumberOfEmployees  
    string rdfs_label  
    uri sudokn_hasOwnershipStatusClassifier  
    uri sudokn_hasMaterialCapability  
    uri sudokn_suppliesToIndustry  
}
IoMaterialProduct {
    string rdfs_label  
}
IoPhysicalLocationIdentifier {

}
IoscIndustry {

}
IoscProductionCapability {

}
OboBFO0000019 {

}
OboBFO0000029 {

}
OwlNamedIndividual {
    uri sudokn_hasCertificate  
    uri sudokn_hasProcessCapability  
    uri sudokn_hasPostalAddress  
    uri sudokn_hasWebAddress  
    uri sudokn_hasOwnershipStatusClassifier  
    uri sudokn_hasMaterialCapability  
    uri sudokn_hasManagementCapability  
    uri sudokn_suppliesToIndustry  
    uri sudokn_hasNAICSClassifier  
    uri sudokn_hasEmailAddress  
}
Sudokn2-AxisCNCTurningCapability {
    string rdfs_label  
}
Sudokn3DPrintingCapability {
    string rdfs_label  
}
SudoknAS9000Certificate {
    string rdfs_label  
}
SudoknAS9003Certificate {

}
SudoknAS9100 {
    string rdfs_label  
}
SudoknAS9100Certificate {
    uri sudokn_attestsTo  
    string rdfs_label  
}
SudoknAS9102Certificate {
    string rdfs_label  
}
SudoknASCertificate {

}
SudoknASME {
    string rdfs_label  
}
SudoknASMECertificate {
    string rdfs_label  
}
SudoknAWSWelderCertificate {
    string rdfs_label  
}
SudoknAbrasiveCleaningCapability {
    string rdfs_label  
}
SudoknAbrassiveMachiningCapability {
    string rdfs_label  
}
SudoknAccommodationAndFoodServices {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknAcetalProcessingCapability {
    string rdfs_label  
}
SudoknAcrylicFabricationCapability {
    string rdfs_label  
}
SudoknAdditiveManufacturingCapability {
    string rdfs_label  
}
SudoknAddtiveManufacturingCapability {
    string rdfs_label  
}
SudoknAdministrativeAndSupportAndWasteServices {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknAerospaceIndustry {
    string rdfs_label  
}
SudoknAgricultureForestryFishingAndHunting {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknAgricultureIndustry {
    string rdfs_label  
}
SudoknAlloySteelProcessingCapability {
    string rdfs_label  
}
SudoknAluminumProcessingCapability {
    string rdfs_label  
}
SudoknAnnealingCapability {
    string rdfs_label  
}
SudoknAnodizingCapability {
    string rdfs_label  
}
SudoknApparelIndustry {
    string rdfs_label  
}
SudoknArtsEnterntainmentAndRecreation {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknAssemblyCapability {
    string rdfs_label  
}
SudoknAssemblyCapibility {

}
SudoknAtomicHydrogenWeldingCapability {
    string rdfs_label  
}
SudoknAutomotiveIndustry {
    string rdfs_label  
}
SudoknBABACertificate {
    string rdfs_label  
}
SudoknBeltSandingCapability {
    string rdfs_label  
}
SudoknBendingCapability {
    string rdfs_label  
}
SudoknBerylliumProcessingCapability {
    string rdfs_label  
}
SudoknBeverageIndustry {
    string rdfs_label  
}
SudoknBlackOxideCoatingCapability {
    string rdfs_label  
}
SudoknBoringCapability {
    string rdfs_label  
}
SudoknBrandName {

}
SudoknBrassBlackeningCapability {
    string rdfs_label  
}
SudoknBrassProcessingCapability {
    string rdfs_label  
}
SudoknBrazeWeldingCapability {
    string rdfs_label  
}
SudoknBrazingCapability {
    string rdfs_label  
}
SudoknBritishRetailConsortiumAccreditation {
    string rdfs_label  
}
SudoknBritishRetailConsortiumCertificate {

}
SudoknBroachingCapability {
    string rdfs_label  
}
SudoknBronzeProcessingCapability {
    string rdfs_label  
}
SudoknBuildingNumber {

}
SudoknBusinessEquipmentIndustry {
    string rdfs_label  
}
SudoknButtWeldingCapability {
    string rdfs_label  
}
SudoknCADCAMCapability {

}
SudoknCADCapability {
    string rdfs_label  
}
SudoknCAECapability {

}
SudoknCNCBendingCapability {
    string rdfs_label  
}
SudoknCNCClyndricalGrindingCapability {
    string rdfs_label  
}
SudoknCNCCuttingCapability {
    string rdfs_label  
}
SudoknCNCCylindricalGrindingCapability {
    string rdfs_label  
}
SudoknCNCFormingCapability {
    string rdfs_label  
}
SudoknCNCGrindingCapability {
    string rdfs_label  
}
SudoknCNCHorizontalTurningCapability {
    string rdfs_label  
}
SudoknCNCLaserCuttingCapability {
    string rdfs_label  
}
SudoknCNCLatheCapability {
    string rdfs_label  
}
SudoknCNCMachiningCapability {
    string rdfs_label  
}
SudoknCNCMillingCapability {
    string rdfs_label  
}
SudoknCNCPlasmaCuttingCapability {
    string rdfs_label  
}
SudoknCNCPressBrakeCapability {
    string rdfs_label  
}
SudoknCNCTurningCapability {
    string rdfs_label  
}
SudoknCNCVerticalMillingCapability {
    string rdfs_label  
}
SudoknCNCWireBendingCapability {
    string rdfs_label  
}
SudoknCNCmillingCapability {
    string rdfs_label  
}
SudoknCarbideProcessingCapability {
    string rdfs_label  
}
SudoknCarbonArcBrazingCapability {
    string rdfs_label  
}
SudoknCarbonArcWeldingCapability {
    string rdfs_label  
}
SudoknCarbonGraphiteProcessingCapability {
    string rdfs_label  
}
SudoknCarbonProcessingCapability {

}
SudoknCarbonitridingCapability {
    string rdfs_label  
}
SudoknCarburizingCapability {
    string rdfs_label  
}
SudoknCastingCapability {
    string rdfs_label  
}
SudoknCenterlessGrindingCapability {
    string rdfs_label  
}
SudoknCentrifugalCastingCapability {
    string rdfs_label  
}
SudoknCerakoteCoatingCapability {
    string rdfs_label  
}
SudoknCeramicMoldCastingCapability {
    string rdfs_label  
}
SudoknCeramicProcessingCapability {
    string rdfs_label  
}
SudoknCertificate {

}
SudoknChemicalAndPetrochemicalIndustry {
    string rdfs_label  
}
SudoknChemicalCleaningCapability {
    string rdfs_label  
}
SudoknChemicalCoatingCapability {
    string rdfs_label  
}
SudoknChemicalProcessingCapability {
    string rdfs_label  
}
SudoknChemicalsProcessingCapability {
    string rdfs_label  
}
SudoknChromateConversionCoatingCapability {
    string rdfs_label  
}
SudoknChromiumProcessingCapability {
    string rdfs_label  
}
SudoknCity {
    string rdfs_label  
}
SudoknCityOfAddress {

}
SudoknClassifier {

}
SudoknClyndricalGrindingCapability {
    string rdfs_label  
}
SudoknCoatingCapability {
    string rdfs_label  
}
SudoknCobaltProcessingCapability {
    string rdfs_label  
}
SudoknColdRolledSteelProcessingCapability {
    string rdfs_label  
}
SudoknCombustableGasWeldingCapability {
    string rdfs_label  
}
SudoknCommunicationAndElectronicPowerUtilitiesIndustry {
    string rdfs_label  
}
SudoknCommunicationIndustry {
    string rdfs_label  
}
SudoknCommunicationandElectronicPowerUtilitiesIndustry {
    string rdfs_label  
}
SudoknCommunicationsIndustry {

}
SudoknCompositeProcessingCapability {
    string rdfs_label  
}
SudoknComputerIndustry {
    string rdfs_label  
}
SudoknComputersandElectronicProductsIndustry {
    string rdfs_label  
}
SudoknConstruction {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknConstructionIndustry {
    string rdfs_label  
}
SudoknConsumerGoods {
    string rdfs_label  
}
SudoknConsumerGoodsIndustry {
    string rdfs_label  
}
SudoknContinuousCastingCapability {
    string rdfs_label  
}
SudoknCopperProcessingCapability {
    string rdfs_label  
}
SudoknCounterBoringCapability {
    string rdfs_label  
}
SudoknCounterSinkingCapability {
    string rdfs_label  
}
SudoknCountry {

}
SudoknCountryOfAddress {

}
SudoknCounty {

}
SudoknCreepFeedGrindingCapability {
    string rdfs_label  
}
SudoknCrochetCapability {

}
SudoknCustomFoamCuttingCapability {
    string rdfs_label  
}
SudoknCuttingCapability {
    string rdfs_label  
}
SudoknCylindricalGrindingCapability {
    string rdfs_label  
}
SudoknDeburringCapability {
    string rdfs_label  
}
SudoknDeepFreezingCapability {
    string rdfs_label  
}
SudoknDeepHoleDrillingCapability {
    string rdfs_label  
}
SudoknDelrinProcessingCapability {
    string rdfs_label  
}
SudoknDesignativeName {

}
SudoknDieCastingCapability {
    string rdfs_label  
}
SudoknDieDesignCapability {

}
SudoknDieMakingCapability {
    string rdfs_label  
}
SudoknDifficultToMachineMaterialsProcessingCapability {
    string rdfs_label  
}
SudoknDiffusionBondingCapability {
    string rdfs_label  
}
SudoknDiffusionHardeningCapability {
    string rdfs_label  
}
SudoknDigitalPrintingCapability {
    string rdfs_label  
}
SudoknDipBrazingCapability {
    string rdfs_label  
}
SudoknDrawingCapability {
    string rdfs_label  
}
SudoknDrillingCapability {
    string rdfs_label  
}
SudoknDyeingCapability {

}
SudoknEDMCapability {
    string rdfs_label  
}
SudoknEducationIndustry {
    string rdfs_label  
}
SudoknEducationalInstitutionsIndustry {
    string rdfs_label  
}
SudoknEducationalServices {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknElectolessNickelPlatingCapability {
    string rdfs_label  
}
SudoknElectricArcWeldingCapability {
    string rdfs_label  
}
SudoknElectricAutomotiveIndustry {
    string rdfs_label  
}
SudoknElectricVehiclesIndustry {
    string rdfs_label  
}
SudoknElectricalDischargeMachiningCapability {
    string rdfs_label  
}
SudoknElectricalResistanceWeldingCapability {
    string rdfs_label  
}
SudoknElectroPlatingCapability {
    string rdfs_label  
}
SudoknElectroSlagWeldingCapability {
    string rdfs_label  
}
SudoknElectrolessNickelPlating {
    string rdfs_label  
}
SudoknElectrolessNickelPlatingCapability {
    string rdfs_label  
}
SudoknElectrolessPlatingCapability {
    string rdfs_label  
}
SudoknElectronBeamWeldingCapability {
    string rdfs_label  
}
SudoknElectronicAutomotiveInudstry {
    string rdfs_label  
}
SudoknElectronicProcessingCapability {

}
SudoknElectronicProductIndustry {
    string rdfs_label  
}
SudoknElectroplatingCapability {
    string rdfs_label  
}
SudoknElectropolishingCapability {
    string rdfs_label  
}
SudoknEmailAddress {

}
SudoknEmbossingCapability {
    string rdfs_label  
}
SudoknEndFormingCapability {
    string rdfs_label  
}
SudoknEndMillingCapability {
    string rdfs_label  
}
SudoknEngineeringCapability {

}
SudoknEngineeringDesignCapability {
    string rdfs_label  
}
SudoknEtchingCapability {
    string rdfs_label  
}
SudoknExoticMaterialProcessingCapability {
    string rdfs_label  
}
SudoknExplosiveWeldingCapability {
    string rdfs_label  
}
SudoknExtremelyHardMaterialProcessingCapability {
    string rdfs_label  
}
SudoknExtrudingCapability {
    string rdfs_label  
}
SudoknExtrusionCapability {
    string rdfs_label  
}
SudoknFDA-GMPCertificate {
    string rdfs_label  
}
SudoknFDA-PMACertificate {
    string rdfs_label  
}
SudoknFDACertificate {
    string rdfs_label  
}
SudoknFDAGMPCompliant {
    string rdfs_label  
}
SudoknFabricatingCapability {
    string rdfs_label  
}
SudoknFabricationCapability {
    string rdfs_label  
}
SudoknFaceMillingCapability {
    string rdfs_label  
}
SudoknFasteningCapability {
    string rdfs_label  
}
SudoknFiberOpticLaserCuttingCapability {
    string rdfs_label  
}
SudoknFiberProcessingCapability {

}
SudoknFillingCapability {
    string rdfs_label  
}
SudoknFinanceAndInsurance {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknFinishingCapability {
    string rdfs_label  
}
SudoknFixtureDesignCapability {
    string rdfs_label  
}
SudoknFixturingCapability {
    string rdfs_label  
}
SudoknFlameSprayingCapability {
    string rdfs_label  
}
SudoknFoamProcessingCapability {
    string rdfs_label  
}
SudoknFoodIndustry {
    string rdfs_label  
}
SudoknForgingCapability {
    string rdfs_label  
}
SudoknFormingCapability {
    string rdfs_label  
}
SudoknFrictionWeldingCapability {
    string rdfs_label  
}
SudoknFurnaceBrazingCapability {
    string rdfs_label  
}
SudoknFurnitureIndustry {
    string rdfs_label  
}
SudoknGWOCertificate {

}
SudoknGalvanizingCapability {
    string rdfs_label  
}
SudoknGasBrazingCapability {
    string rdfs_label  
}
SudoknGasMetalArcWeldingCapability {
    string rdfs_label  
}
SudoknGasTungstenArcWeldingCapability {
    string rdfs_label  
}
SudoknGasWeldingCapability {
    string rdfs_label  
}
SudoknGearCuttingCapability {
    string rdfs_label  
}
SudoknGearHobbingCapability {
    string rdfs_label  
}
SudoknGeopoliticalSite {

}
SudoknGeospatialLocation {
    uri sudokn_hasPostalAddress  
}
SudoknGlassProcessingCapability {
    string rdfs_label  
}
SudoknGoldProcessingCapability {
    string rdfs_label  
}
SudoknGovermentIndustry {
    string rdfs_label  
}
SudoknGovernmentIndustry {
    string rdfs_label  
}
SudoknGraphiteProcessingCapability {
    string rdfs_label  
}
SudoknGrindingCapability {
    string rdfs_label  
}
SudoknHAACPCertificate {
    string rdfs_label  
}
SudoknHardeningCapability {
    string rdfs_label  
}
SudoknHarperizingCapability {
    string rdfs_label  
}
SudoknHastelloyProcessingCapability {
    string rdfs_label  
}
SudoknHealthCareServicesIndustry {
    string rdfs_label  
}
SudoknHealthcareAndSocialAssistance {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknHealthcareServices {

}
SudoknHealthcareServicesIndustry {
    string rdfs_label  
}
SudoknHeatTreatingCapability {
    string rdfs_label  
}
SudoknHighEnergyBeamMachiningCapability {

}
SudoknHighEnergyBeamWeldingCapability {
    string rdfs_label  
}
SudoknHighGradeAluminumProcessingCapability {
    string rdfs_label  
}
SudoknHoleDrillingEDMCapability {
    string rdfs_label  
}
SudoknHoleMakingCapability {
    string rdfs_label  
}
SudoknHoningCapability {
    string rdfs_label  
}
SudoknHorizontalMillingCapability {
    string rdfs_label  
}
SudoknHotDipGalvanizingCapability {
    string rdfs_label  
}
SudoknIATF16949Certificate {
    string rdfs_label  
}
SudoknIS-TS16949 {
    string rdfs_label  
}
SudoknISO13485 {
    string rdfs_label  
}
SudoknISO13485Certificate {
    string rdfs_label  
}
SudoknISO14000Certificate {
    string rdfs_label  
}
SudoknISO14001 {
    string rdfs_label  
}
SudoknISO14001Certificate {
    string rdfs_label  
}
SudoknISO17265Certificate {
    string rdfs_label  
}
SudoknISO27001Certificate {
    string rdfs_label  
}
SudoknISO9000 {
    string rdfs_label  
}
SudoknISO9000Certificate {
    uri sudokn_attestsTo  
    string rdfs_label  
}
SudoknISO9001 {
    string rdfs_label  
}
SudoknISO9001Certificate {
    string rdfs_label  
}
SudoknISOCertificate {
    string rdfs_label  
}
SudoknISTS-16949Certificate {

}
SudoknISTS16949Certificate {
    string rdfs_label  
}
SudoknISTSCertificate {

}
SudoknITARCertificate {
    string rdfs_label  
}
SudoknITARCompliant {
    string rdfs_label  
}
SudoknInconelProcessingCapability {
    string rdfs_label  
}
SudoknInductionBrazingCapability {
    string rdfs_label  
}
SudoknInductionHeatingCapability {
    string rdfs_label  
}
SudoknIndustrialMachineryandEquipmentIndustry {
    string rdfs_label  
}
SudoknIndustry {
    string rdfs_label  
}
SudoknInformation {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknInfraredBrazingCapability {
    string rdfs_label  
}
SudoknInjectionMoldingCapability {
    string rdfs_label  
}
SudoknInstallationCapability {
    string rdfs_label  
}
SudoknInvarProcessingCapability {
    string rdfs_label  
}
SudoknInvestmentCastingCapability {
    string rdfs_label  
}
SudoknIronProcessingCapability {
    string rdfs_label  
}
SudoknJoiningCapability {
    string rdfs_label  
}
SudoknKOSHERApproved {
    string rdfs_label  
}
SudoknKaptonProcessingCapability {
    string rdfs_label  
}
SudoknKittingCapability {
    string rdfs_label  
}
SudoknKnittingCapability {
    string rdfs_label  
}
SudoknKnurlingCapability {
    string rdfs_label  
}
SudoknKosherApprovedCertificate {

}
SudoknKovarProcessingCapability {
    string rdfs_label  
}
SudoknLEEDCertificate {
    string rdfs_label  
}
SudoknLaserBeamWeldingCapability {
    string rdfs_label  
}
SudoknLaserCuttingCapability {
    string rdfs_label  
}
SudoknLaserEtchingCapability {
    string rdfs_label  
}
SudoknLaserProcessingCapability {
    string rdfs_label  
}
SudoknLaserWeldingCapability {
    string rdfs_label  
}
SudoknLatheWorkCapability {
    string rdfs_label  
}
SudoknLeadProcessingCapability {
    string rdfs_label  
}
SudoknLexanProcessingCapability {
    string rdfs_label  
}
SudoknLiquidCoatingCapability {
    string rdfs_label  
}
SudoknLiveToolingCapability {
    string rdfs_label  
}
SudoknLowAlloySteelProcessingCapability {
    string rdfs_label  
}
SudoknMIGWeldinCapability {
    string rdfs_label  
}
SudoknMIGWeldingCapability {
    string rdfs_label  
}
SudoknMachinaryAndEquipmentIndustry {
    string rdfs_label  
}
SudoknMachineBuildingCapability {
    string rdfs_label  
}
SudoknMachiningCapability {
    string rdfs_label  
}
SudoknMagnesiumAlloyProcessingCapability {
    string rdfs_label  
}
SudoknMagnesiumProcessingCapability {
    string rdfs_label  
}
SudoknManMadeFiberProcessingCapability {
    string rdfs_label  
}
SudoknManagementOfCompaniesAndEnterprise {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknManufacturing {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknManufacturingProcessCapability {

}
SudoknMaterialProcessingCapability {

}
SudoknMechanicalAssemblyCapability {
    string rdfs_label  
}
SudoknMechanicalCoatingCapability {
    string rdfs_label  
}
SudoknMechanicalJoiningCapability {
    string rdfs_label  
}
SudoknMechanicalWeldingCapability {
    string rdfs_label  
}
SudoknMediaBlastingCapability {
    string rdfs_label  
}
SudoknMetalFabricationCapability {
    string rdfs_label  
}
SudoknMetalProcessingCapability {
    string rdfs_label  
}
SudoknMetalProductionIndustry {
    string rdfs_label  
}
SudoknMetalProductsIndustry {

}
SudoknMetalSpinningCapability {
    string rdfs_label  
}
SudoknMetalStampingCapability {
    string rdfs_label  
}
SudoknMetalsProductsIndustry {
    string rdfs_label  
}
SudoknMetalworkingCapability {
    string rdfs_label  
}
SudoknMigWeldingCapability {
    string rdfs_label  
}
SudoknMilitaryIndustry {
    string rdfs_label  
}
SudoknMillingCapability {
    string rdfs_label  
}
SudoknMining {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknMiningIndustry {
    string rdfs_label  
}
SudoknMoldMakingCapability {
    string rdfs_label  
}
SudoknMoldingCapability {
    string rdfs_label  
}
SudoknMolybdenumProcessingCapability {
    string rdfs_label  
}
SudoknMultiPointCuttingCapability {
    string rdfs_label  
}
SudoknNADCAPAC7004 {
    string rdfs_label  
}
SudoknNADCAPCertificate {
    string rdfs_label  
}
SudoknNAICS332111 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332112 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332114 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332115 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332116 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332117 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332211 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332212 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332213 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332214 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332311 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332312 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332313 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332321 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332322 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332323 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332410 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332420 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332431 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332439 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332510 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332611 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332612 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332618 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332710 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332721 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332722 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332811 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332812 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332813 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332911 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332912 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332913 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332919 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332991 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332992 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332994 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332995 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332996 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332997 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332998 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICS332999 {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNAICSClassifier {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknNIST-800-171Certificate {

}
SudoknNISTCertificate {

}
SudoknNaturalFiberProcessingCapability {
    string rdfs_label  
}
SudoknNickelPlatingCapability {
    string rdfs_label  
}
SudoknNickelProcessingCapability {
    string rdfs_label  
}
SudoknNitridingCapability {
    string rdfs_label  
}
SudoknNomexProcessingCapability {
    string rdfs_label  
}
SudoknNotchingCapability {
    string rdfs_label  
}
SudoknNylonProcessingCapability {
    string rdfs_label  
}
SudoknOffshoreWindIndustry {
    string rdfs_label  
}
SudoknOilAndGasIndustry {
    string rdfs_label  
}
SudoknOilGroovingCapability {
    string rdfs_label  
}
SudoknOrganizationName {

}
SudoknOwnershipStatusClassifier {
    string skos_altLabel  
    string rdfs_label  
}
SudoknOxy-FuelCuttingCapability {
    string rdfs_label  
}
SudoknPLCProgrammingCapability {
    string rdfs_label  
}
SudoknPackagingCapability {
    string rdfs_label  
}
SudoknPackingCapability {
    string rdfs_label  
}
SudoknPaintingCapability {
    string rdfs_label  
}
SudoknPalladiumProcessingCapability {
    string rdfs_label  
}
SudoknPaperIndustry {
    string rdfs_label  
}
SudoknPaperandPaperboardProductsIndustry {
    string rdfs_label  
}
SudoknPaperboardProductsIndustry {
    string rdfs_label  
}
SudoknPassivationCapability {
    string rdfs_label  
}
SudoknPemInsertionCapability {
    string rdfs_label  
}
SudoknPercussionWeldingCapability {
    string rdfs_label  
}
SudoknPermanentMoldCastingCapability {
    string rdfs_label  
}
SudoknPhosBronzeProcessingCapability {
    string rdfs_label  
}
SudoknPhosphateCoatingCapability {
    string rdfs_label  
}
SudoknPhosphorBronzeProcessingCapability {
    string rdfs_label  
}
SudoknPhysicalVaporDepositionCapability {
    string rdfs_label  
}
SudoknPipingFabricationCapability {
    string rdfs_label  
}
SudoknPlaningCapability {
    string rdfs_label  
}
SudoknPlasmaArcWeldingCapability {
    string rdfs_label  
}
SudoknPlasmaCuttingCapability {
    string rdfs_label  
}
SudoknPlasmaSprayingCapability {
    string rdfs_label  
}
SudoknPlasterMoldCastingCapability {
    string rdfs_label  
}
SudoknPlasticAndRubberIndustry {
    string rdfs_label  
}
SudoknPlasticMachiningCapability {
    string rdfs_label  
}
SudoknPlasticProcessingCapability {
    string rdfs_label  
}
SudoknPlasticsandRubberProductsIndustry {
    string rdfs_label  
}
SudoknPlatingCapability {
    string rdfs_label  
}
SudoknPlatinumProcessingCapability {
    string rdfs_label  
}
SudoknPolishingCapability {
    string rdfs_label  
}
SudoknPolycarbonateProcessingCapability {
    string rdfs_label  
}
SudoknPolycrystallineDiamondMachiningCapability {
    string rdfs_label  
}
SudoknPostalAddress {
    string iosc_hasTextValue  
}
SudoknPowderCoatingCapability {
    string rdfs_label  
}
SudoknPreciousMaterialProcessingCapability {
    string rdfs_label  
}
SudoknPressBrakingCapability {
    string rdfs_label  
}
SudoknPressingCapability {
    string rdfs_label  
}
SudoknPressureWeldingCapability {
    string rdfs_label  
}
SudoknPrintingAndInformationIndustry {
    string rdfs_label  
}
SudoknPrintingCapability {
    string rdfs_label  
}
SudoknProductDesignCapability {
    string rdfs_label  
}
SudoknProfessionalScientificAndTechnicalServices {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknProfessionalServices {

}
SudoknProfessionalServicesIndustry {
    string rdfs_label  
}
SudoknProjectionWeldingCapability {
    string rdfs_label  
}
SudoknPrototypeManufacturingCapability {
    string rdfs_label  
}
SudoknPrototypingCapability {
    string rdfs_label  
}
SudoknPublicAdministration {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknPulsedElectrochemicalMachiningCapability {
    string rdfs_label  
}
SudoknPunchingCapability {
    string rdfs_label  
}
SudoknQS9000 {
    string rdfs_label  
}
SudoknQS9000Certificate {
    string rdfs_label  
}
SudoknQSCertificate {

}
SudoknQualityCertificate {

}
SudoknQualityManagementCapability {

}
SudoknRAMEDMCapability {
    string rdfs_label  
}
SudoknRAMEdmCapability {
    string rdfs_label  
}
SudoknRamEDMCapability {
    string rdfs_label  
}
SudoknRapidPrototypingCapability {
    string rdfs_label  
}
SudoknRealEstateRentalAndLeasing {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknReamingCapability {
    string rdfs_label  
}
SudoknRecyclingIndustry {
    string rdfs_label  
}
SudoknResistanceBrazingCapability {
    string rdfs_label  
}
SudoknResistanceWeldingCapability {
    string rdfs_label  
}
SudoknRestaurantIndustry {
    string rdfs_label  
}
SudoknRetailIndustry {
    string rdfs_label  
}
SudoknRetailTrade {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknRetailTradeIndustry {
    string rdfs_label  
}
SudoknReverseEngineeringCapability {
    string rdfs_label  
}
SudoknRivetingCapability {
    string rdfs_label  
}
SudoknRivettingCapability {
    string rdfs_label  
}
SudoknRoboticWeldingCapability {
    string rdfs_label  
}
SudoknRollingCapability {
    string rdfs_label  
}
SudoknRubberProcessingCapability {
    string rdfs_label  
}
SudoknSandBlastingCapability {
    string rdfs_label  
}
SudoknSandCastingCapability {
    string rdfs_label  
}
SudoknSanitaryWeldingCapability {
    string rdfs_label  
}
SudoknSawingCapability {
    string rdfs_label  
}
SudoknScreenPrintingCapability {
    string rdfs_label  
}
SudoknSeamWeldingCapability {
    string rdfs_label  
}
SudoknSewingCapability {
    string rdfs_label  
}
SudoknShapingCapability {
    string rdfs_label  
}
SudoknShearingCapability {
    string rdfs_label  
}
SudoknSheeringCapability {
    string rdfs_label  
}
SudoknSheetMetalFabricationCapability {
    string rdfs_label  
}
SudoknSheetMetalFormingCapability {
    string rdfs_label  
}
SudoknSheetMetalProcessingCapability {
    string rdfs_label  
}
SudoknShellMoldCastingCapability {
    string rdfs_label  
}
SudoknShieldedMetalArcWeldingCapability {
    string rdfs_label  
}
SudoknShotPeeningCapability {
    string rdfs_label  
}
SudoknShrinkFittingCapability {
    string rdfs_label  
}
SudoknSiliconeProcessingCapability {
    string rdfs_label  
}
SudoknSilkScreeningCapability {
    string rdfs_label  
}
SudoknSilverProcessingCapability {
    string rdfs_label  
}
SudoknSinglePointCuttingCapability {
    string rdfs_label  
}
SudoknSinkerEDMCapability {
    string rdfs_label  
}
SudoknSinkerEdmCapability {
    string rdfs_label  
}
SudoknSinteringCapability {
    string rdfs_label  
}
SudoknSlabMillingCapability {
    string rdfs_label  
}
SudoknSmeltingCapability {
    string rdfs_label  
}
SudoknSolderingCapability {
    string rdfs_label  
}
SudoknSpecialBusinessStatusClassifier {

}
SudoknSpecialMaterialsProcessingCapability {
    string rdfs_label  
}
SudoknSpinningCapability {
    string rdfs_label  
}
SudoknSportsAndLeisureIndustry {
    string rdfs_label  
}
SudoknSportsandLeisureIndustry {
    string rdfs_label  
}
SudoknSpotWeldingCapability {
    string rdfs_label  
}
SudoknStainlessSteelProcessingCapability {
    string rdfs_label  
}
SudoknStampingCapability {
    string rdfs_label  
}
SudoknState {
    string rdfs_label  
}
SudoknStateOfAddress {

}
SudoknSteelAlloyProcessingCapability {
    string rdfs_label  
}
SudoknSteelManufacturingCapability {
    string rdfs_label  
}
SudoknSteelProcessingCapability {
    string rdfs_label  
}
SudoknStreetAddress {

}
SudoknStretchFormingCapability {
    string rdfs_label  
}
SudoknStudWeldingCapability {
    string rdfs_label  
}
SudoknSubmergedArcWeldingCapability {
    string rdfs_label  
}
SudoknSurfaceFinishingCapability {
    string rdfs_label  
}
SudoknSurfaceGrindingCapability {
    string rdfs_label  
}
SudoknSurfaceHardeningCapability {
    string rdfs_label  
}
SudoknSurfacePreparationCapability {
    string rdfs_label  
}
SudoknSwissMachiningCapability {
    string rdfs_label  
}
SudoknSwissTurningCapability {
    string rdfs_label  
}
SudoknTI-9000Certificate {

}
SudoknTI9000Certificate {
    string rdfs_label  
}
SudoknTICertificate {

}
SudoknTIGWeldingCapability {
    string rdfs_label  
}
SudoknTantalumProcessingCapability {
    string rdfs_label  
}
SudoknTappingCapability {
    string rdfs_label  
}
SudoknTeflonProcessingCapability {
    string rdfs_label  
}
SudoknTextileProcessCapability {

}
SudoknTextiles {
    string rdfs_label  
}
SudoknTextilesIndustry {
    string rdfs_label  
}
SudoknThermaJoiningCapability {
    string rdfs_label  
}
SudoknThermalCoatingCapability {
    string rdfs_label  
}
SudoknThermalSubtractionCapability {

}
SudoknThermalWeldingCapability {
    string rdfs_label  
}
SudoknThermoformingCapability {
    string rdfs_label  
}
SudoknTinProcessingCapability {
    string rdfs_label  
}
SudoknTitaniumProcessingCapability {
    string rdfs_label  
}
SudoknToolDesignCapability {

}
SudoknToolMakingCapability {
    string rdfs_label  
}
SudoknTorchBrazingCapability {
    string rdfs_label  
}
SudoknTorchCuttingCapability {

}
SudoknTransportationAndWarehousing {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknTransportationIndustry {
    string rdfs_label  
}
SudoknTubeBendingCapability {
    string rdfs_label  
}
SudoknTubeFormingCapability {
    string rdfs_label  
}
SudoknTubingCapability {
    string rdfs_label  
}
SudoknTungstenProcessingCapability {
    string rdfs_label  
}
SudoknTurningCapability {
    string rdfs_label  
}
SudoknTurretPunchingCapability {
    string rdfs_label  
}
SudoknTwoDimensionalCartesianSpatialCoordinateDatum {
    uri sudokn_hasLatitudeValue  
    string sudokn_hasLatitudeValue  
    uri sudokn_hasLongitudeValue  
    string sudokn_hasLongitudeValue  
}
SudoknUSPostalCode {
    string sudokn_hasIntegerValue  
}
SudoknUltrasonicWeldingCapability {
    string rdfs_label  
}
SudoknUnitedStatesPostalCode {

}
SudoknUrethaneProcessingCapability {
    string rdfs_label  
}
SudoknUtilities {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknUtilitiesIndustry {
    string rdfs_label  
}
SudoknVacuumCastingCapability {
    string rdfs_label  
}
SudoknVacuumFormingCapability {
    string rdfs_label  
}
SudoknVacuumHardeningCapability {
    string rdfs_label  
}
SudoknVacuumPackagingCapability {
    string rdfs_label  
}
SudoknVaporizedMetalCoatingCapability {
    string rdfs_label  
}
SudoknVerticalMillingCapability {
    string rdfs_label  
}
SudoknVitualLocationIdentifier {

}
SudoknWarehousingAndStorageIndustry {
    string rdfs_label  
}
SudoknWaspaloyProcessingCapability {
    string rdfs_label  
}
SudoknWaterAndSewerUtilitiesIndustry {
    string rdfs_label  
}
SudoknWaterJetCuttingCapability {
    string rdfs_label  
}
SudoknWaterandSewerUtilitiesIndustry {
    string rdfs_label  
}
SudoknWaterjetCuttimgCapability {
    string rdfs_label  
}
SudoknWaterjetCuttingCapability {
    string rdfs_label  
}
SudoknWeavingCapability {

}
SudoknWebAddress {

}
SudoknWeldingCapability {
    string rdfs_label  
}
SudoknWetPaintingCapability {
    string rdfs_label  
}
SudoknWholesaleTrade {
    uri sudokn_hasNAICSTextValue  
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
    uri sudokn_hasNAICSCodeValue  
}
SudoknWireBendingCapability {
    string rdfs_label  
}
SudoknWireEDMCapability {
    string rdfs_label  
}
SudoknWireFormingCapability {
    string rdfs_label  
}
SudoknWireHarnessAssemblyCapability {
    string rdfs_label  
}
SudoknWiringCapability {
    string rdfs_label  
}
SudoknWoodProcessingCapability {
    string rdfs_label  
}
SudoknWoodProductManufacturingIndustry {
    string rdfs_label  
}
SudoknWoodWorkingCapability {
    string rdfs_label  
}
SudoknWoodworkingCapability {
    string rdfs_label  
}
SudoknZincAlloyProcessingCapability {
    string rdfs_label  
}
SudoknZincArcSprayCapability {
    string rdfs_label  
}
SudoknZincProcessingCapability {
    string rdfs_label  
}
SudoknZirconProcessingCapability {
    string rdfs_label  
}
SudoknOrganizationSize {

}

IoManufacturer ||--|o SudoknNAICS332618 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332612 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332321 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332115 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332510 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332919 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332999 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332992 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332994 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332997 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332117 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332995 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332813 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332211 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332722 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332721 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332212 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332311 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332991 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332913 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332313 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332213 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332116 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332410 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332998 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332811 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332312 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332431 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332323 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332214 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332112 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICSClassifier : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332996 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332611 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332420 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332912 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332911 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332114 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332710 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332812 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332322 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332439 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332111 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o IoMaterialProduct : "sudokn_manufactures"
IoManufacturer ||--|o SudoknISO9000 : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknKOSHERApproved : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknISO14001 : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknISO13485 : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknAS9000Certificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknQS9000Certificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknNADCAPCertificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknISO14001Certificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknISO9001 : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknITARCertificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknISO9000Certificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknASME : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknHAACPCertificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknISO9001Certificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknIS-TS16949 : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknIATF16949Certificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknAWSWelderCertificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknNADCAPAC7004 : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknISTS16949Certificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknISO14000Certificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknBritishRetailConsortiumAccreditation : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknISOCertificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknASMECertificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknAS9102Certificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknBABACertificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknITARCompliant : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknAS9100 : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknFDACertificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknFDAGMPCompliant : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknQS9000 : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknISO13485Certificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknTI9000Certificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknAS9100Certificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknLEEDCertificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknLaserCuttingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknAssemblyCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknLaserProcessingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknWaterjetCuttimgCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPulsedElectrochemicalMachiningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknFixturingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCNCHorizontalTurningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCarbonitridingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSolderingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknGearCuttingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknElectronBeamWeldingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknMachineBuildingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPunchingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknMetalStampingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknFabricatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSmeltingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknDieCastingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknVerticalMillingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknDigitalPrintingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknRivettingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPassivationCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknAcrylicFabricationCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknFlameSprayingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknKnurlingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknWireFormingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCNCMachiningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknGalvanizingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknAssemblyCapibility : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknWireHarnessAssemblyCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCastingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCeramicMoldCastingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknDieMakingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknMetalSpinningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCNCCuttingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknVacuumCastingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSilkScreeningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknChemicalCoatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknMoldMakingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPlasterMoldCastingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSheetMetalFormingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknChemicalCleaningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPhosphateCoatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknRapidPrototypingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPolishingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknVacuumHardeningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPrintingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSandCastingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknTubingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknElectroplatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknTubeBendingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknKnittingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknToolMakingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknNickelPlatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknBrazingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCNCPressBrakeCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknWireEDMCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSinkerEDMCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknVacuumFormingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknElectropolishingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCustomFoamCuttingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o Sudokn3DPrintingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknBendingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCarburizingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknMillingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCoatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknAddtiveManufacturingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknWeldingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSinteringCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknMIGWeldinCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknVacuumPackagingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPlasticMachiningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPressingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSwissMachiningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCNCLatheCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknTurningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknAbrasiveCleaningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknFabricationCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknInvestmentCastingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknEmbossingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPackingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknShearingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknShrinkFittingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknLatheWorkCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCNCWireBendingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknChromateConversionCoatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknLiveToolingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknMediaBlastingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCNCMillingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPressBrakingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknInstallationCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknDeepFreezingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCNCFormingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknRollingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknNotchingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPipingFabricationCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknBoringCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknWetPaintingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCentrifugalCastingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknMIGWeldingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknHardeningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknRoboticWeldingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknElectricalDischargeMachiningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknTappingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknProductDesignCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o Sudokn2-AxisCNCTurningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknMetalFabricationCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknWireBendingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknHoningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknExtrudingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknLaserEtchingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCreepFeedGrindingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPlaningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknShellMoldCastingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknMetalworkingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPrototypingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCNCPlasmaCuttingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknWaterjetCuttingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPlasmaCuttingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknElectolessNickelPlatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknHotDipGalvanizingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknElectrolessPlatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknRAMEdmCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknChemicalProcessingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknFiberOpticLaserCuttingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCNCVerticalMillingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknContinuousCastingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknMechanicalAssemblyCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknJoiningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCADCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCenterlessGrindingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCNCmillingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknHeatTreatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknElectrolessNickelPlatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknGrindingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPLCProgrammingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknMoldingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknDrawingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknExtrusionCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknEtchingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSwissTurningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknScreenPrintingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknShapingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPlasmaSprayingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknFinishingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPaintingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknWiringCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPackagingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPlatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPrototypeManufacturingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknZincArcSprayCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknVaporizedMetalCoatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknRivetingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknRamEDMCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknTurretPunchingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknTIGWeldingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSheetMetalProcessingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSurfaceGrindingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknFasteningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknReverseEngineeringCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknAdditiveManufacturingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknDeepHoleDrillingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknDeburringCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknOilGroovingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknInductionHeatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknForgingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknElectroPlatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSheetMetalFabricationCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPowderCoatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCuttingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknEDMCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknAnnealingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknTubeFormingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSandBlastingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSurfaceFinishingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknNitridingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknFormingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknOxy-FuelCuttingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknMechanicalJoiningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknKittingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSanitaryWeldingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCNCBendingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCerakoteCoatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknReamingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknLiquidCoatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknHorizontalMillingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknEngineeringDesignCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknStampingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknFixtureDesignCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknWaterJetCuttingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSewingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPemInsertionCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPermanentMoldCastingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSinkerEdmCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknBrassBlackeningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknBlackOxideCoatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknAnodizingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknFillingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknWoodWorkingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknMigWeldingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCNCGrindingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknWoodworkingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknResistanceWeldingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknEndFormingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCNCLaserCuttingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPhysicalVaporDepositionCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknBroachingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCNCCylindricalGrindingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSurfacePreparationCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPolycrystallineDiamondMachiningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknDrillingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSpinningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknThermoformingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCylindricalGrindingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknHarperizingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknLaserWeldingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSpotWeldingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCNCTurningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSteelManufacturingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknMachiningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPostalAddress : "sudokn_hasPostalAddress"
IoManufacturer ||--|o SudoknUnitedStatesPostalCode : "sudokn_hasPostalAddress"
IoManufacturer ||--|o SudoknOwnershipStatusClassifier : "sudokn_hasOwnershipStatusClassifier"
IoManufacturer ||--|o SudoknWoodProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknBronzeProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknPhosphorBronzeProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknCarbonGraphiteProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknDelrinProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknSteelProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknInvarProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknMetalProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknTantalumProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknManMadeFiberProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknBerylliumProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknCeramicProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknTinProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknExoticMaterialProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknPalladiumProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknMagnesiumProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknDifficultToMachineMaterialsProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknSpecialMaterialsProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknChromiumProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknStainlessSteelProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknSteelAlloyProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknZincAlloyProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknPhosBronzeProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknMolybdenumProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknZirconProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknSilverProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknFoamProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknLowAlloySteelProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknCompositeProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknLexanProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknTungstenProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknHighGradeAluminumProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknGlassProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknIronProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknBrassProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknColdRolledSteelProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknRubberProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknKovarProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknChemicalsProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknLeadProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknNickelProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknNylonProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknPolycarbonateProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknGoldProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknNomexProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknAluminumProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknCopperProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknKaptonProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknPlasticProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknNaturalFiberProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknTeflonProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknZincProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknHastelloyProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknPlatinumProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknPreciousMaterialProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknWaspaloyProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknAcetalProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknAlloySteelProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknUrethaneProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknSiliconeProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknCarbideProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknExtremelyHardMaterialProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknTitaniumProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknCobaltProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknGraphiteProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknInconelProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknHealthCareServicesIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknTextiles : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknSportsandLeisureIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknOffshoreWindIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknUtilitiesIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknPaperIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknElectronicAutomotiveInudstry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknTransportationIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknMachinaryAndEquipmentIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknEducationalInstitutionsIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknProfessionalServicesIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknMetalProductionIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknOilAndGasIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknAgricultureIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknFurnitureIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknRecyclingIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknAerospaceIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknPaperandPaperboardProductsIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknChemicalAndPetrochemicalIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknPrintingAndInformationIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknComputersandElectronicProductsIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknRetailIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknCommunicationandElectronicPowerUtilitiesIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknWoodProductManufacturingIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknMetalsProductsIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknWaterandSewerUtilitiesIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknConsumerGoods : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknGovermentIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknPlasticsandRubberProductsIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknConsumerGoodsIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknApparelIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknHealthcareServicesIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknEducationIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknMilitaryIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknTextilesIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknIndustrialMachineryandEquipmentIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknGovernmentIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknElectronicProductIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknSportsAndLeisureIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknRetailTradeIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknWarehousingAndStorageIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknPlasticAndRubberIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknConstructionIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknFoodIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknCommunicationIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknMiningIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknAutomotiveIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknElectricVehiclesIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknBusinessEquipmentIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknGeospatialLocation : "sudokn_organizationLocatedIn"
IoManufacturer ||--|o SudoknNAICSClassifier : "sudokn_hasSecondaryNAICSClassifier"
OwlNamedIndividual ||--|o SudoknISO9000 : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknKOSHERApproved : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknISO14001 : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknISO13485 : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknAS9000Certificate : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknQS9000Certificate : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknNADCAPCertificate : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknISO14001Certificate : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknISO9001 : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknITARCertificate : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknISO9000Certificate : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknASME : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknHAACPCertificate : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknISO9001Certificate : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknIS-TS16949 : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknIATF16949Certificate : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknAWSWelderCertificate : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknNADCAPAC7004 : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknISTS16949Certificate : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknISO14000Certificate : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknBritishRetailConsortiumAccreditation : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknISOCertificate : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknASMECertificate : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknAS9102Certificate : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknBABACertificate : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknITARCompliant : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknAS9100 : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknFDACertificate : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknFDAGMPCompliant : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknQS9000 : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknISO13485Certificate : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknTI9000Certificate : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknAS9100Certificate : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknLEEDCertificate : "sudokn_hasCertificate"
OwlNamedIndividual ||--|o SudoknLaserCuttingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknAssemblyCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknLaserProcessingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknWaterjetCuttimgCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknPulsedElectrochemicalMachiningCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknFixturingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknCNCHorizontalTurningCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknCarbonitridingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknSolderingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknGearCuttingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknElectronBeamWeldingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknMachineBuildingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknPunchingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknMetalStampingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknFabricatingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknSmeltingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknDieCastingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknVerticalMillingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknDigitalPrintingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknRivettingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknPassivationCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknAcrylicFabricationCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknFlameSprayingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknKnurlingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknWireFormingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknCNCMachiningCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknGalvanizingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknAssemblyCapibility : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknWireHarnessAssemblyCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknCastingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknCeramicMoldCastingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknDieMakingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknMetalSpinningCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknCNCCuttingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknVacuumCastingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknSilkScreeningCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknChemicalCoatingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknMoldMakingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknPlasterMoldCastingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknSheetMetalFormingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknChemicalCleaningCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknPhosphateCoatingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknRapidPrototypingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknPolishingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknVacuumHardeningCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknPrintingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknSandCastingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknTubingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknElectroplatingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknTubeBendingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknKnittingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknToolMakingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknNickelPlatingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknBrazingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknCNCPressBrakeCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknWireEDMCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknSinkerEDMCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknVacuumFormingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknElectropolishingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknCustomFoamCuttingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o Sudokn3DPrintingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknBendingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknCarburizingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknMillingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknCoatingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknAddtiveManufacturingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknWeldingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknSinteringCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknMIGWeldinCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknVacuumPackagingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknPlasticMachiningCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknPressingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknSwissMachiningCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknCNCLatheCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknTurningCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknAbrasiveCleaningCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknFabricationCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknInvestmentCastingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknEmbossingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknPackingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknShearingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknShrinkFittingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknLatheWorkCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknCNCWireBendingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknChromateConversionCoatingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknLiveToolingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknMediaBlastingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknCNCMillingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknPressBrakingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknInstallationCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknDeepFreezingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknCNCFormingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknRollingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknNotchingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknPipingFabricationCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknBoringCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknWetPaintingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknCentrifugalCastingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknMIGWeldingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknHardeningCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknRoboticWeldingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknElectricalDischargeMachiningCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknTappingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknProductDesignCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o Sudokn2-AxisCNCTurningCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknMetalFabricationCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknWireBendingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknHoningCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknExtrudingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknLaserEtchingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknCreepFeedGrindingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknPlaningCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknShellMoldCastingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknMetalworkingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknPrototypingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknCNCPlasmaCuttingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknWaterjetCuttingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknPlasmaCuttingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknElectolessNickelPlatingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknHotDipGalvanizingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknElectrolessPlatingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknRAMEdmCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknChemicalProcessingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknFiberOpticLaserCuttingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknCNCVerticalMillingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknContinuousCastingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknMechanicalAssemblyCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknJoiningCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknCADCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknCenterlessGrindingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknCNCmillingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknHeatTreatingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknElectrolessNickelPlatingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknGrindingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknPLCProgrammingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknMoldingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknDrawingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknExtrusionCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknEtchingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknSwissTurningCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknScreenPrintingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknShapingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknPlasmaSprayingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknFinishingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknPaintingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknWiringCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknPackagingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknPlatingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknPrototypeManufacturingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknZincArcSprayCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknVaporizedMetalCoatingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknRivetingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknRamEDMCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknTurretPunchingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknTIGWeldingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknSheetMetalProcessingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknSurfaceGrindingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknFasteningCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknReverseEngineeringCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknAdditiveManufacturingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknDeepHoleDrillingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknDeburringCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknOilGroovingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknInductionHeatingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknForgingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknElectroPlatingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknSheetMetalFabricationCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknPowderCoatingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknCuttingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknEDMCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknAnnealingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknTubeFormingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknSandBlastingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknSurfaceFinishingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknNitridingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknFormingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknOxy-FuelCuttingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknMechanicalJoiningCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknKittingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknSanitaryWeldingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknCNCBendingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknCerakoteCoatingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknReamingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknLiquidCoatingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknHorizontalMillingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknEngineeringDesignCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknStampingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknFixtureDesignCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknWaterJetCuttingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknSewingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknPemInsertionCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknPermanentMoldCastingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknSinkerEdmCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknBrassBlackeningCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknBlackOxideCoatingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknAnodizingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknFillingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknWoodWorkingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknMigWeldingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknCNCGrindingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknWoodworkingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknResistanceWeldingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknEndFormingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknCNCLaserCuttingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknPhysicalVaporDepositionCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknBroachingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknCNCCylindricalGrindingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknSurfacePreparationCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknPolycrystallineDiamondMachiningCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknDrillingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknSpinningCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknThermoformingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknCylindricalGrindingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknHarperizingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknLaserWeldingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknSpotWeldingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknCNCTurningCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknSteelManufacturingCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknMachiningCapability : "sudokn_hasProcessCapability"
OwlNamedIndividual ||--|o SudoknPostalAddress : "sudokn_hasPostalAddress"
OwlNamedIndividual ||--|o SudoknUnitedStatesPostalCode : "sudokn_hasPostalAddress"
OwlNamedIndividual ||--|o SudoknOrganizationName : "sudokn_hasName"
OwlNamedIndividual ||--|o SudoknWebAddress : "sudokn_hasWebAddress"
OwlNamedIndividual ||--|o SudoknOwnershipStatusClassifier : "sudokn_hasOwnershipStatusClassifier"
OwlNamedIndividual ||--|o SudoknWoodProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknBronzeProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknPhosphorBronzeProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknCarbonGraphiteProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknDelrinProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknSteelProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknInvarProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknMetalProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknTantalumProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknManMadeFiberProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknBerylliumProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknCeramicProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknTinProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknExoticMaterialProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknPalladiumProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknMagnesiumProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknDifficultToMachineMaterialsProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknSpecialMaterialsProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknChromiumProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknStainlessSteelProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknSteelAlloyProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknZincAlloyProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknPhosBronzeProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknMolybdenumProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknZirconProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknSilverProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknFoamProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknLowAlloySteelProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknCompositeProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknLexanProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknTungstenProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknHighGradeAluminumProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknGlassProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknIronProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknBrassProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknColdRolledSteelProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknRubberProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknKovarProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknChemicalsProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknLeadProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknNickelProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknNylonProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknPolycarbonateProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknGoldProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknNomexProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknAluminumProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknCopperProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknKaptonProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknPlasticProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknNaturalFiberProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknTeflonProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknZincProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknHastelloyProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknPlatinumProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknPreciousMaterialProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknWaspaloyProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknAcetalProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknAlloySteelProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknUrethaneProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknSiliconeProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknCarbideProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknExtremelyHardMaterialProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknTitaniumProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknCobaltProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknGraphiteProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknInconelProcessingCapability : "sudokn_hasMaterialCapability"
OwlNamedIndividual ||--|o SudoknQualityManagementCapability : "sudokn_hasManagementCapability"
OwlNamedIndividual ||--|o SudoknHealthCareServicesIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknTextiles : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknSportsandLeisureIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknOffshoreWindIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknUtilitiesIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknPaperIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknElectronicAutomotiveInudstry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknTransportationIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknMachinaryAndEquipmentIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknEducationalInstitutionsIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknProfessionalServicesIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknMetalProductionIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknOilAndGasIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknAgricultureIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknFurnitureIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknRecyclingIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknAerospaceIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknPaperandPaperboardProductsIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknChemicalAndPetrochemicalIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknPrintingAndInformationIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknComputersandElectronicProductsIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknRetailIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknCommunicationandElectronicPowerUtilitiesIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknWoodProductManufacturingIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknMetalsProductsIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknWaterandSewerUtilitiesIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknConsumerGoods : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknGovermentIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknPlasticsandRubberProductsIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknConsumerGoodsIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknApparelIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknHealthcareServicesIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknEducationIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknMilitaryIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknTextilesIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknIndustrialMachineryandEquipmentIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknGovernmentIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknElectronicProductIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknSportsAndLeisureIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknRetailTradeIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknWarehousingAndStorageIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknPlasticAndRubberIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknConstructionIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknFoodIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknCommunicationIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknMiningIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknAutomotiveIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknElectricVehiclesIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknBusinessEquipmentIndustry : "sudokn_suppliesToIndustry"
OwlNamedIndividual ||--|o SudoknNAICSClassifier : "sudokn_hasNAICSClassifier"
OwlNamedIndividual ||--|o SudoknEmailAddress : "sudokn_hasEmailAddress"
SudoknAS9100Certificate ||--|o SudoknQualityManagementCapability : "sudokn_attestsTo"
SudoknCity ||--|o SudoknState : "sudokn_locatedInState"
SudoknGeospatialLocation ||--|o SudoknUSPostalCode : "sudokn_hasZIPcode"
SudoknGeospatialLocation ||--|o SudoknPostalAddress : "sudokn_hasPostalAddress"
SudoknGeospatialLocation ||--|o SudoknUnitedStatesPostalCode : "sudokn_hasPostalAddress"
SudoknGeospatialLocation ||--|o SudoknTwoDimensionalCartesianSpatialCoordinateDatum : "sudokn_hasSpatialCoordinates"
SudoknGeospatialLocation ||--|o SudoknCity : "sudokn_locatedInCity"
SudoknISO9000Certificate ||--|o SudoknQualityManagementCapability : "sudokn_attestsTo"

```


## IRI prefixes

* dct: http://purl.org/dc/terms/
* io: https://spec.industrialontologies.org/ontology/core/Core/
* iosc: https://spec.industrialontologies.org/ontology/supplychain/SupplyChain/
* linkml: https://w3id.org/linkml/
* obo: http://purl.obolibrary.org/obo/
* owl: http://www.w3.org/2002/07/owl#
* rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
* rdfs: http://www.w3.org/2000/01/rdf-schema#
* skos: http://www.w3.org/2004/02/skos/core#
* sudokn: http://asu.edu/semantics/SUDOKN/
* xsd: http://www.w3.org/2001/XMLSchema#



## Classes

| Class | Description |
| --- | --- |
| [IoGroupOfPersons](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/IoGroupOfPersons.md) | No type description provided<br/>Class with 0 occurences.| 
| [IoIdentifier](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/IoIdentifier.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknDesignativeName](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDesignativeName.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBrandName](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBrandName.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknOrganizationName](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknOrganizationName.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknVitualLocationIdentifier](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknVitualLocationIdentifier.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknEmailAddress](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknEmailAddress.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknWebAddress](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWebAddress.md) | No type description provided<br/>Class with 1 occurences.| 
| [IoInformationContentEntity](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/IoInformationContentEntity.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCertificate.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknQualityCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknQualityCertificate.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknASCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknASCertificate.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAS9003Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAS9003Certificate.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAS9100Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAS9100Certificate.md) | No type description provided<br/>Class with 1220 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAS9102Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAS9102Certificate.md) | No type description provided<br/>Class with 9 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknASMECertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknASMECertificate.md) | No type description provided<br/>Class with 804 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBABACertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBABACertificate.md) | No type description provided<br/>Class with 3 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBritishRetailConsortiumCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBritishRetailConsortiumCertificate.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFDACertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFDACertificate.md) | No type description provided<br/>Class with 5 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFDA-GMPCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFDA-GMPCertificate.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFDA-PMACertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFDA-PMACertificate.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknGWOCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGWOCertificate.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknHAACPCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHAACPCertificate.md) | No type description provided<br/>Class with 2 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknISOCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknISOCertificate.md) | No type description provided<br/>Class with 67 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknISO13485Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknISO13485Certificate.md) | No type description provided<br/>Class with 326 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknISO14000Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknISO14000Certificate.md) | No type description provided<br/>Class with 12 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknISO14001Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknISO14001Certificate.md) | No type description provided<br/>Class with 321 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknISO17265Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknISO17265Certificate.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknISO27001Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknISO27001Certificate.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknISO9000Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknISO9000Certificate.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknISO9001Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknISO9001Certificate.md) | No type description provided<br/>Class with 3466 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknISTSCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknISTSCertificate.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknISTS-16949Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknISTS-16949Certificate.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknITARCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknITARCertificate.md) | No type description provided<br/>Class with 127 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknKosherApprovedCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknKosherApprovedCertificate.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNADCAPCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNADCAPCertificate.md) | No type description provided<br/>Class with 467 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNISTCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNISTCertificate.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNIST-800-171Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNIST-800-171Certificate.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknQSCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknQSCertificate.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknQS9000Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknQS9000Certificate.md) | No type description provided<br/>Class with 41 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknTICertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTICertificate.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknTI-9000Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTI-9000Certificate.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknClassifier](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknClassifier.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICSClassifier](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICSClassifier.md) | No type description provided<br/>Class with 23 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAccommodationAndFoodServices](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAccommodationAndFoodServices.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAdministrativeAndSupportAndWasteServices](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAdministrativeAndSupportAndWasteServices.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAgricultureForestryFishingAndHunting](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAgricultureForestryFishingAndHunting.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknArtsEnterntainmentAndRecreation](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknArtsEnterntainmentAndRecreation.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknConstruction](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknConstruction.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknEducationalServices](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknEducationalServices.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFinanceAndInsurance](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFinanceAndInsurance.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknHealthcareAndSocialAssistance](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHealthcareAndSocialAssistance.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknInformation](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknInformation.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknManagementOfCompaniesAndEnterprise](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknManagementOfCompaniesAndEnterprise.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknManufacturing](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknManufacturing.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMining](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMining.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknProfessionalScientificAndTechnicalServices](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknProfessionalScientificAndTechnicalServices.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPublicAdministration](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPublicAdministration.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknRealEstateRentalAndLeasing](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknRealEstateRentalAndLeasing.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknRetailTrade](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknRetailTrade.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknTransportationAndWarehousing](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTransportationAndWarehousing.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknUtilities](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknUtilities.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknWholesaleTrade](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWholesaleTrade.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSpecialBusinessStatusClassifier](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSpecialBusinessStatusClassifier.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknOwnershipStatusClassifier](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknOwnershipStatusClassifier.md) | No type description provided<br/>Class with 8 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknTwoDimensionalCartesianSpatialCoordinateDatum](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTwoDimensionalCartesianSpatialCoordinateDatum.md) | No type description provided<br/>Class with 20728 occurences.| 
| [IoManufacturer](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/IoManufacturer.md) | No type description provided<br/>Class with 11367 occurences.| 
| [IoMaterialProduct](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/IoMaterialProduct.md) | No type description provided<br/>Class with 44818 occurences.| 
| [IoPhysicalLocationIdentifier](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/IoPhysicalLocationIdentifier.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBuildingNumber](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBuildingNumber.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCityOfAddress](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCityOfAddress.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCountryOfAddress](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCountryOfAddress.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPostalAddress](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPostalAddress.md) | No type description provided<br/>Class with 20728 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknStateOfAddress](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknStateOfAddress.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknStreetAddress](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknStreetAddress.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknUnitedStatesPostalCode](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknUnitedStatesPostalCode.md) | No type description provided<br/>Class with 1 occurences.| 
| [IoscIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/IoscIndustry.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAerospaceIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAerospaceIndustry.md) | No type description provided<br/>Class with 2 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAgricultureIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAgricultureIndustry.md) | No type description provided<br/>Class with 2 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknApparelIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknApparelIndustry.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAutomotiveIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAutomotiveIndustry.md) | No type description provided<br/>Class with 2 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknElectricAutomotiveIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectricAutomotiveIndustry.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBusinessEquipmentIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBusinessEquipmentIndustry.md) | No type description provided<br/>Class with 2 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCommunicationsIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCommunicationsIndustry.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknConstructionIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknConstructionIndustry.md) | No type description provided<br/>Class with 2 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknConsumerGoodsIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknConsumerGoodsIndustry.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknEducationIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknEducationIndustry.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknElectronicProductIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectronicProductIndustry.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknComputerIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknComputerIndustry.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFoodIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFoodIndustry.md) | No type description provided<br/>Class with 2 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBeverageIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBeverageIndustry.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknRestaurantIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknRestaurantIndustry.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFurnitureIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFurnitureIndustry.md) | No type description provided<br/>Class with 2 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknGovernmentIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGovernmentIndustry.md) | No type description provided<br/>Class with 2 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknHealthcareServices](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHealthcareServices.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMachinaryAndEquipmentIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMachinaryAndEquipmentIndustry.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMetalProductsIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMetalProductsIndustry.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMilitaryIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMilitaryIndustry.md) | No type description provided<br/>Class with 2 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMiningIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMiningIndustry.md) | No type description provided<br/>Class with 2 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknOffshoreWindIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknOffshoreWindIndustry.md) | No type description provided<br/>Class with 2 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPaperIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPaperIndustry.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPaperboardProductsIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPaperboardProductsIndustry.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPlasticAndRubberIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPlasticAndRubberIndustry.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPrintingAndInformationIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPrintingAndInformationIndustry.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknProfessionalServices](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknProfessionalServices.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknRecyclingIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknRecyclingIndustry.md) | No type description provided<br/>Class with 2 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknRetailIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknRetailIndustry.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSportsAndLeisureIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSportsAndLeisureIndustry.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknTextilesIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTextilesIndustry.md) | No type description provided<br/>Class with 2 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknTransportationIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTransportationIndustry.md) | No type description provided<br/>Class with 2 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknUtilitiesIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknUtilitiesIndustry.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCommunicationAndElectronicPowerUtilitiesIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCommunicationAndElectronicPowerUtilitiesIndustry.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknWaterAndSewerUtilitiesIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWaterAndSewerUtilitiesIndustry.md) | No type description provided<br/>Class with 0 occurences.| 
| [IoscProductionCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/IoscProductionCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknEngineeringCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknEngineeringCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCADCAMCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCADCAMCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCADCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCADCapability.md) | No type description provided<br/>Class with 3 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCAECapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCAECapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknEngineeringDesignCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknEngineeringDesignCapability.md) | No type description provided<br/>Class with 28 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPLCProgrammingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPLCProgrammingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknReverseEngineeringCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknReverseEngineeringCapability.md) | No type description provided<br/>Class with 2 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknToolDesignCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknToolDesignCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknDieDesignCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDieDesignCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFixtureDesignCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFixtureDesignCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknManufacturingProcessCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknManufacturingProcessCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAssemblyCapibility](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAssemblyCapibility.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFabricatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFabricatingCapability.md) | No type description provided<br/>Class with 2518 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknKittingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknKittingCapability.md) | No type description provided<br/>Class with 2 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknWireHarnessAssemblyCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWireHarnessAssemblyCapability.md) | No type description provided<br/>Class with 23 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCastingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCastingCapability.md) | No type description provided<br/>Class with 1195 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFinishingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFinishingCapability.md) | No type description provided<br/>Class with 1615 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCoatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCoatingCapability.md) | No type description provided<br/>Class with 1744 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBlackOxideCoatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBlackOxideCoatingCapability.md) | No type description provided<br/>Class with 228 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknChemicalCoatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknChemicalCoatingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknElectroPlatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectroPlatingCapability.md) | No type description provided<br/>Class with 1339 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknElectrolessNickelPlating](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectrolessNickelPlating.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknGalvanizingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGalvanizingCapability.md) | No type description provided<br/>Class with 72 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMechanicalCoatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMechanicalCoatingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPowderCoatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPowderCoatingCapability.md) | No type description provided<br/>Class with 679 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPhosphateCoatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPhosphateCoatingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPrintingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPrintingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknWetPaintingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWetPaintingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknThermalCoatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknThermalCoatingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknVaporizedMetalCoatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknVaporizedMetalCoatingCapability.md) | No type description provided<br/>Class with 13 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPhysicalVaporDepositionCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPhysicalVaporDepositionCapability.md) | No type description provided<br/>Class with 10 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSurfacePreparationCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSurfacePreparationCapability.md) | No type description provided<br/>Class with 550 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBeltSandingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBeltSandingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSandBlastingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSandBlastingCapability.md) | No type description provided<br/>Class with 340 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknShotPeeningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknShotPeeningCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknForgingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknForgingCapability.md) | No type description provided<br/>Class with 609 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFormingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFormingCapability.md) | No type description provided<br/>Class with 1802 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknDrawingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDrawingCapability.md) | No type description provided<br/>Class with 1449 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknExtrudingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknExtrudingCapability.md) | No type description provided<br/>Class with 602 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknRollingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknRollingCapability.md) | No type description provided<br/>Class with 605 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknHeatTreatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHeatTreatingCapability.md) | No type description provided<br/>Class with 923 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknHardeningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHardeningCapability.md) | No type description provided<br/>Class with 269 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSurfaceHardeningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSurfaceHardeningCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknDiffusionHardeningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDiffusionHardeningCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCarburizingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCarburizingCapability.md) | No type description provided<br/>Class with 81 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNitridingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNitridingCapability.md) | No type description provided<br/>Class with 45 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknVacuumHardeningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknVacuumHardeningCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknJoiningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknJoiningCapability.md) | No type description provided<br/>Class with 437 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMechanicalJoiningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMechanicalJoiningCapability.md) | No type description provided<br/>Class with 3 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMechanicalWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMechanicalWeldingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknExplosiveWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknExplosiveWeldingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFrictionWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFrictionWeldingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPressureWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPressureWeldingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknUltrasonicWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknUltrasonicWeldingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknRivetingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknRivetingCapability.md) | No type description provided<br/>Class with 2 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknThermaJoiningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknThermaJoiningCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBrazingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBrazingCapability.md) | No type description provided<br/>Class with 147 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknDipBrazingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDipBrazingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFurnaceBrazingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFurnaceBrazingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknInductionBrazingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknInductionBrazingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknInfraredBrazingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknInfraredBrazingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknResistanceBrazingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknResistanceBrazingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknTorchBrazingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTorchBrazingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSolderingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSolderingCapability.md) | No type description provided<br/>Class with 271 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknThermalWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknThermalWeldingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBrazeWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBrazeWeldingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCarbonArcBrazingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCarbonArcBrazingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknGasBrazingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGasBrazingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknDiffusionBondingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDiffusionBondingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknElectricalResistanceWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectricalResistanceWeldingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknButtWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknButtWeldingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknElectroSlagWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectroSlagWeldingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPercussionWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPercussionWeldingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknProjectionWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknProjectionWeldingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSeamWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSeamWeldingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSpotWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSpotWeldingCapability.md) | No type description provided<br/>Class with 3 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknElectricArcWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectricArcWeldingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCarbonArcWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCarbonArcWeldingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknGasMetalArcWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGasMetalArcWeldingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMIGWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMIGWeldingCapability.md) | No type description provided<br/>Class with 2 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknGasTungstenArcWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGasTungstenArcWeldingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknTIGWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTIGWeldingCapability.md) | No type description provided<br/>Class with 3 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknShieldedMetalArcWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknShieldedMetalArcWeldingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknStudWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknStudWeldingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSubmergedArcWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSubmergedArcWeldingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknGasWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGasWeldingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAtomicHydrogenWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAtomicHydrogenWeldingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCombustableGasWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCombustableGasWeldingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknHighEnergyBeamWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHighEnergyBeamWeldingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknElectronBeamWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectronBeamWeldingCapability.md) | No type description provided<br/>Class with 6 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknLaserBeamWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknLaserBeamWeldingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPlasmaArcWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPlasmaArcWeldingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMachiningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMachiningCapability.md) | No type description provided<br/>Class with 3494 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAbrassiveMachiningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAbrassiveMachiningCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknGrindingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGrindingCapability.md) | No type description provided<br/>Class with 1654 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCenterlessGrindingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCenterlessGrindingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknClyndricalGrindingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknClyndricalGrindingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCNCClyndricalGrindingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCClyndricalGrindingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknHoningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHoningCapability.md) | No type description provided<br/>Class with 460 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCNCMachiningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCMachiningCapability.md) | No type description provided<br/>Class with 1427 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMultiPointCuttingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMultiPointCuttingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBroachingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBroachingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknGearCuttingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGearCuttingCapability.md) | No type description provided<br/>Class with 2 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknGearHobbingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGearHobbingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknHoleMakingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHoleMakingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCounterBoringCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCounterBoringCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCounterSinkingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCounterSinkingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknDrillingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDrillingCapability.md) | No type description provided<br/>Class with 1361 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknDeepHoleDrillingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDeepHoleDrillingCapability.md) | No type description provided<br/>Class with 81 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknReamingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknReamingCapability.md) | No type description provided<br/>Class with 278 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknTappingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTappingCapability.md) | No type description provided<br/>Class with 860 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMillingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMillingCapability.md) | No type description provided<br/>Class with 2311 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCNCMillingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCMillingCapability.md) | No type description provided<br/>Class with 1105 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknHorizontalMillingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHorizontalMillingCapability.md) | No type description provided<br/>Class with 181 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSlabMillingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSlabMillingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknVerticalMillingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknVerticalMillingCapability.md) | No type description provided<br/>Class with 437 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknEndMillingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknEndMillingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFaceMillingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFaceMillingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSawingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSawingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSinglePointCuttingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSinglePointCuttingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPlaningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPlaningCapability.md) | No type description provided<br/>Class with 17 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknShapingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknShapingCapability.md) | No type description provided<br/>Class with 504 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknTurningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTurningCapability.md) | No type description provided<br/>Class with 2077 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCNCTurningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCTurningCapability.md) | No type description provided<br/>Class with 16 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMoldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMoldingCapability.md) | No type description provided<br/>Class with 644 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknInjectionMoldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknInjectionMoldingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPackingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPackingCapability.md) | No type description provided<br/>Class with 1765 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSheetMetalProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSheetMetalProcessingCapability.md) | No type description provided<br/>Class with 28 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBendingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBendingCapability.md) | No type description provided<br/>Class with 945 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknWireBendingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWireBendingCapability.md) | No type description provided<br/>Class with 3 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknEmbossingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknEmbossingCapability.md) | No type description provided<br/>Class with 69 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPunchingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPunchingCapability.md) | No type description provided<br/>Class with 7 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSheeringCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSheeringCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSpinningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSpinningCapability.md) | No type description provided<br/>Class with 38 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknStampingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknStampingCapability.md) | No type description provided<br/>Class with 1216 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknStretchFormingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknStretchFormingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknTextileProcessCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTextileProcessCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCrochetCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCrochetCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknDyeingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDyeingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknKnittingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknKnittingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknWeavingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWeavingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknThermalSubtractionCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknThermalSubtractionCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknEDMCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknEDMCapability.md) | No type description provided<br/>Class with 1114 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknHoleDrillingEDMCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHoleDrillingEDMCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknRAMEDMCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknRAMEDMCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSinkerEDMCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSinkerEDMCapability.md) | No type description provided<br/>Class with 148 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknWireEDMCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWireEDMCapability.md) | No type description provided<br/>Class with 644 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknHighEnergyBeamMachiningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHighEnergyBeamMachiningCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknLaserCuttingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknLaserCuttingCapability.md) | No type description provided<br/>Class with 581 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCNCLaserCuttingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCLaserCuttingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknTorchCuttingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTorchCuttingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPlasmaCuttingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPlasmaCuttingCapability.md) | No type description provided<br/>Class with 235 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknToolMakingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknToolMakingCapability.md) | No type description provided<br/>Class with 6 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMoldMakingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMoldMakingCapability.md) | No type description provided<br/>Class with 8 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknWoodWorkingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWoodWorkingCapability.md) | No type description provided<br/>Class with 12 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMaterialProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMaterialProcessingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCarbonProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCarbonProcessingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCeramicProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCeramicProcessingCapability.md) | No type description provided<br/>Class with 1051 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknChemicalsProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknChemicalsProcessingCapability.md) | No type description provided<br/>Class with 1344 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCompositeProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCompositeProcessingCapability.md) | No type description provided<br/>Class with 1196 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknElectronicProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectronicProcessingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFiberProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFiberProcessingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknManMadeFiberProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknManMadeFiberProcessingCapability.md) | No type description provided<br/>Class with 2 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNaturalFiberProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNaturalFiberProcessingCapability.md) | No type description provided<br/>Class with 15 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFoamProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFoamProcessingCapability.md) | No type description provided<br/>Class with 1065 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknGlassProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGlassProcessingCapability.md) | No type description provided<br/>Class with 2866 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMetalProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMetalProcessingCapability.md) | No type description provided<br/>Class with 6560 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAluminumProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAluminumProcessingCapability.md) | No type description provided<br/>Class with 5647 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBrassProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBrassProcessingCapability.md) | No type description provided<br/>Class with 2596 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBronzeProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBronzeProcessingCapability.md) | No type description provided<br/>Class with 1754 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCopperProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCopperProcessingCapability.md) | No type description provided<br/>Class with 2784 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknIronProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknIronProcessingCapability.md) | No type description provided<br/>Class with 5903 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMagnesiumAlloyProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMagnesiumAlloyProcessingCapability.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSteelProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSteelProcessingCapability.md) | No type description provided<br/>Class with 7200 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknStainlessSteelProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknStainlessSteelProcessingCapability.md) | No type description provided<br/>Class with 4796 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknTitaniumProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTitaniumProcessingCapability.md) | No type description provided<br/>Class with 1349 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknZincAlloyProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknZincAlloyProcessingCapability.md) | No type description provided<br/>Class with 80 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPlasticProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPlasticProcessingCapability.md) | No type description provided<br/>Class with 4159 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknRubberProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknRubberProcessingCapability.md) | No type description provided<br/>Class with 1830 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSiliconeProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSiliconeProcessingCapability.md) | No type description provided<br/>Class with 690 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknUrethaneProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknUrethaneProcessingCapability.md) | No type description provided<br/>Class with 1039 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknWoodProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWoodProcessingCapability.md) | No type description provided<br/>Class with 2918 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknQualityManagementCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknQualityManagementCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [OboBFO0000019](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/OboBFO0000019.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknOrganizationSize](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknOrganizationSize.md) | No type description provided<br/>Class with 1 occurences.| 
| [OboBFO0000029](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/OboBFO0000029.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknGeopoliticalSite](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGeopoliticalSite.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCity](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCity.md) | No type description provided<br/>Class with 2994 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCountry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCountry.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCounty](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCounty.md) | No type description provided<br/>Class with 0 occurences.| 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknState](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknState.md) | No type description provided<br/>Class with 129 occurences.| 
| [OwlNamedIndividual](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/OwlNamedIndividual.md) | No type description provided<br/>Class with 29 occurences.| 
| [Sudokn2-AxisCNCTurningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/Sudokn2-AxisCNCTurningCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [Sudokn3DPrintingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/Sudokn3DPrintingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknAbrasiveCleaningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAbrasiveCleaningCapability.md) | No type description provided<br/>Class with 9 occurences.| 
| [SudoknAcetalProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAcetalProcessingCapability.md) | No type description provided<br/>Class with 362 occurences.| 
| [SudoknAcrylicFabricationCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAcrylicFabricationCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknAdditiveManufacturingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAdditiveManufacturingCapability.md) | No type description provided<br/>Class with 209 occurences.| 
| [SudoknAddtiveManufacturingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAddtiveManufacturingCapability.md) | No type description provided<br/>Class with 337 occurences.| 
| [SudoknAlloySteelProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAlloySteelProcessingCapability.md) | No type description provided<br/>Class with 825 occurences.| 
| [SudoknAnnealingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAnnealingCapability.md) | No type description provided<br/>Class with 99 occurences.| 
| [SudoknAnodizingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAnodizingCapability.md) | No type description provided<br/>Class with 659 occurences.| 
| [SudoknAS9000Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAS9000Certificate.md) | No type description provided<br/>Class with 5 occurences.| 
| [SudoknAS9100](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAS9100.md) | No type description provided<br/>Class with 20 occurences.| 
| [SudoknASME](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknASME.md) | No type description provided<br/>Class with 10 occurences.| 
| [SudoknAssemblyCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAssemblyCapability.md) | No type description provided<br/>Class with 2931 occurences.| 
| [SudoknAWSWelderCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAWSWelderCertificate.md) | No type description provided<br/>Class with 48 occurences.| 
| [SudoknBerylliumProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBerylliumProcessingCapability.md) | No type description provided<br/>Class with 360 occurences.| 
| [SudoknBoringCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBoringCapability.md) | No type description provided<br/>Class with 857 occurences.| 
| [SudoknBrassBlackeningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBrassBlackeningCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknBritishRetailConsortiumAccreditation](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBritishRetailConsortiumAccreditation.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknCarbideProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCarbideProcessingCapability.md) | No type description provided<br/>Class with 786 occurences.| 
| [SudoknCarbonGraphiteProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCarbonGraphiteProcessingCapability.md) | No type description provided<br/>Class with 13 occurences.| 
| [SudoknCarbonitridingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCarbonitridingCapability.md) | No type description provided<br/>Class with 43 occurences.| 
| [SudoknCentrifugalCastingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCentrifugalCastingCapability.md) | No type description provided<br/>Class with 17 occurences.| 
| [SudoknCerakoteCoatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCerakoteCoatingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknCeramicMoldCastingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCeramicMoldCastingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknChemicalAndPetrochemicalIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknChemicalAndPetrochemicalIndustry.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknChemicalCleaningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknChemicalCleaningCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknChemicalProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknChemicalProcessingCapability.md) | No type description provided<br/>Class with 194 occurences.| 
| [SudoknChromateConversionCoatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknChromateConversionCoatingCapability.md) | No type description provided<br/>Class with 139 occurences.| 
| [SudoknChromiumProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknChromiumProcessingCapability.md) | No type description provided<br/>Class with 551 occurences.| 
| [SudoknCNCBendingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCBendingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknCNCCuttingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCCuttingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknCNCCylindricalGrindingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCCylindricalGrindingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknCNCFormingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCFormingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknCNCGrindingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCGrindingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknCNCHorizontalTurningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCHorizontalTurningCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknCNCLatheCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCLatheCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknCNCmillingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCmillingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknCNCPlasmaCuttingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCPlasmaCuttingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknCNCPressBrakeCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCPressBrakeCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknCNCVerticalMillingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCVerticalMillingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknCNCWireBendingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCWireBendingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknCobaltProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCobaltProcessingCapability.md) | No type description provided<br/>Class with 303 occurences.| 
| [SudoknColdRolledSteelProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknColdRolledSteelProcessingCapability.md) | No type description provided<br/>Class with 252 occurences.| 
| [SudoknCommunicationandElectronicPowerUtilitiesIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCommunicationandElectronicPowerUtilitiesIndustry.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknCommunicationIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCommunicationIndustry.md) | No type description provided<br/>Class with 2 occurences.| 
| [SudoknComputersandElectronicProductsIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknComputersandElectronicProductsIndustry.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknConsumerGoods](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknConsumerGoods.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknContinuousCastingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknContinuousCastingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknCreepFeedGrindingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCreepFeedGrindingCapability.md) | No type description provided<br/>Class with 8 occurences.| 
| [SudoknCustomFoamCuttingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCustomFoamCuttingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknCuttingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCuttingCapability.md) | No type description provided<br/>Class with 19 occurences.| 
| [SudoknCylindricalGrindingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCylindricalGrindingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknDeburringCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDeburringCapability.md) | No type description provided<br/>Class with 86 occurences.| 
| [SudoknDeepFreezingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDeepFreezingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknDelrinProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDelrinProcessingCapability.md) | No type description provided<br/>Class with 289 occurences.| 
| [SudoknDieCastingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDieCastingCapability.md) | No type description provided<br/>Class with 220 occurences.| 
| [SudoknDieMakingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDieMakingCapability.md) | No type description provided<br/>Class with 6 occurences.| 
| [SudoknDifficultToMachineMaterialsProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDifficultToMachineMaterialsProcessingCapability.md) | No type description provided<br/>Class with 28 occurences.| 
| [SudoknDigitalPrintingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDigitalPrintingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknEducationalInstitutionsIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknEducationalInstitutionsIndustry.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknElectolessNickelPlatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectolessNickelPlatingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknElectricalDischargeMachiningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectricalDischargeMachiningCapability.md) | No type description provided<br/>Class with 197 occurences.| 
| [SudoknElectricVehiclesIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectricVehiclesIndustry.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknElectrolessNickelPlatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectrolessNickelPlatingCapability.md) | No type description provided<br/>Class with 214 occurences.| 
| [SudoknElectrolessPlatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectrolessPlatingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknElectronicAutomotiveInudstry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectronicAutomotiveInudstry.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknElectroplatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectroplatingCapability.md) | No type description provided<br/>Class with 3 occurences.| 
| [SudoknElectropolishingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectropolishingCapability.md) | No type description provided<br/>Class with 61 occurences.| 
| [SudoknEndFormingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknEndFormingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknEtchingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknEtchingCapability.md) | No type description provided<br/>Class with 487 occurences.| 
| [SudoknExoticMaterialProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknExoticMaterialProcessingCapability.md) | No type description provided<br/>Class with 317 occurences.| 
| [SudoknExtremelyHardMaterialProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknExtremelyHardMaterialProcessingCapability.md) | No type description provided<br/>Class with 12 occurences.| 
| [SudoknExtrusionCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknExtrusionCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknFabricationCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFabricationCapability.md) | No type description provided<br/>Class with 121 occurences.| 
| [SudoknFasteningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFasteningCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknFDAGMPCompliant](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFDAGMPCompliant.md) | No type description provided<br/>Class with 2 occurences.| 
| [SudoknFiberOpticLaserCuttingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFiberOpticLaserCuttingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknFillingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFillingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknFixturingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFixturingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknFlameSprayingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFlameSprayingCapability.md) | No type description provided<br/>Class with 6 occurences.| 
| [SudoknGeospatialLocation](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGeospatialLocation.md) | No type description provided<br/>Class with 20728 occurences.| 
| [SudoknGoldProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGoldProcessingCapability.md) | No type description provided<br/>Class with 1302 occurences.| 
| [SudoknGovermentIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGovermentIndustry.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknGraphiteProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGraphiteProcessingCapability.md) | No type description provided<br/>Class with 472 occurences.| 
| [SudoknHarperizingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHarperizingCapability.md) | No type description provided<br/>Class with 2 occurences.| 
| [SudoknHastelloyProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHastelloyProcessingCapability.md) | No type description provided<br/>Class with 321 occurences.| 
| [SudoknHealthcareServicesIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHealthcareServicesIndustry.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknHealthCareServicesIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHealthCareServicesIndustry.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknHighGradeAluminumProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHighGradeAluminumProcessingCapability.md) | No type description provided<br/>Class with 5 occurences.| 
| [SudoknHotDipGalvanizingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHotDipGalvanizingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknIATF16949Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknIATF16949Certificate.md) | No type description provided<br/>Class with 330 occurences.| 
| [SudoknInconelProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknInconelProcessingCapability.md) | No type description provided<br/>Class with 906 occurences.| 
| [SudoknInductionHeatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknInductionHeatingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknIndustrialMachineryandEquipmentIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknIndustrialMachineryandEquipmentIndustry.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknIndustry.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknInstallationCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknInstallationCapability.md) | No type description provided<br/>Class with 2 occurences.| 
| [SudoknInvarProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknInvarProcessingCapability.md) | No type description provided<br/>Class with 219 occurences.| 
| [SudoknInvestmentCastingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknInvestmentCastingCapability.md) | No type description provided<br/>Class with 83 occurences.| 
| [SudoknIS-TS16949](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknIS-TS16949.md) | No type description provided<br/>Class with 6 occurences.| 
| [SudoknISO13485](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknISO13485.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknISO14001](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknISO14001.md) | No type description provided<br/>Class with 7 occurences.| 
| [SudoknISO9000](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknISO9000.md) | No type description provided<br/>Class with 31 occurences.| 
| [SudoknISO9001](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknISO9001.md) | No type description provided<br/>Class with 82 occurences.| 
| [SudoknISTS16949Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknISTS16949Certificate.md) | No type description provided<br/>Class with 4 occurences.| 
| [SudoknITARCompliant](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknITARCompliant.md) | No type description provided<br/>Class with 8 occurences.| 
| [SudoknKaptonProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknKaptonProcessingCapability.md) | No type description provided<br/>Class with 32 occurences.| 
| [SudoknKnurlingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknKnurlingCapability.md) | No type description provided<br/>Class with 64 occurences.| 
| [SudoknKOSHERApproved](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknKOSHERApproved.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknKovarProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknKovarProcessingCapability.md) | No type description provided<br/>Class with 197 occurences.| 
| [SudoknLaserEtchingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknLaserEtchingCapability.md) | No type description provided<br/>Class with 81 occurences.| 
| [SudoknLaserProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknLaserProcessingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknLaserWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknLaserWeldingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknLatheWorkCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknLatheWorkCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknLeadProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknLeadProcessingCapability.md) | No type description provided<br/>Class with 2484 occurences.| 
| [SudoknLEEDCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknLEEDCertificate.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknLexanProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknLexanProcessingCapability.md) | No type description provided<br/>Class with 461 occurences.| 
| [SudoknLiquidCoatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknLiquidCoatingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknLiveToolingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknLiveToolingCapability.md) | No type description provided<br/>Class with 287 occurences.| 
| [SudoknLowAlloySteelProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknLowAlloySteelProcessingCapability.md) | No type description provided<br/>Class with 120 occurences.| 
| [SudoknMachineBuildingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMachineBuildingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknMagnesiumProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMagnesiumProcessingCapability.md) | No type description provided<br/>Class with 419 occurences.| 
| [SudoknMechanicalAssemblyCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMechanicalAssemblyCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknMediaBlastingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMediaBlastingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknMetalFabricationCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMetalFabricationCapability.md) | No type description provided<br/>Class with 6 occurences.| 
| [SudoknMetalProductionIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMetalProductionIndustry.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknMetalSpinningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMetalSpinningCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknMetalsProductsIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMetalsProductsIndustry.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknMetalStampingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMetalStampingCapability.md) | No type description provided<br/>Class with 2 occurences.| 
| [SudoknMetalworkingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMetalworkingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknMIGWeldinCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMIGWeldinCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknMigWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMigWeldingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknMolybdenumProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMolybdenumProcessingCapability.md) | No type description provided<br/>Class with 382 occurences.| 
| [SudoknNADCAPAC7004](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNADCAPAC7004.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332111](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332111.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332112](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332112.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332114](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332114.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332115](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332115.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332116](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332116.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332117](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332117.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332211](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332211.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332212](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332212.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332213](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332213.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332214](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332214.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332311](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332311.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332312](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332312.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332313](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332313.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332321](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332321.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332322](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332322.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332323](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332323.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332410](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332410.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332420](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332420.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332431](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332431.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332439](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332439.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332510](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332510.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332611](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332611.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332612](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332612.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332618](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332618.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332710](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332710.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332721](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332721.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332722](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332722.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332811](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332811.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332812](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332812.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332813](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332813.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332911](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332911.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332912](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332912.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332913](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332913.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332919](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332919.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332991](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332991.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332992](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332992.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332994](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332994.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332995](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332995.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332996](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332996.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332997](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332997.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332998](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332998.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNAICS332999](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332999.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNickelPlatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNickelPlatingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknNickelProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNickelProcessingCapability.md) | No type description provided<br/>Class with 1603 occurences.| 
| [SudoknNomexProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNomexProcessingCapability.md) | No type description provided<br/>Class with 58 occurences.| 
| [SudoknNotchingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNotchingCapability.md) | No type description provided<br/>Class with 109 occurences.| 
| [SudoknNylonProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNylonProcessingCapability.md) | No type description provided<br/>Class with 1177 occurences.| 
| [SudoknOilAndGasIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknOilAndGasIndustry.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknOilGroovingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknOilGroovingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknOxy-FuelCuttingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknOxy-FuelCuttingCapability.md) | No type description provided<br/>Class with 27 occurences.| 
| [SudoknPackagingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPackagingCapability.md) | No type description provided<br/>Class with 3 occurences.| 
| [SudoknPaintingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPaintingCapability.md) | No type description provided<br/>Class with 3 occurences.| 
| [SudoknPalladiumProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPalladiumProcessingCapability.md) | No type description provided<br/>Class with 78 occurences.| 
| [SudoknPaperandPaperboardProductsIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPaperandPaperboardProductsIndustry.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknPassivationCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPassivationCapability.md) | No type description provided<br/>Class with 280 occurences.| 
| [SudoknPemInsertionCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPemInsertionCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknPermanentMoldCastingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPermanentMoldCastingCapability.md) | No type description provided<br/>Class with 10 occurences.| 
| [SudoknPhosBronzeProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPhosBronzeProcessingCapability.md) | No type description provided<br/>Class with 12 occurences.| 
| [SudoknPhosphorBronzeProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPhosphorBronzeProcessingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknPipingFabricationCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPipingFabricationCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknPlasmaSprayingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPlasmaSprayingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknPlasterMoldCastingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPlasterMoldCastingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknPlasticMachiningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPlasticMachiningCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknPlasticsandRubberProductsIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPlasticsandRubberProductsIndustry.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknPlatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPlatingCapability.md) | No type description provided<br/>Class with 2 occurences.| 
| [SudoknPlatinumProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPlatinumProcessingCapability.md) | No type description provided<br/>Class with 225 occurences.| 
| [SudoknPolishingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPolishingCapability.md) | No type description provided<br/>Class with 456 occurences.| 
| [SudoknPolycarbonateProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPolycarbonateProcessingCapability.md) | No type description provided<br/>Class with 693 occurences.| 
| [SudoknPolycrystallineDiamondMachiningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPolycrystallineDiamondMachiningCapability.md) | No type description provided<br/>Class with 70 occurences.| 
| [SudoknPreciousMaterialProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPreciousMaterialProcessingCapability.md) | No type description provided<br/>Class with 6 occurences.| 
| [SudoknPressBrakingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPressBrakingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknPressingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPressingCapability.md) | No type description provided<br/>Class with 6 occurences.| 
| [SudoknProductDesignCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknProductDesignCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknProfessionalServicesIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknProfessionalServicesIndustry.md) | No type description provided<br/>Class with 2 occurences.| 
| [SudoknPrototypeManufacturingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPrototypeManufacturingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknPrototypingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPrototypingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknPulsedElectrochemicalMachiningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPulsedElectrochemicalMachiningCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknQS9000](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknQS9000.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknRamEDMCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknRamEDMCapability.md) | No type description provided<br/>Class with 28 occurences.| 
| [SudoknRAMEdmCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknRAMEdmCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknRapidPrototypingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknRapidPrototypingCapability.md) | No type description provided<br/>Class with 256 occurences.| 
| [SudoknResistanceWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknResistanceWeldingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknRetailTradeIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknRetailTradeIndustry.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknRivettingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknRivettingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknRoboticWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknRoboticWeldingCapability.md) | No type description provided<br/>Class with 2 occurences.| 
| [SudoknSandCastingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSandCastingCapability.md) | No type description provided<br/>Class with 4 occurences.| 
| [SudoknSanitaryWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSanitaryWeldingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknScreenPrintingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknScreenPrintingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknSewingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSewingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknShearingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknShearingCapability.md) | No type description provided<br/>Class with 13 occurences.| 
| [SudoknSheetMetalFabricationCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSheetMetalFabricationCapability.md) | No type description provided<br/>Class with 5 occurences.| 
| [SudoknSheetMetalFormingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSheetMetalFormingCapability.md) | No type description provided<br/>Class with 2 occurences.| 
| [SudoknShellMoldCastingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknShellMoldCastingCapability.md) | No type description provided<br/>Class with 2 occurences.| 
| [SudoknShrinkFittingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknShrinkFittingCapability.md) | No type description provided<br/>Class with 9 occurences.| 
| [SudoknSilkScreeningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSilkScreeningCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknSilverProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSilverProcessingCapability.md) | No type description provided<br/>Class with 1251 occurences.| 
| [SudoknSinkerEdmCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSinkerEdmCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknSinteringCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSinteringCapability.md) | No type description provided<br/>Class with 56 occurences.| 
| [SudoknSmeltingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSmeltingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknSpecialMaterialsProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSpecialMaterialsProcessingCapability.md) | No type description provided<br/>Class with 71 occurences.| 
| [SudoknSportsandLeisureIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSportsandLeisureIndustry.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknSteelAlloyProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSteelAlloyProcessingCapability.md) | No type description provided<br/>Class with 365 occurences.| 
| [SudoknSteelManufacturingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSteelManufacturingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknSurfaceFinishingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSurfaceFinishingCapability.md) | No type description provided<br/>Class with 76 occurences.| 
| [SudoknSurfaceGrindingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSurfaceGrindingCapability.md) | No type description provided<br/>Class with 2 occurences.| 
| [SudoknSwissMachiningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSwissMachiningCapability.md) | No type description provided<br/>Class with 19 occurences.| 
| [SudoknSwissTurningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSwissTurningCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknTantalumProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTantalumProcessingCapability.md) | No type description provided<br/>Class with 234 occurences.| 
| [SudoknTeflonProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTeflonProcessingCapability.md) | No type description provided<br/>Class with 538 occurences.| 
| [SudoknTextiles](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTextiles.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknThermoformingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknThermoformingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknTI9000Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTI9000Certificate.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknTinProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTinProcessingCapability.md) | No type description provided<br/>Class with 417 occurences.| 
| [SudoknTubeBendingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTubeBendingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknTubeFormingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTubeFormingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknTubingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTubingCapability.md) | No type description provided<br/>Class with 533 occurences.| 
| [SudoknTungstenProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTungstenProcessingCapability.md) | No type description provided<br/>Class with 820 occurences.| 
| [SudoknTurretPunchingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTurretPunchingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknUSPostalCode](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknUSPostalCode.md) | No type description provided<br/>Class with 20424 occurences.| 
| [SudoknVacuumCastingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknVacuumCastingCapability.md) | No type description provided<br/>Class with 16 occurences.| 
| [SudoknVacuumFormingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknVacuumFormingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknVacuumPackagingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknVacuumPackagingCapability.md) | No type description provided<br/>Class with 2 occurences.| 
| [SudoknWarehousingAndStorageIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWarehousingAndStorageIndustry.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknWaspaloyProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWaspaloyProcessingCapability.md) | No type description provided<br/>Class with 66 occurences.| 
| [SudoknWaterandSewerUtilitiesIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWaterandSewerUtilitiesIndustry.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknWaterjetCuttimgCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWaterjetCuttimgCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknWaterjetCuttingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWaterjetCuttingCapability.md) | No type description provided<br/>Class with 373 occurences.| 
| [SudoknWaterJetCuttingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWaterJetCuttingCapability.md) | No type description provided<br/>Class with 2 occurences.| 
| [SudoknWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWeldingCapability.md) | No type description provided<br/>Class with 2700 occurences.| 
| [SudoknWireFormingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWireFormingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknWiringCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWiringCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknWoodProductManufacturingIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWoodProductManufacturingIndustry.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknWoodworkingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWoodworkingCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknZincArcSprayCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknZincArcSprayCapability.md) | No type description provided<br/>Class with 1 occurences.| 
| [SudoknZincProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknZincProcessingCapability.md) | No type description provided<br/>Class with 1266 occurences.| 
| [SudoknZirconProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknZirconProcessingCapability.md) | No type description provided<br/>Class with 240 occurences.| 





## Slots

| Slot | Description |
| --- | --- |
| [https___spec.industrialontologies.org_ontology_core_meta_AnnotationVocabulary_replacedBy](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/https___spec.industrialontologies.org_ontology_core_meta_AnnotationVocabulary_replacedBy.md) | No slot description provided<br/>|
| [iosc_hasTextValue](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/iosc_hasTextValue.md) | No slot description provided<br/>19102 occurrences with subject type sudokn_PostalAddress and object type string.|
| [rdfs_label](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/rdfs_label.md) | No slot description provided<br/>2994 occurrences with subject type sudokn_City and object type string.<br/>1 occurrences with subject type sudokn_Industry and object type string.<br/>1754 occurrences with subject type sudokn_BronzeProcessingCapability and object type string.<br/>2866 occurrences with subject type sudokn_GlassProcessingCapability and object type string.<br/>472 occurrences with subject type sudokn_GraphiteProcessingCapability and object type string.<br/>5903 occurrences with subject type sudokn_IronProcessingCapability and object type string.<br/>1830 occurrences with subject type sudokn_RubberProcessingCapability and object type string.<br/>4795 occurrences with subject type sudokn_StainlessSteelProcessingCapability and object type string.<br/>7200 occurrences with subject type sudokn_SteelProcessingCapability and object type string.<br/>1065 occurrences with subject type sudokn_FoamProcessingCapability and object type string.<br/>3466 occurrences with subject type sudokn_ISO9001Certificate and object type string.<br/>4159 occurrences with subject type sudokn_PlasticProcessingCapability and object type string.<br/>1427 occurrences with subject type sudokn_CNCMachiningCapability and object type string.<br/>2784 occurrences with subject type sudokn_CopperProcessingCapability and object type string.<br/>2518 occurrences with subject type sudokn_FabricatingCapability and object type string.<br/>1614 occurrences with subject type sudokn_FinishingCapability and object type string.<br/>1802 occurrences with subject type sudokn_FormingCapability and object type string.<br/>3508 occurrences with subject type sudokn_MachiningCapability and object type string.<br/>6560 occurrences with subject type sudokn_MetalProcessingCapability and object type string.<br/>2918 occurrences with subject type sudokn_WoodProcessingCapability and object type string.<br/>2931 occurrences with subject type sudokn_AssemblyCapability and object type string.<br/>1449 occurrences with subject type sudokn_DrawingCapability and object type string.<br/>1114 occurrences with subject type sudokn_EDMCapability and object type string.<br/>330 occurrences with subject type sudokn_IATF16949Certificate and object type string.<br/>581 occurrences with subject type sudokn_LaserCuttingCapability and object type string.<br/>1216 occurrences with subject type sudokn_StampingCapability and object type string.<br/>2700 occurrences with subject type sudokn_WeldingCapability and object type string.<br/>644 occurrences with subject type sudokn_WireEDMCapability and object type string.<br/>129 occurrences with subject type sudokn_State and object type string.<br/>5646 occurrences with subject type sudokn_AluminumProcessingCapability and object type string.<br/>2484 occurrences with subject type sudokn_LeadProcessingCapability and object type string.<br/>1039 occurrences with subject type sudokn_UrethaneProcessingCapability and object type string.<br/>1219 occurrences with subject type sudokn_AS9100Certificate and object type string.<br/>1051 occurrences with subject type sudokn_CeramicProcessingCapability and object type string.<br/>289 occurrences with subject type sudokn_DelrinProcessingCapability and object type string.<br/>1177 occurrences with subject type sudokn_NylonProcessingCapability and object type string.<br/>693 occurrences with subject type sudokn_PolycarbonateProcessingCapability and object type string.<br/>538 occurrences with subject type sudokn_TeflonProcessingCapability and object type string.<br/>1266 occurrences with subject type sudokn_ZincProcessingCapability and object type string.<br/>825 occurrences with subject type sudokn_AlloySteelProcessingCapability and object type string.<br/>945 occurrences with subject type sudokn_BendingCapability and object type string.<br/>857 occurrences with subject type sudokn_BoringCapability and object type string.<br/>1195 occurrences with subject type sudokn_CastingCapability and object type string.<br/>197 occurrences with subject type sudokn_ElectricalDischargeMachiningCapability and object type string.<br/>2311 occurrences with subject type sudokn_MillingCapability and object type string.<br/>1765 occurrences with subject type sudokn_PackingCapability and object type string.<br/>690 occurrences with subject type sudokn_SiliconeProcessingCapability and object type string.<br/>365 occurrences with subject type sudokn_SteelAlloyProcessingCapability and object type string.<br/>533 occurrences with subject type sudokn_TubingCapability and object type string.<br/>373 occurrences with subject type sudokn_WaterjetCuttingCapability and object type string.<br/>659 occurrences with subject type sudokn_AnodizingCapability and object type string.<br/>1105 occurrences with subject type sudokn_CNCMillingCapability and object type string.<br/>1196 occurrences with subject type sudokn_CompositeProcessingCapability and object type string.<br/>1361 occurrences with subject type sudokn_DrillingCapability and object type string.<br/>1339 occurrences with subject type sudokn_ElectroPlatingCapability and object type string.<br/>487 occurrences with subject type sudokn_EtchingCapability and object type string.<br/>1654 occurrences with subject type sudokn_GrindingCapability and object type string.<br/>225 occurrences with subject type sudokn_PlatinumProcessingCapability and object type string.<br/>2077 occurrences with subject type sudokn_TurningCapability and object type string.<br/>209 occurrences with subject type sudokn_AdditiveManufacturingCapability and object type string.<br/>337 occurrences with subject type sudokn_AddtiveManufacturingCapability and object type string.<br/>1344 occurrences with subject type sudokn_ChemicalsProcessingCapability and object type string.<br/>303 occurrences with subject type sudokn_CobaltProcessingCapability and object type string.<br/>220 occurrences with subject type sudokn_DieCastingCapability and object type string.<br/>602 occurrences with subject type sudokn_ExtrudingCapability and object type string.<br/>326 occurrences with subject type sudokn_ISO13485Certificate and object type string.<br/>83 occurrences with subject type sudokn_InvestmentCastingCapability and object type string.<br/>1603 occurrences with subject type sudokn_NickelProcessingCapability and object type string.<br/>278 occurrences with subject type sudokn_ReamingCapability and object type string.<br/>504 occurrences with subject type sudokn_ShapingCapability and object type string.<br/>28 occurrences with subject type sudokn_SheetMetalProcessingCapability and object type string.<br/>56 occurrences with subject type sudokn_SinteringCapability and object type string.<br/>16 occurrences with subject type sudokn_VacuumCastingCapability and object type string.<br/>906 occurrences with subject type sudokn_InconelProcessingCapability and object type string.<br/>256 occurrences with subject type sudokn_RapidPrototypingCapability and object type string.<br/>1349 occurrences with subject type sudokn_TitaniumProcessingCapability and object type string.<br/>820 occurrences with subject type sudokn_TungstenProcessingCapability and object type string.<br/>362 occurrences with subject type sudokn_AcetalProcessingCapability and object type string.<br/>360 occurrences with subject type sudokn_BerylliumProcessingCapability and object type string.<br/>228 occurrences with subject type sudokn_BlackOxideCoatingCapability and object type string.<br/>2596 occurrences with subject type sudokn_BrassProcessingCapability and object type string.<br/>17 occurrences with subject type sudokn_CentrifugalCastingCapability and object type string.<br/>69 occurrences with subject type sudokn_EmbossingCapability and object type string.<br/>72 occurrences with subject type sudokn_GalvanizingCapability and object type string.<br/>461 occurrences with subject type sudokn_LexanProcessingCapability and object type string.<br/>382 occurrences with subject type sudokn_MolybdenumProcessingCapability and object type string.<br/>10 occurrences with subject type sudokn_PermanentMoldCastingCapability and object type string.<br/>1744 occurrences with subject type sudokn_CoatingCapability and object type string.<br/>679 occurrences with subject type sudokn_PowderCoatingCapability and object type string.<br/>550 occurrences with subject type sudokn_SurfacePreparationCapability and object type string.<br/>1251 occurrences with subject type sudokn_SilverProcessingCapability and object type string.<br/>437 occurrences with subject type sudokn_VerticalMillingCapability and object type string.<br/>923 occurrences with subject type sudokn_HeatTreatingCapability and object type string.<br/>786 occurrences with subject type sudokn_CarbideProcessingCapability and object type string.<br/>127 occurrences with subject type sudokn_ITARCertificate and object type string.<br/>1302 occurrences with subject type sudokn_GoldProcessingCapability and object type string.<br/>609 occurrences with subject type sudokn_ForgingCapability and object type string.<br/>644 occurrences with subject type sudokn_MoldingCapability and object type string.<br/>287 occurrences with subject type sudokn_LiveToolingCapability and object type string.<br/>109 occurrences with subject type sudokn_NotchingCapability and object type string.<br/>605 occurrences with subject type sudokn_RollingCapability and object type string.<br/>417 occurrences with subject type sudokn_TinProcessingCapability and object type string.<br/>81 occurrences with subject type sudokn_LaserEtchingCapability and object type string.<br/>121 occurrences with subject type sudokn_FabricationCapability and object type string.<br/>235 occurrences with subject type sudokn_PlasmaCuttingCapability and object type string.<br/>340 occurrences with subject type sudokn_SandBlastingCapability and object type string.<br/>551 occurrences with subject type sudokn_ChromiumProcessingCapability and object type string.<br/>460 occurrences with subject type sudokn_HoningCapability and object type string.<br/>219 occurrences with subject type sudokn_InvarProcessingCapability and object type string.<br/>197 occurrences with subject type sudokn_KovarProcessingCapability and object type string.<br/>419 occurrences with subject type sudokn_MagnesiumProcessingCapability and object type string.<br/>148 occurrences with subject type sudokn_SinkerEDMCapability and object type string.<br/>234 occurrences with subject type sudokn_TantalumProcessingCapability and object type string.<br/>860 occurrences with subject type sudokn_TappingCapability and object type string.<br/>66 occurrences with subject type sudokn_WaspaloyProcessingCapability and object type string.<br/>456 occurrences with subject type sudokn_PolishingCapability and object type string.<br/>64 occurrences with subject type sudokn_KnurlingCapability and object type string.<br/>9 occurrences with subject type sudokn_AbrasiveCleaningCapability and object type string.<br/>194 occurrences with subject type sudokn_ChemicalProcessingCapability and object type string.<br/>437 occurrences with subject type sudokn_JoiningCapability and object type string.<br/>467 occurrences with subject type sudokn_NADCAPCertificate and object type string.<br/>280 occurrences with subject type sudokn_PassivationCapability and object type string.<br/>76 occurrences with subject type sudokn_SurfaceFinishingCapability and object type string.<br/>321 occurrences with subject type sudokn_ISO14001Certificate and object type string.<br/>804 occurrences with subject type sudokn_ASMECertificate and object type string.<br/>181 occurrences with subject type sudokn_HorizontalMillingCapability and object type string.<br/>70 occurrences with subject type sudokn_PolycrystallineDiamondMachiningCapability and object type string.<br/>321 occurrences with subject type sudokn_HastelloyProcessingCapability and object type string.<br/>317 occurrences with subject type sudokn_ExoticMaterialProcessingCapability and object type string.<br/>78 occurrences with subject type sudokn_PalladiumProcessingCapability and object type string.<br/>31 occurrences with subject type sudokn_ISO9000 and object type string.<br/>147 occurrences with subject type sudokn_BrazingCapability and object type string.<br/>28 occurrences with subject type sudokn_RamEDMCapability and object type string.<br/>80 occurrences with subject type sudokn_ZincAlloyProcessingCapability and object type string.<br/>269 occurrences with subject type sudokn_HardeningCapability and object type string.<br/>81 occurrences with subject type sudokn_DeepHoleDrillingCapability and object type string.<br/>99 occurrences with subject type sudokn_AnnealingCapability and object type string.<br/>12 occurrences with subject type sudokn_ISO14000Certificate and object type string.<br/>271 occurrences with subject type sudokn_SolderingCapability and object type string.<br/>240 occurrences with subject type sudokn_ZirconProcessingCapability and object type string.<br/>71 occurrences with subject type sudokn_SpecialMaterialsProcessingCapability and object type string.<br/>86 occurrences with subject type sudokn_DeburringCapability and object type string.<br/>81 occurrences with subject type sudokn_CarburizingCapability and object type string.<br/>8 occurrences with subject type sudokn_CreepFeedGrindingCapability and object type string.<br/>120 occurrences with subject type sudokn_LowAlloySteelProcessingCapability and object type string.<br/>139 occurrences with subject type sudokn_ChromateConversionCoatingCapability and object type string.<br/>10 occurrences with subject type sudokn_PhysicalVaporDepositionCapability and object type string.<br/>252 occurrences with subject type sudokn_ColdRolledSteelProcessingCapability and object type string.<br/>214 occurrences with subject type sudokn_ElectrolessNickelPlatingCapability and object type string.<br/>45 occurrences with subject type sudokn_NitridingCapability and object type string.<br/>5 occurrences with subject type sudokn_FDACertificate and object type string.<br/>58 occurrences with subject type sudokn_NomexProcessingCapability and object type string.<br/>38 occurrences with subject type sudokn_SpinningCapability and object type string.<br/>61 occurrences with subject type sudokn_ElectropolishingCapability and object type string.<br/>67 occurrences with subject type sudokn_ISOCertificate and object type string.<br/>23 occurrences with subject type sudokn_WireHarnessAssemblyCapability and object type string.<br/>13 occurrences with subject type sudokn_VaporizedMetalCoatingCapability and object type string.<br/>48 occurrences with subject type sudokn_AWSWelderCertificate and object type string.<br/>5 occurrences with subject type sudokn_AS9000Certificate and object type string.<br/>28 occurrences with subject type sudokn_DifficultToMachineMaterialsProcessingCapability and object type string.<br/>44836 occurrences with subject type io_MaterialProduct and object type string.<br/>41 occurrences with subject type sudokn_QS9000Certificate and object type string.<br/>27 occurrences with subject type sudokn_Oxy-FuelCuttingCapability and object type string.<br/>1 occurrences with subject type sudokn_LaserProcessingCapability and object type string.<br/>32 occurrences with subject type sudokn_KaptonProcessingCapability and object type string.<br/>5 occurrences with subject type sudokn_HighGradeAluminumProcessingCapability and object type string.<br/>6 occurrences with subject type sudokn_PreciousMaterialProcessingCapability and object type string.<br/>17 occurrences with subject type sudokn_PlaningCapability and object type string.<br/>1 occurrences with subject type sudokn_PlasmaSprayingCapability and object type string.<br/>19 occurrences with subject type sudokn_CuttingCapability and object type string.<br/>12 occurrences with subject type sudokn_ExtremelyHardMaterialProcessingCapability and object type string.<br/>6 occurrences with subject type sudokn_FlameSprayingCapability and object type string.<br/>16 occurrences with subject type sudokn_CNCTurningCapability and object type string.<br/>6 occurrences with subject type sudokn_ElectronBeamWeldingCapability and object type string.<br/>82 occurrences with subject type sudokn_ISO9001 and object type string.<br/>1 occurrences with subject type sudokn_ScreenPrintingCapability and object type string.<br/>1 occurrences with subject type sudokn_WetPaintingCapability and object type string.<br/>20 occurrences with subject type sudokn_AS9100 and object type string.<br/>8 occurrences with subject type sudokn_ITARCompliant and object type string.<br/>1 occurrences with subject type sudokn_AerospaceIndustry and object type string.<br/>2 occurrences with subject type sudokn_AgricultureIndustry and object type string.<br/>28 occurrences with subject type sudokn_EngineeringDesignCapability and object type string.<br/>1 occurrences with subject type sudokn_ElectolessNickelPlatingCapability and object type string.<br/>1 occurrences with subject type sudokn_NickelPlatingCapability and object type string.<br/>2 occurrences with subject type sudokn_PlatingCapability and object type string.<br/>6 occurrences with subject type sudokn_DieMakingCapability and object type string.<br/>8 occurrences with subject type sudokn_MoldMakingCapability and object type string.<br/>2 occurrences with subject type sudokn_RivetingCapability and object type string.<br/>6 occurrences with subject type sudokn_ToolMakingCapability and object type string.<br/>1 occurrences with subject type sudokn_PLCProgrammingCapability and object type string.<br/>1 occurrences with subject type sudokn_ContinuousCastingCapability and object type string.<br/>7 occurrences with subject type sudokn_PunchingCapability and object type string.<br/>1 occurrences with subject type sudokn_SmeltingCapability and object type string.<br/>10 occurrences with subject type sudokn_ASME and object type string.<br/>1 occurrences with subject type sudokn_DeepFreezingCapability and object type string.<br/>1 occurrences with subject type sudokn_VacuumHardeningCapability and object type string.<br/>7 occurrences with subject type sudokn_ISO14001 and object type string.<br/>13 occurrences with subject type sudokn_ShearingCapability and object type string.<br/>2 occurrences with subject type sudokn_AutomotiveIndustry and object type string.<br/>1 occurrences with subject type sudokn_PrototypingCapability and object type string.<br/>12 occurrences with subject type sudokn_WoodWorkingCapability and object type string.<br/>15 occurrences with subject type sudokn_NaturalFiberProcessingCapability and object type string.<br/>43 occurrences with subject type sudokn_CarbonitridingCapability and object type string.<br/>9 occurrences with subject type sudokn_ShrinkFittingCapability and object type string.<br/>3 occurrences with subject type sudokn_MechanicalJoiningCapability and object type string.<br/>1 occurrences with subject type sudokn_OilGroovingCapability and object type string.<br/>1 occurrences with subject type sudokn_PressBrakingCapability and object type string.<br/>2 occurrences with subject type sudokn_RoboticWeldingCapability and object type string.<br/>2 occurrences with subject type sudokn_GearCuttingCapability and object type string.<br/>6 occurrences with subject type sudokn_MetalFabricationCapability and object type string.<br/>2 occurrences with subject type sudokn_BusinessEquipmentIndustry and object type string.<br/>12 occurrences with subject type sudokn_PhosBronzeProcessingCapability and object type string.<br/>13 occurrences with subject type sudokn_CarbonGraphiteProcessingCapability and object type string.<br/>1 occurrences with subject type sudokn_CNCmillingCapability and object type string.<br/>5 occurrences with subject type sudokn_SheetMetalFabricationCapability and object type string.<br/>2 occurrences with subject type sudokn_HAACPCertificate and object type string.<br/>9 occurrences with subject type sudokn_AS9102Certificate and object type string.<br/>2 occurrences with subject type sudokn_ManMadeFiberProcessingCapability and object type string.<br/>1 occurrences with subject type sudokn_PrintingCapability and object type string.<br/>1 occurrences with subject type sudokn_LatheWorkCapability and object type string.<br/>1 occurrences with subject type sudokn_MechanicalAssemblyCapability and object type string.<br/>1 occurrences with subject type sudokn_BrassBlackeningCapability and object type string.<br/>1 occurrences with subject type sudokn_MetalSpinningCapability and object type string.<br/>1 occurrences with subject type sudokn_KnittingCapability and object type string.<br/>2 occurrences with subject type sudokn_CommunicationIndustry and object type string.<br/>1 occurrences with subject type sudokn_CommunicationandElectronicPowerUtilitiesIndustry and object type string.<br/>1 occurrences with subject type sudokn_2-AxisCNCTurningCapability and object type string.<br/>3 occurrences with subject type sudokn_TIGWeldingCapability and object type string.<br/>1 occurrences with subject type sudokn_ComputersandElectronicProductsIndustry and object type string.<br/>2 occurrences with subject type sudokn_ConstructionIndustry and object type string.<br/>1 occurrences with subject type sudokn_ConsumerGoodsIndustry and object type string.<br/>1 occurrences with subject type sudokn_BritishRetailConsortiumAccreditation and object type string.<br/>1 occurrences with subject type sudokn_CNCPlasmaCuttingCapability and object type string.<br/>3 occurrences with subject type sudokn_BABACertificate and object type string.<br/>6 occurrences with subject type sudokn_PressingCapability and object type string.<br/>1 occurrences with subject type sudokn_VacuumFormingCapability and object type string.<br/>19 occurrences with subject type sudokn_SwissMachiningCapability and object type string.<br/>1 occurrences with subject type sudokn_ThermoformingCapability and object type string.<br/>1 occurrences with subject type sudokn_ISO13485 and object type string.<br/>2 occurrences with subject type sudokn_ShellMoldCastingCapability and object type string.<br/>1 occurrences with subject type sudokn_EducationalInstitutionsIndustry and object type string.<br/>1 occurrences with subject type sudokn_ElectricVehiclesIndustry and object type string.<br/>2 occurrences with subject type sudokn_InstallationCapability and object type string.<br/>6 occurrences with subject type sudokn_IS-TS16949 and object type string.<br/>4 occurrences with subject type sudokn_ISTS16949Certificate and object type string.<br/>2 occurrences with subject type sudokn_KittingCapability and object type string.<br/>1 occurrences with subject type sudokn_CNCPressBrakeCapability and object type string.<br/>2 occurrences with subject type sudokn_FoodIndustry and object type string.<br/>1 occurrences with subject type sudokn_SteelManufacturingCapability and object type string.<br/>1 occurrences with subject type sudokn_TurretPunchingCapability and object type string.<br/>2 occurrences with subject type sudokn_FurnitureIndustry and object type string.<br/>4 occurrences with subject type sudokn_SandCastingCapability and object type string.<br/>1 occurrences with subject type sudokn_QS9000 and object type string.<br/>1 occurrences with subject type sudokn_CenterlessGrindingCapability and object type string.<br/>2 occurrences with subject type sudokn_GovernmentIndustry and object type string.<br/>3 occurrences with subject type sudokn_PaintingCapability and object type string.<br/>1 occurrences with subject type sudokn_WiringCapability and object type string.<br/>1 occurrences with subject type sudokn_PlasterMoldCastingCapability and object type string.<br/>1 occurrences with subject type sudokn_FasteningCapability and object type string.<br/>1 occurrences with subject type sudokn_HealthCareServicesIndustry and object type string.<br/>2 occurrences with subject type sudokn_MetalStampingCapability and object type string.<br/>1 occurrences with subject type sudokn_SinkerEdmCapability and object type string.<br/>1 occurrences with subject type sudokn_FillingCapability and object type string.<br/>3 occurrences with subject type sudokn_PackagingCapability and object type string.<br/>1 occurrences with subject type sudokn_CNCCylindricalGrindingCapability and object type string.<br/>1 occurrences with subject type sudokn_EndFormingCapability and object type string.<br/>1 occurrences with subject type sudokn_IndustrialMachineryandEquipmentIndustry and object type string.<br/>2 occurrences with subject type sudokn_FDAGMPCompliant and object type string.<br/>1 occurrences with subject type sudokn_DigitalPrintingCapability and object type string.<br/>1 occurrences with subject type sudokn_SwissTurningCapability and object type string.<br/>1 occurrences with subject type sudokn_PipingFabricationCapability and object type string.<br/>2 occurrences with subject type sudokn_HarperizingCapability and object type string.<br/>1 occurrences with subject type sudokn_BroachingCapability and object type string.<br/>2 occurrences with subject type sudokn_WaterJetCuttingCapability and object type string.<br/>1 occurrences with subject type sudokn_PrototypeManufacturingCapability and object type string.<br/>1 occurrences with subject type sudokn_MIGWeldinCapability and object type string.<br/>3 occurrences with subject type sudokn_SpotWeldingCapability and object type string.<br/>2 occurrences with subject type sudokn_MIGWeldingCapability and object type string.<br/>3 occurrences with subject type sudokn_CADCapability and object type string.<br/>1 occurrences with subject type sudokn_PhosphorBronzeProcessingCapability and object type string.<br/>1 occurrences with subject type sudokn_LEEDCertificate and object type string.<br/>1 occurrences with subject type sudokn_CeramicMoldCastingCapability and object type string.<br/>1 occurrences with subject type sudokn_CNCBendingCapability and object type string.<br/>1 occurrences with subject type sudokn_WaterjetCuttimgCapability and object type string.<br/>1 occurrences with subject type sudokn_LiquidCoatingCapability and object type string.<br/>1 occurrences with subject type sudokn_MetalsProductsIndustry and object type string.<br/>2 occurrences with subject type sudokn_MilitaryIndustry and object type string.<br/>2 occurrences with subject type sudokn_MiningIndustry and object type string.<br/>4 occurrences with subject type sudokn_OwnershipStatusClassifier and object type string.<br/>2 occurrences with subject type sudokn_VacuumPackagingCapability and object type string.<br/>1 occurrences with subject type sudokn_ChemicalCoatingCapability and object type string.<br/>3 occurrences with subject type sudokn_OffshoreWindIndustry and object type string.<br/>1 occurrences with subject type sudokn_CNCCuttingCapability and object type string.<br/>1 occurrences with subject type sudokn_SewingCapability and object type string.<br/>1 occurrences with subject type sudokn_PaperandPaperboardProductsIndustry and object type string.<br/>2 occurrences with subject type sudokn_SheetMetalFormingCapability and object type string.<br/>1 occurrences with subject type sudokn_CNCFormingCapability and object type string.<br/>1 occurrences with subject type sudokn_ProductDesignCapability and object type string.<br/>1 occurrences with subject type sudokn_PlasticsandRubberProductsIndustry and object type string.<br/>1 occurrences with subject type sudokn_RivettingCapability and object type string.<br/>2 occurrences with subject type sudokn_ProfessionalServicesIndustry and object type string.<br/>1 occurrences with subject type sudokn_SilkScreeningCapability and object type string.<br/>2 occurrences with subject type sudokn_RecyclingIndustry and object type string.<br/>1 occurrences with subject type sudokn_CNCWireBendingCapability and object type string.<br/>3 occurrences with subject type sudokn_WireBendingCapability and object type string.<br/>1 occurrences with subject type sudokn_WireFormingCapability and object type string.<br/>1 occurrences with subject type sudokn_RetailTradeIndustry and object type string.<br/>2 occurrences with subject type sudokn_ReverseEngineeringCapability and object type string.<br/>1 occurrences with subject type sudokn_FixtureDesignCapability and object type string.<br/>1 occurrences with subject type sudokn_FixturingCapability and object type string.<br/>1 occurrences with subject type sudokn_PemInsertionCapability and object type string.<br/>1 occurrences with subject type sudokn_TI9000Certificate and object type string.<br/>1 occurrences with subject type sudokn_CNCGrindingCapability and object type string.<br/>1 occurrences with subject type sudokn_ExtrusionCapability and object type string.<br/>1 occurrences with subject type sudokn_KOSHERApproved and object type string.<br/>1 occurrences with subject type sudokn_SanitaryWeldingCapability and object type string.<br/>1 occurrences with subject type sudokn_SportsandLeisureIndustry and object type string.<br/>1 occurrences with subject type sudokn_CNCHorizontalTurningCapability and object type string.<br/>1 occurrences with subject type sudokn_CNCLaserCuttingCapability and object type string.<br/>1 occurrences with subject type sudokn_CNCVerticalMillingCapability and object type string.<br/>3 occurrences with subject type sudokn_ElectroplatingCapability and object type string.<br/>1 occurrences with subject type sudokn_NADCAPAC7004 and object type string.<br/>1 occurrences with subject type sudokn_TubeBendingCapability and object type string.<br/>1 occurrences with subject type sudokn_MediaBlastingCapability and object type string.<br/>1 occurrences with subject type sudokn_MigWeldingCapability and object type string.<br/>1 occurrences with subject type sudokn_ResistanceWeldingCapability and object type string.<br/>2 occurrences with subject type sudokn_TextilesIndustry and object type string.<br/>1 occurrences with subject type sudokn_InductionHeatingCapability and object type string.<br/>1 occurrences with subject type sudokn_PhosphateCoatingCapability and object type string.<br/>2 occurrences with subject type sudokn_TransportationIndustry and object type string.<br/>1 occurrences with subject type sudokn_CerakoteCoatingCapability and object type string.<br/>1 occurrences with subject type sudokn_TubeFormingCapability and object type string.<br/>2 occurrences with subject type sudokn_SurfaceGrindingCapability and object type string.<br/>1 occurrences with subject type sudokn_CylindricalGrindingCapability and object type string.<br/>1 occurrences with subject type sudokn_PulsedElectrochemicalMachiningCapability and object type string.<br/>1 occurrences with subject type sudokn_CNCLatheCapability and object type string.<br/>1 occurrences with subject type sudokn_WaterandSewerUtilitiesIndustry and object type string.<br/>1 occurrences with subject type sudokn_FiberOpticLaserCuttingCapability and object type string.<br/>1 occurrences with subject type sudokn_ZincArcSprayCapability and object type string.<br/>1 occurrences with subject type sudokn_PlasticMachiningCapability and object type string.<br/>1 occurrences with subject type sudokn_MachineBuildingCapability and object type string.<br/>1 occurrences with subject type sudokn_ChemicalCleaningCapability and object type string.<br/>1 occurrences with subject type sudokn_ElectrolessPlatingCapability and object type string.<br/>1 occurrences with subject type sudokn_HotDipGalvanizingCapability and object type string.<br/>1 occurrences with subject type sudokn_LaserWeldingCapability and object type string.<br/>1 occurrences with subject type sudokn_RAMEdmCapability and object type string.<br/>1 occurrences with subject type sudokn_CustomFoamCuttingCapability and object type string.<br/>1 occurrences with subject type sudokn_ApparelIndustry and object type string.<br/>1 occurrences with subject type sudokn_3DPrintingCapability and object type string.<br/>1 occurrences with subject type sudokn_AcrylicFabricationCapability and object type string.<br/>1 occurrences with subject type sudokn_MetalworkingCapability and object type string.<br/>1 occurrences with subject type sudokn_WoodworkingCapability and object type string.<br/>1 occurrences with subject type sudokn_ChemicalAndPetrochemicalIndustry and object type string.<br/>1 occurrences with subject type sudokn_ConsumerGoods and object type string.<br/>1 occurrences with subject type sudokn_EducationIndustry and object type string.<br/>1 occurrences with subject type sudokn_ElectronicAutomotiveInudstry and object type string.<br/>1 occurrences with subject type sudokn_ElectronicProductIndustry and object type string.<br/>1 occurrences with subject type sudokn_GovermentIndustry and object type string.<br/>1 occurrences with subject type sudokn_HealthcareServicesIndustry and object type string.<br/>1 occurrences with subject type sudokn_MachinaryAndEquipmentIndustry and object type string.<br/>1 occurrences with subject type sudokn_MetalProductionIndustry and object type string.<br/>1 occurrences with subject type sudokn_OilAndGasIndustry and object type string.<br/>1 occurrences with subject type sudokn_PaperIndustry and object type string.<br/>1 occurrences with subject type sudokn_PlasticAndRubberIndustry and object type string.<br/>1 occurrences with subject type sudokn_PrintingAndInformationIndustry and object type string.<br/>1 occurrences with subject type sudokn_RetailIndustry and object type string.<br/>1 occurrences with subject type sudokn_SportsAndLeisureIndustry and object type string.<br/>1 occurrences with subject type sudokn_Textiles and object type string.<br/>1 occurrences with subject type sudokn_UtilitiesIndustry and object type string.<br/>1 occurrences with subject type sudokn_WarehousingAndStorageIndustry and object type string.<br/>1 occurrences with subject type sudokn_WoodProductManufacturingIndustry and object type string.<br/>11813 occurrences with subject type io_Manufacturer and object type string.|
| [skos_altLabel](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/skos_altLabel.md) | No slot description provided<br/>1 occurrences with subject type sudokn_OwnershipStatusClassifier and object type string.|
| [sudokn_attestsTo](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_attestsTo.md) | No slot description provided<br/>1 occurrences with subject type sudokn_ISO9000Certificate and object type sudokn_QualityManagementCapability.<br/>1 occurrences with subject type sudokn_AS9100Certificate and object type sudokn_QualityManagementCapability.|
| [sudokn_hasAddressPart](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasAddressPart.md) | No slot description provided<br/>|
| [sudokn_hasCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasCertificate.md) | No slot description provided<br/>1 occurrences with subject type owl_NamedIndividual and object type sudokn_ISO9000Certificate.<br/>3466 occurrences with subject type io_Manufacturer and object type sudokn_ISO9001Certificate.<br/>330 occurrences with subject type io_Manufacturer and object type sudokn_IATF16949Certificate.<br/>1219 occurrences with subject type io_Manufacturer and object type sudokn_AS9100Certificate.<br/>326 occurrences with subject type io_Manufacturer and object type sudokn_ISO13485Certificate.<br/>127 occurrences with subject type io_Manufacturer and object type sudokn_ITARCertificate.<br/>467 occurrences with subject type io_Manufacturer and object type sudokn_NADCAPCertificate.<br/>321 occurrences with subject type io_Manufacturer and object type sudokn_ISO14001Certificate.<br/>804 occurrences with subject type io_Manufacturer and object type sudokn_ASMECertificate.<br/>31 occurrences with subject type io_Manufacturer and object type sudokn_ISO9000.<br/>12 occurrences with subject type io_Manufacturer and object type sudokn_ISO14000Certificate.<br/>5 occurrences with subject type io_Manufacturer and object type sudokn_FDACertificate.<br/>67 occurrences with subject type io_Manufacturer and object type sudokn_ISOCertificate.<br/>48 occurrences with subject type io_Manufacturer and object type sudokn_AWSWelderCertificate.<br/>5 occurrences with subject type io_Manufacturer and object type sudokn_AS9000Certificate.<br/>41 occurrences with subject type io_Manufacturer and object type sudokn_QS9000Certificate.<br/>82 occurrences with subject type io_Manufacturer and object type sudokn_ISO9001.<br/>20 occurrences with subject type io_Manufacturer and object type sudokn_AS9100.<br/>8 occurrences with subject type io_Manufacturer and object type sudokn_ITARCompliant.<br/>10 occurrences with subject type io_Manufacturer and object type sudokn_ASME.<br/>7 occurrences with subject type io_Manufacturer and object type sudokn_ISO14001.<br/>2 occurrences with subject type io_Manufacturer and object type sudokn_HAACPCertificate.<br/>9 occurrences with subject type io_Manufacturer and object type sudokn_AS9102Certificate.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_BritishRetailConsortiumAccreditation.<br/>3 occurrences with subject type io_Manufacturer and object type sudokn_BABACertificate.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_ISO13485.<br/>6 occurrences with subject type io_Manufacturer and object type sudokn_IS-TS16949.<br/>4 occurrences with subject type io_Manufacturer and object type sudokn_ISTS16949Certificate.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_QS9000.<br/>2 occurrences with subject type io_Manufacturer and object type sudokn_FDAGMPCompliant.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_LEEDCertificate.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_TI9000Certificate.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_KOSHERApproved.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_NADCAPAC7004.|
| [sudokn_hasEmailAddress](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasEmailAddress.md) | No slot description provided<br/>1 occurrences with subject type owl_NamedIndividual and object type sudokn_EmailAddress.|
| [sudokn_hasIntegerValue](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasIntegerValue.md) | No slot description provided<br/>18729 occurrences with subject type sudokn_USPostalCode and object type string.|
| [sudokn_hasLatitudeValue](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasLatitudeValue.md) | No slot description provided<br/>19082 occurrences with subject type sudokn_TwoDimensionalCartesianSpatialCoordinateDatum and object type string.|
| [sudokn_hasLongitudeValue](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasLongitudeValue.md) | No slot description provided<br/>19083 occurrences with subject type sudokn_TwoDimensionalCartesianSpatialCoordinateDatum and object type string.|
| [sudokn_hasManagementCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasManagementCapability.md) | No slot description provided<br/>1 occurrences with subject type owl_NamedIndividual and object type sudokn_QualityManagementCapability.|
| [sudokn_hasMaterialCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasMaterialCapability.md) | No slot description provided<br/>1 occurrences with subject type owl_NamedIndividual and object type sudokn_AluminumProcessingCapability.<br/>1 occurrences with subject type owl_NamedIndividual and object type sudokn_StainlessSteelProcessingCapability.<br/>1754 occurrences with subject type io_Manufacturer and object type sudokn_BronzeProcessingCapability.<br/>2866 occurrences with subject type io_Manufacturer and object type sudokn_GlassProcessingCapability.<br/>472 occurrences with subject type io_Manufacturer and object type sudokn_GraphiteProcessingCapability.<br/>5903 occurrences with subject type io_Manufacturer and object type sudokn_IronProcessingCapability.<br/>1830 occurrences with subject type io_Manufacturer and object type sudokn_RubberProcessingCapability.<br/>4795 occurrences with subject type io_Manufacturer and object type sudokn_StainlessSteelProcessingCapability.<br/>7200 occurrences with subject type io_Manufacturer and object type sudokn_SteelProcessingCapability.<br/>1065 occurrences with subject type io_Manufacturer and object type sudokn_FoamProcessingCapability.<br/>4159 occurrences with subject type io_Manufacturer and object type sudokn_PlasticProcessingCapability.<br/>2784 occurrences with subject type io_Manufacturer and object type sudokn_CopperProcessingCapability.<br/>6560 occurrences with subject type io_Manufacturer and object type sudokn_MetalProcessingCapability.<br/>2918 occurrences with subject type io_Manufacturer and object type sudokn_WoodProcessingCapability.<br/>5646 occurrences with subject type io_Manufacturer and object type sudokn_AluminumProcessingCapability.<br/>2484 occurrences with subject type io_Manufacturer and object type sudokn_LeadProcessingCapability.<br/>1039 occurrences with subject type io_Manufacturer and object type sudokn_UrethaneProcessingCapability.<br/>1051 occurrences with subject type io_Manufacturer and object type sudokn_CeramicProcessingCapability.<br/>289 occurrences with subject type io_Manufacturer and object type sudokn_DelrinProcessingCapability.<br/>1177 occurrences with subject type io_Manufacturer and object type sudokn_NylonProcessingCapability.<br/>693 occurrences with subject type io_Manufacturer and object type sudokn_PolycarbonateProcessingCapability.<br/>538 occurrences with subject type io_Manufacturer and object type sudokn_TeflonProcessingCapability.<br/>1266 occurrences with subject type io_Manufacturer and object type sudokn_ZincProcessingCapability.<br/>825 occurrences with subject type io_Manufacturer and object type sudokn_AlloySteelProcessingCapability.<br/>690 occurrences with subject type io_Manufacturer and object type sudokn_SiliconeProcessingCapability.<br/>365 occurrences with subject type io_Manufacturer and object type sudokn_SteelAlloyProcessingCapability.<br/>1196 occurrences with subject type io_Manufacturer and object type sudokn_CompositeProcessingCapability.<br/>225 occurrences with subject type io_Manufacturer and object type sudokn_PlatinumProcessingCapability.<br/>1344 occurrences with subject type io_Manufacturer and object type sudokn_ChemicalsProcessingCapability.<br/>303 occurrences with subject type io_Manufacturer and object type sudokn_CobaltProcessingCapability.<br/>1603 occurrences with subject type io_Manufacturer and object type sudokn_NickelProcessingCapability.<br/>906 occurrences with subject type io_Manufacturer and object type sudokn_InconelProcessingCapability.<br/>1349 occurrences with subject type io_Manufacturer and object type sudokn_TitaniumProcessingCapability.<br/>820 occurrences with subject type io_Manufacturer and object type sudokn_TungstenProcessingCapability.<br/>362 occurrences with subject type io_Manufacturer and object type sudokn_AcetalProcessingCapability.<br/>360 occurrences with subject type io_Manufacturer and object type sudokn_BerylliumProcessingCapability.<br/>2596 occurrences with subject type io_Manufacturer and object type sudokn_BrassProcessingCapability.<br/>461 occurrences with subject type io_Manufacturer and object type sudokn_LexanProcessingCapability.<br/>382 occurrences with subject type io_Manufacturer and object type sudokn_MolybdenumProcessingCapability.<br/>1251 occurrences with subject type io_Manufacturer and object type sudokn_SilverProcessingCapability.<br/>786 occurrences with subject type io_Manufacturer and object type sudokn_CarbideProcessingCapability.<br/>1302 occurrences with subject type io_Manufacturer and object type sudokn_GoldProcessingCapability.<br/>417 occurrences with subject type io_Manufacturer and object type sudokn_TinProcessingCapability.<br/>551 occurrences with subject type io_Manufacturer and object type sudokn_ChromiumProcessingCapability.<br/>219 occurrences with subject type io_Manufacturer and object type sudokn_InvarProcessingCapability.<br/>197 occurrences with subject type io_Manufacturer and object type sudokn_KovarProcessingCapability.<br/>419 occurrences with subject type io_Manufacturer and object type sudokn_MagnesiumProcessingCapability.<br/>234 occurrences with subject type io_Manufacturer and object type sudokn_TantalumProcessingCapability.<br/>66 occurrences with subject type io_Manufacturer and object type sudokn_WaspaloyProcessingCapability.<br/>321 occurrences with subject type io_Manufacturer and object type sudokn_HastelloyProcessingCapability.<br/>317 occurrences with subject type io_Manufacturer and object type sudokn_ExoticMaterialProcessingCapability.<br/>78 occurrences with subject type io_Manufacturer and object type sudokn_PalladiumProcessingCapability.<br/>80 occurrences with subject type io_Manufacturer and object type sudokn_ZincAlloyProcessingCapability.<br/>240 occurrences with subject type io_Manufacturer and object type sudokn_ZirconProcessingCapability.<br/>71 occurrences with subject type io_Manufacturer and object type sudokn_SpecialMaterialsProcessingCapability.<br/>120 occurrences with subject type io_Manufacturer and object type sudokn_LowAlloySteelProcessingCapability.<br/>252 occurrences with subject type io_Manufacturer and object type sudokn_ColdRolledSteelProcessingCapability.<br/>58 occurrences with subject type io_Manufacturer and object type sudokn_NomexProcessingCapability.<br/>28 occurrences with subject type io_Manufacturer and object type sudokn_DifficultToMachineMaterialsProcessingCapability.<br/>32 occurrences with subject type io_Manufacturer and object type sudokn_KaptonProcessingCapability.<br/>5 occurrences with subject type io_Manufacturer and object type sudokn_HighGradeAluminumProcessingCapability.<br/>6 occurrences with subject type io_Manufacturer and object type sudokn_PreciousMaterialProcessingCapability.<br/>12 occurrences with subject type io_Manufacturer and object type sudokn_ExtremelyHardMaterialProcessingCapability.<br/>15 occurrences with subject type io_Manufacturer and object type sudokn_NaturalFiberProcessingCapability.<br/>12 occurrences with subject type io_Manufacturer and object type sudokn_PhosBronzeProcessingCapability.<br/>13 occurrences with subject type io_Manufacturer and object type sudokn_CarbonGraphiteProcessingCapability.<br/>2 occurrences with subject type io_Manufacturer and object type sudokn_ManMadeFiberProcessingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_PhosphorBronzeProcessingCapability.|
| [sudokn_hasNAICSClassifier](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasNAICSClassifier.md) | No slot description provided<br/>1 occurrences with subject type owl_NamedIndividual and object type sudokn_NAICSClassifier.|
| [sudokn_hasNAICSCodeValue](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasNAICSCodeValue.md) | No slot description provided<br/>22 occurrences with subject type sudokn_NAICSClassifier and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332111 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332112 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332114 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332115 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332116 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332117 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332211 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332212 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332213 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332214 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332311 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332312 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332313 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332321 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332322 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332323 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332410 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332420 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332431 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332439 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332510 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332611 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332612 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332618 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332710 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332721 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332722 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332811 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332812 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332813 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332911 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332912 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332913 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332919 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332991 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332992 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332994 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332995 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332996 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332997 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332998 and object type integer.<br/>1 occurrences with subject type sudokn_NAICS332999 and object type integer.|
| [sudokn_hasNAICSTextValue](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasNAICSTextValue.md) | No slot description provided<br/>23 occurrences with subject type sudokn_NAICSClassifier and object type string.<br/>1 occurrences with subject type sudokn_NAICS332111 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332112 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332114 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332115 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332116 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332117 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332211 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332212 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332213 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332214 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332311 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332312 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332313 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332321 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332322 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332323 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332410 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332420 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332431 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332439 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332510 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332611 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332612 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332618 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332710 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332721 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332722 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332811 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332812 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332813 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332911 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332912 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332913 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332919 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332991 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332992 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332994 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332995 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332996 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332997 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332998 and object type string.<br/>1 occurrences with subject type sudokn_NAICS332999 and object type string.|
| [sudokn_hasName](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasName.md) | No slot description provided<br/>1 occurrences with subject type owl_NamedIndividual and object type sudokn_OrganizationName.|
| [sudokn_hasNumberOfEmployees](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasNumberOfEmployees.md) | No slot description provided<br/>6931 occurrences with subject type io_Manufacturer and object type integer.|
| [sudokn_hasOrganizationYearOfEstablishment](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasOrganizationYearOfEstablishment.md) | No slot description provided<br/>280 occurrences with subject type io_Manufacturer and object type string.|
| [sudokn_hasOwnershipStatusClassifier](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasOwnershipStatusClassifier.md) | No slot description provided<br/>1 occurrences with subject type owl_NamedIndividual and object type sudokn_OwnershipStatusClassifier.<br/>1119 occurrences with subject type io_Manufacturer and object type sudokn_OwnershipStatusClassifier.|
| [sudokn_hasPostalAddress](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasPostalAddress.md) | No slot description provided<br/>6948 occurrences with subject type sudokn_GeospatialLocation and object type sudokn_PostalAddress.<br/>2414 occurrences with subject type sudokn_GeospatialLocation and object type uri.<br/>1 occurrences with subject type owl_NamedIndividual and object type sudokn_UnitedStatesPostalCode.<br/>11366 occurrences with subject type io_Manufacturer and object type sudokn_PostalAddress.|
| [sudokn_hasPrimaryNAICSClassifier](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasPrimaryNAICSClassifier.md) | No slot description provided<br/>150 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332996.<br/>49 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332997.<br/>172 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332812.<br/>202 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332321.<br/>249 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332312.<br/>579 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332322.<br/>338 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332813.<br/>69 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332439.<br/>1745 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332710.<br/>304 occurrences with subject type io_Manufacturer and object type sudokn_NAICSClassifier.<br/>223 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332618.<br/>127 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332323.<br/>121 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332510.<br/>377 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332116.<br/>556 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332999.<br/>18 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332998.<br/>69 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332111.<br/>133 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332311.<br/>143 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332919.<br/>35 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332721.<br/>92 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332811.<br/>25 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332214.<br/>15 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332211.<br/>103 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332212.<br/>102 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332410.<br/>80 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332912.<br/>87 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332420.<br/>13 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332117.<br/>11 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332114.<br/>86 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332911.<br/>114 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332722.<br/>72 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332611.<br/>42 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332994.<br/>6 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332313.<br/>16 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332992.<br/>39 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332991.<br/>16 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332431.<br/>19 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332213.<br/>9 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332913.<br/>3 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332612.<br/>3 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332115.<br/>6 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332112.<br/>6 occurrences with subject type io_Manufacturer and object type sudokn_NAICS332995.|
| [sudokn_hasPrimaryNIACSClassifier](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasPrimaryNIACSClassifier.md) | No slot description provided<br/>|
| [sudokn_hasProcessCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasProcessCapability.md) | No slot description provided<br/>1 occurrences with subject type owl_NamedIndividual and object type sudokn_AssemblyCapibility.<br/>1 occurrences with subject type owl_NamedIndividual and object type sudokn_FinishingCapability.<br/>1 occurrences with subject type owl_NamedIndividual and object type sudokn_MachiningCapability.<br/>1427 occurrences with subject type io_Manufacturer and object type sudokn_CNCMachiningCapability.<br/>2518 occurrences with subject type io_Manufacturer and object type sudokn_FabricatingCapability.<br/>1614 occurrences with subject type io_Manufacturer and object type sudokn_FinishingCapability.<br/>1802 occurrences with subject type io_Manufacturer and object type sudokn_FormingCapability.<br/>3493 occurrences with subject type io_Manufacturer and object type sudokn_MachiningCapability.<br/>2931 occurrences with subject type io_Manufacturer and object type sudokn_AssemblyCapability.<br/>1449 occurrences with subject type io_Manufacturer and object type sudokn_DrawingCapability.<br/>1114 occurrences with subject type io_Manufacturer and object type sudokn_EDMCapability.<br/>581 occurrences with subject type io_Manufacturer and object type sudokn_LaserCuttingCapability.<br/>1216 occurrences with subject type io_Manufacturer and object type sudokn_StampingCapability.<br/>2700 occurrences with subject type io_Manufacturer and object type sudokn_WeldingCapability.<br/>644 occurrences with subject type io_Manufacturer and object type sudokn_WireEDMCapability.<br/>945 occurrences with subject type io_Manufacturer and object type sudokn_BendingCapability.<br/>857 occurrences with subject type io_Manufacturer and object type sudokn_BoringCapability.<br/>1195 occurrences with subject type io_Manufacturer and object type sudokn_CastingCapability.<br/>197 occurrences with subject type io_Manufacturer and object type sudokn_ElectricalDischargeMachiningCapability.<br/>2311 occurrences with subject type io_Manufacturer and object type sudokn_MillingCapability.<br/>1765 occurrences with subject type io_Manufacturer and object type sudokn_PackingCapability.<br/>533 occurrences with subject type io_Manufacturer and object type sudokn_TubingCapability.<br/>373 occurrences with subject type io_Manufacturer and object type sudokn_WaterjetCuttingCapability.<br/>659 occurrences with subject type io_Manufacturer and object type sudokn_AnodizingCapability.<br/>1105 occurrences with subject type io_Manufacturer and object type sudokn_CNCMillingCapability.<br/>1361 occurrences with subject type io_Manufacturer and object type sudokn_DrillingCapability.<br/>1339 occurrences with subject type io_Manufacturer and object type sudokn_ElectroPlatingCapability.<br/>487 occurrences with subject type io_Manufacturer and object type sudokn_EtchingCapability.<br/>1654 occurrences with subject type io_Manufacturer and object type sudokn_GrindingCapability.<br/>2077 occurrences with subject type io_Manufacturer and object type sudokn_TurningCapability.<br/>209 occurrences with subject type io_Manufacturer and object type sudokn_AdditiveManufacturingCapability.<br/>337 occurrences with subject type io_Manufacturer and object type sudokn_AddtiveManufacturingCapability.<br/>220 occurrences with subject type io_Manufacturer and object type sudokn_DieCastingCapability.<br/>602 occurrences with subject type io_Manufacturer and object type sudokn_ExtrudingCapability.<br/>83 occurrences with subject type io_Manufacturer and object type sudokn_InvestmentCastingCapability.<br/>278 occurrences with subject type io_Manufacturer and object type sudokn_ReamingCapability.<br/>504 occurrences with subject type io_Manufacturer and object type sudokn_ShapingCapability.<br/>28 occurrences with subject type io_Manufacturer and object type sudokn_SheetMetalProcessingCapability.<br/>56 occurrences with subject type io_Manufacturer and object type sudokn_SinteringCapability.<br/>16 occurrences with subject type io_Manufacturer and object type sudokn_VacuumCastingCapability.<br/>256 occurrences with subject type io_Manufacturer and object type sudokn_RapidPrototypingCapability.<br/>228 occurrences with subject type io_Manufacturer and object type sudokn_BlackOxideCoatingCapability.<br/>17 occurrences with subject type io_Manufacturer and object type sudokn_CentrifugalCastingCapability.<br/>69 occurrences with subject type io_Manufacturer and object type sudokn_EmbossingCapability.<br/>72 occurrences with subject type io_Manufacturer and object type sudokn_GalvanizingCapability.<br/>10 occurrences with subject type io_Manufacturer and object type sudokn_PermanentMoldCastingCapability.<br/>1744 occurrences with subject type io_Manufacturer and object type sudokn_CoatingCapability.<br/>679 occurrences with subject type io_Manufacturer and object type sudokn_PowderCoatingCapability.<br/>550 occurrences with subject type io_Manufacturer and object type sudokn_SurfacePreparationCapability.<br/>437 occurrences with subject type io_Manufacturer and object type sudokn_VerticalMillingCapability.<br/>923 occurrences with subject type io_Manufacturer and object type sudokn_HeatTreatingCapability.<br/>609 occurrences with subject type io_Manufacturer and object type sudokn_ForgingCapability.<br/>644 occurrences with subject type io_Manufacturer and object type sudokn_MoldingCapability.<br/>287 occurrences with subject type io_Manufacturer and object type sudokn_LiveToolingCapability.<br/>109 occurrences with subject type io_Manufacturer and object type sudokn_NotchingCapability.<br/>605 occurrences with subject type io_Manufacturer and object type sudokn_RollingCapability.<br/>81 occurrences with subject type io_Manufacturer and object type sudokn_LaserEtchingCapability.<br/>121 occurrences with subject type io_Manufacturer and object type sudokn_FabricationCapability.<br/>235 occurrences with subject type io_Manufacturer and object type sudokn_PlasmaCuttingCapability.<br/>340 occurrences with subject type io_Manufacturer and object type sudokn_SandBlastingCapability.<br/>460 occurrences with subject type io_Manufacturer and object type sudokn_HoningCapability.<br/>148 occurrences with subject type io_Manufacturer and object type sudokn_SinkerEDMCapability.<br/>860 occurrences with subject type io_Manufacturer and object type sudokn_TappingCapability.<br/>456 occurrences with subject type io_Manufacturer and object type sudokn_PolishingCapability.<br/>64 occurrences with subject type io_Manufacturer and object type sudokn_KnurlingCapability.<br/>9 occurrences with subject type io_Manufacturer and object type sudokn_AbrasiveCleaningCapability.<br/>194 occurrences with subject type io_Manufacturer and object type sudokn_ChemicalProcessingCapability.<br/>437 occurrences with subject type io_Manufacturer and object type sudokn_JoiningCapability.<br/>280 occurrences with subject type io_Manufacturer and object type sudokn_PassivationCapability.<br/>76 occurrences with subject type io_Manufacturer and object type sudokn_SurfaceFinishingCapability.<br/>181 occurrences with subject type io_Manufacturer and object type sudokn_HorizontalMillingCapability.<br/>70 occurrences with subject type io_Manufacturer and object type sudokn_PolycrystallineDiamondMachiningCapability.<br/>147 occurrences with subject type io_Manufacturer and object type sudokn_BrazingCapability.<br/>28 occurrences with subject type io_Manufacturer and object type sudokn_RamEDMCapability.<br/>269 occurrences with subject type io_Manufacturer and object type sudokn_HardeningCapability.<br/>81 occurrences with subject type io_Manufacturer and object type sudokn_DeepHoleDrillingCapability.<br/>99 occurrences with subject type io_Manufacturer and object type sudokn_AnnealingCapability.<br/>271 occurrences with subject type io_Manufacturer and object type sudokn_SolderingCapability.<br/>86 occurrences with subject type io_Manufacturer and object type sudokn_DeburringCapability.<br/>81 occurrences with subject type io_Manufacturer and object type sudokn_CarburizingCapability.<br/>8 occurrences with subject type io_Manufacturer and object type sudokn_CreepFeedGrindingCapability.<br/>139 occurrences with subject type io_Manufacturer and object type sudokn_ChromateConversionCoatingCapability.<br/>10 occurrences with subject type io_Manufacturer and object type sudokn_PhysicalVaporDepositionCapability.<br/>214 occurrences with subject type io_Manufacturer and object type sudokn_ElectrolessNickelPlatingCapability.<br/>45 occurrences with subject type io_Manufacturer and object type sudokn_NitridingCapability.<br/>38 occurrences with subject type io_Manufacturer and object type sudokn_SpinningCapability.<br/>61 occurrences with subject type io_Manufacturer and object type sudokn_ElectropolishingCapability.<br/>23 occurrences with subject type io_Manufacturer and object type sudokn_WireHarnessAssemblyCapability.<br/>13 occurrences with subject type io_Manufacturer and object type sudokn_VaporizedMetalCoatingCapability.<br/>27 occurrences with subject type io_Manufacturer and object type sudokn_Oxy-FuelCuttingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_LaserProcessingCapability.<br/>17 occurrences with subject type io_Manufacturer and object type sudokn_PlaningCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_PlasmaSprayingCapability.<br/>19 occurrences with subject type io_Manufacturer and object type sudokn_CuttingCapability.<br/>6 occurrences with subject type io_Manufacturer and object type sudokn_FlameSprayingCapability.<br/>16 occurrences with subject type io_Manufacturer and object type sudokn_CNCTurningCapability.<br/>6 occurrences with subject type io_Manufacturer and object type sudokn_ElectronBeamWeldingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_ScreenPrintingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_WetPaintingCapability.<br/>28 occurrences with subject type io_Manufacturer and object type sudokn_EngineeringDesignCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_ElectolessNickelPlatingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_NickelPlatingCapability.<br/>2 occurrences with subject type io_Manufacturer and object type sudokn_PlatingCapability.<br/>6 occurrences with subject type io_Manufacturer and object type sudokn_DieMakingCapability.<br/>8 occurrences with subject type io_Manufacturer and object type sudokn_MoldMakingCapability.<br/>2 occurrences with subject type io_Manufacturer and object type sudokn_RivetingCapability.<br/>6 occurrences with subject type io_Manufacturer and object type sudokn_ToolMakingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_PLCProgrammingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_ContinuousCastingCapability.<br/>7 occurrences with subject type io_Manufacturer and object type sudokn_PunchingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_SmeltingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_DeepFreezingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_VacuumHardeningCapability.<br/>13 occurrences with subject type io_Manufacturer and object type sudokn_ShearingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_PrototypingCapability.<br/>12 occurrences with subject type io_Manufacturer and object type sudokn_WoodWorkingCapability.<br/>43 occurrences with subject type io_Manufacturer and object type sudokn_CarbonitridingCapability.<br/>9 occurrences with subject type io_Manufacturer and object type sudokn_ShrinkFittingCapability.<br/>3 occurrences with subject type io_Manufacturer and object type sudokn_MechanicalJoiningCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_OilGroovingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_PressBrakingCapability.<br/>2 occurrences with subject type io_Manufacturer and object type sudokn_RoboticWeldingCapability.<br/>2 occurrences with subject type io_Manufacturer and object type sudokn_GearCuttingCapability.<br/>6 occurrences with subject type io_Manufacturer and object type sudokn_MetalFabricationCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_CNCmillingCapability.<br/>5 occurrences with subject type io_Manufacturer and object type sudokn_SheetMetalFabricationCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_PrintingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_LatheWorkCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_MechanicalAssemblyCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_BrassBlackeningCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_MetalSpinningCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_KnittingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_2-AxisCNCTurningCapability.<br/>3 occurrences with subject type io_Manufacturer and object type sudokn_TIGWeldingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_CNCPlasmaCuttingCapability.<br/>6 occurrences with subject type io_Manufacturer and object type sudokn_PressingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_VacuumFormingCapability.<br/>19 occurrences with subject type io_Manufacturer and object type sudokn_SwissMachiningCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_ThermoformingCapability.<br/>2 occurrences with subject type io_Manufacturer and object type sudokn_ShellMoldCastingCapability.<br/>2 occurrences with subject type io_Manufacturer and object type sudokn_InstallationCapability.<br/>2 occurrences with subject type io_Manufacturer and object type sudokn_KittingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_CNCPressBrakeCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_SteelManufacturingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_TurretPunchingCapability.<br/>4 occurrences with subject type io_Manufacturer and object type sudokn_SandCastingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_CenterlessGrindingCapability.<br/>3 occurrences with subject type io_Manufacturer and object type sudokn_PaintingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_WiringCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_PlasterMoldCastingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_FasteningCapability.<br/>2 occurrences with subject type io_Manufacturer and object type sudokn_MetalStampingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_SinkerEdmCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_FillingCapability.<br/>3 occurrences with subject type io_Manufacturer and object type sudokn_PackagingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_CNCCylindricalGrindingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_EndFormingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_DigitalPrintingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_SwissTurningCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_PipingFabricationCapability.<br/>2 occurrences with subject type io_Manufacturer and object type sudokn_HarperizingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_BroachingCapability.<br/>2 occurrences with subject type io_Manufacturer and object type sudokn_WaterJetCuttingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_PrototypeManufacturingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_MIGWeldinCapability.<br/>3 occurrences with subject type io_Manufacturer and object type sudokn_SpotWeldingCapability.<br/>2 occurrences with subject type io_Manufacturer and object type sudokn_MIGWeldingCapability.<br/>3 occurrences with subject type io_Manufacturer and object type sudokn_CADCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_CeramicMoldCastingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_CNCBendingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_WaterjetCuttimgCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_LiquidCoatingCapability.<br/>2 occurrences with subject type io_Manufacturer and object type sudokn_VacuumPackagingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_ChemicalCoatingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_CNCCuttingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_SewingCapability.<br/>2 occurrences with subject type io_Manufacturer and object type sudokn_SheetMetalFormingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_CNCFormingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_ProductDesignCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_RivettingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_SilkScreeningCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_CNCWireBendingCapability.<br/>3 occurrences with subject type io_Manufacturer and object type sudokn_WireBendingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_WireFormingCapability.<br/>2 occurrences with subject type io_Manufacturer and object type sudokn_ReverseEngineeringCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_FixtureDesignCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_FixturingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_PemInsertionCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_CNCGrindingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_ExtrusionCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_SanitaryWeldingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_CNCHorizontalTurningCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_CNCLaserCuttingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_CNCVerticalMillingCapability.<br/>3 occurrences with subject type io_Manufacturer and object type sudokn_ElectroplatingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_TubeBendingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_MediaBlastingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_MigWeldingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_ResistanceWeldingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_InductionHeatingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_PhosphateCoatingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_CerakoteCoatingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_TubeFormingCapability.<br/>2 occurrences with subject type io_Manufacturer and object type sudokn_SurfaceGrindingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_CylindricalGrindingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_PulsedElectrochemicalMachiningCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_CNCLatheCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_FiberOpticLaserCuttingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_ZincArcSprayCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_PlasticMachiningCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_MachineBuildingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_ChemicalCleaningCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_ElectrolessPlatingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_HotDipGalvanizingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_LaserWeldingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_RAMEdmCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_CustomFoamCuttingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_3DPrintingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_AcrylicFabricationCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_MetalworkingCapability.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_WoodworkingCapability.|
| [sudokn_hasSecondaryNAICSClassifier](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasSecondaryNAICSClassifier.md) | No slot description provided<br/>112 occurrences with subject type io_Manufacturer and object type sudokn_NAICSClassifier.|
| [sudokn_hasSecondaryNIACSClassifier](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasSecondaryNIACSClassifier.md) | No slot description provided<br/>|
| [sudokn_hasSpatialCoordinates](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasSpatialCoordinates.md) | No slot description provided<br/>20728 occurrences with subject type sudokn_GeospatialLocation and object type sudokn_TwoDimensionalCartesianSpatialCoordinateDatum.|
| [sudokn_hasSpecialBusinessStatusClassifier](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasSpecialBusinessStatusClassifier.md) | No slot description provided<br/>|
| [sudokn_hasWebAddress](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasWebAddress.md) | No slot description provided<br/>1 occurrences with subject type owl_NamedIndividual and object type sudokn_WebAddress.|
| [sudokn_hasZIPcode](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasZIPcode.md) | No slot description provided<br/>20424 occurrences with subject type sudokn_GeospatialLocation and object type sudokn_USPostalCode.|
| [sudokn_locatedInCity](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_locatedInCity.md) | No slot description provided<br/>19022 occurrences with subject type sudokn_GeospatialLocation and object type sudokn_City.|
| [sudokn_locatedInState](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_locatedInState.md) | No slot description provided<br/>3734 occurrences with subject type sudokn_City and object type sudokn_State.|
| [sudokn_manufactures](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_manufactures.md) | No slot description provided<br/>71660 occurrences with subject type io_Manufacturer and object type io_MaterialProduct.|
| [sudokn_OrganizationLocatedIn](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_OrganizationLocatedIn.md) | No slot description provided<br/>|
| [sudokn_organizationLocatedIn](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_organizationLocatedIn.md) | No slot description provided<br/>20728 occurrences with subject type io_Manufacturer and object type sudokn_GeospatialLocation.|
| [sudokn_suppliesToIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_suppliesToIndustry.md) | No slot description provided<br/>1 occurrences with subject type owl_NamedIndividual and object type sudokn_AerospaceIndustry.<br/>2228 occurrences with subject type io_Manufacturer and object type sudokn_TransportationIndustry.<br/>2916 occurrences with subject type io_Manufacturer and object type sudokn_AutomotiveIndustry.<br/>1001 occurrences with subject type io_Manufacturer and object type sudokn_FurnitureIndustry.<br/>3873 occurrences with subject type io_Manufacturer and object type sudokn_ConstructionIndustry.<br/>2314 occurrences with subject type io_Manufacturer and object type sudokn_FoodIndustry.<br/>2603 occurrences with subject type io_Manufacturer and object type sudokn_GovernmentIndustry.<br/>2774 occurrences with subject type io_Manufacturer and object type sudokn_MilitaryIndustry.<br/>248 occurrences with subject type io_Manufacturer and object type sudokn_UtilitiesIndustry.<br/>1910 occurrences with subject type io_Manufacturer and object type sudokn_MiningIndustry.<br/>372 occurrences with subject type io_Manufacturer and object type sudokn_ConsumerGoods.<br/>527 occurrences with subject type io_Manufacturer and object type sudokn_HealthcareServicesIndustry.<br/>398 occurrences with subject type io_Manufacturer and object type sudokn_ProfessionalServicesIndustry.<br/>342 occurrences with subject type io_Manufacturer and object type sudokn_SportsAndLeisureIndustry.<br/>1208 occurrences with subject type io_Manufacturer and object type sudokn_CommunicationIndustry.<br/>671 occurrences with subject type io_Manufacturer and object type sudokn_RecyclingIndustry.<br/>121 occurrences with subject type io_Manufacturer and object type sudokn_ElectronicProductIndustry.<br/>1293 occurrences with subject type io_Manufacturer and object type sudokn_AgricultureIndustry.<br/>226 occurrences with subject type io_Manufacturer and object type sudokn_TextilesIndustry.<br/>525 occurrences with subject type io_Manufacturer and object type sudokn_ChemicalAndPetrochemicalIndustry.<br/>14 occurrences with subject type io_Manufacturer and object type sudokn_HealthCareServicesIndustry.<br/>90 occurrences with subject type io_Manufacturer and object type sudokn_IndustrialMachineryandEquipmentIndustry.<br/>157 occurrences with subject type io_Manufacturer and object type sudokn_ApparelIndustry.<br/>40 occurrences with subject type io_Manufacturer and object type sudokn_AerospaceIndustry.<br/>63 occurrences with subject type io_Manufacturer and object type sudokn_MachinaryAndEquipmentIndustry.<br/>79 occurrences with subject type io_Manufacturer and object type sudokn_EducationIndustry.<br/>127 occurrences with subject type io_Manufacturer and object type sudokn_ElectronicAutomotiveInudstry.<br/>9 occurrences with subject type io_Manufacturer and object type sudokn_WarehousingAndStorageIndustry.<br/>20 occurrences with subject type io_Manufacturer and object type sudokn_CommunicationandElectronicPowerUtilitiesIndustry.<br/>36 occurrences with subject type io_Manufacturer and object type sudokn_MetalProductionIndustry.<br/>60 occurrences with subject type io_Manufacturer and object type sudokn_MetalsProductsIndustry.<br/>10 occurrences with subject type io_Manufacturer and object type sudokn_ComputersandElectronicProductsIndustry.<br/>4 occurrences with subject type io_Manufacturer and object type sudokn_ElectricVehiclesIndustry.<br/>5 occurrences with subject type io_Manufacturer and object type sudokn_WaterandSewerUtilitiesIndustry.<br/>23 occurrences with subject type io_Manufacturer and object type sudokn_ConsumerGoodsIndustry.<br/>7 occurrences with subject type io_Manufacturer and object type sudokn_PlasticsandRubberProductsIndustry.<br/>24 occurrences with subject type io_Manufacturer and object type sudokn_OffshoreWindIndustry.<br/>10 occurrences with subject type io_Manufacturer and object type sudokn_RetailTradeIndustry.<br/>12 occurrences with subject type io_Manufacturer and object type sudokn_Textiles.<br/>16 occurrences with subject type io_Manufacturer and object type sudokn_SportsandLeisureIndustry.<br/>3 occurrences with subject type io_Manufacturer and object type sudokn_RetailIndustry.<br/>14 occurrences with subject type io_Manufacturer and object type sudokn_PaperIndustry.<br/>3 occurrences with subject type io_Manufacturer and object type sudokn_OilAndGasIndustry.<br/>4 occurrences with subject type io_Manufacturer and object type sudokn_WoodProductManufacturingIndustry.<br/>14 occurrences with subject type io_Manufacturer and object type sudokn_BusinessEquipmentIndustry.<br/>8 occurrences with subject type io_Manufacturer and object type sudokn_PaperandPaperboardProductsIndustry.<br/>3 occurrences with subject type io_Manufacturer and object type sudokn_PlasticAndRubberIndustry.<br/>2 occurrences with subject type io_Manufacturer and object type sudokn_EducationalInstitutionsIndustry.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_PrintingAndInformationIndustry.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_GovermentIndustry.<br/>1 occurrences with subject type io_Manufacturer and object type sudokn_Industry.|







