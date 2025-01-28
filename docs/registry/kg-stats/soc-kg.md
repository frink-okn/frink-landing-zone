# SOC KG: Digging Into Soil Carbon With USDA: A Knowledge Graph Informing Soil Carbon Modeling 


## Schema Diagram

```mermaid
erDiagram
SockgAmendment {
    double sockg_irrigationType  
    string sockg_irrigationType  
    string sockg_amendmentPlacement  
    double sockg_amendmentPlacement  
    string sockg_mgtAmendments_UID  
    double sockg_totalAmendmentAmount_kg_per_ha  
    string sockg_startDate  
    double sockg_startDate  
    double sockg_irrigationAmount_cm  
    double sockg_totalNitrogenAmount_kgN_per_ha  
    double sockg_irrigationNitrogen_mg_per_L  
    string sockg_type  
    double sockg_type  
    string sockg_treatmentId  
    double sockg_totalPotassiumAmount_kgK_per_ha  
    double sockg_endDate  
    string sockg_endDate  
    double sockg_totalPhosphorusAmount_kgP_per_ha  
}
SockgBioMassCarbohydrate {
    double sockg_acidInsolubleLigninStd_g_per_kg  
    double sockg_ash_g_per_kg  
    double sockg_acidInsolubleLignin_g_per_kg  
    double sockg_glucan_g_per_kg  
    double sockg_ligninStd_g_per_kg  
    double sockg_xylanStd_g_per_kg  
    double sockg_mannanStd_g_per_kg  
    double sockg_acidDetFiber_g_per_kg  
    string sockg_treatmentId  
    double sockg_acidDetFiberStd_g_per_kg  
    double sockg_acidSolubleLignin_g_per_kg  
    double sockg_lignin_g_per_kg  
    double sockg_mannan_g_per_kg  
    string sockg_date  
    double sockg_date  
    string sockg_growthStage  
    double sockg_growthStage  
    double sockg_crudeProteinStd_g_per_kg  
    double sockg_nonFiberCarbs_g_per_kg  
    double sockg_neutralDetFiber_g_per_kg  
    double sockg_arabinan_g_per_kg  
    double sockg_neutralDetFiberStd_g_per_kg  
    double sockg_glucanStd_g_per_kg  
    double sockg_crudeProtein_g_per_kg  
    double sockg_ashStd_g_per_kg  
    double sockg_galactan_g_per_kg  
    double sockg_nonFiberCarbsStd_g_per_kg  
    string sockg_measBiomassCHO_UID  
    double sockg_galactanStd_g_per_kg  
    string sockg_crop  
    double sockg_crop  
    double sockg_acidSolubleLigninStd_g_per_kg  
    string sockg_plantFraction  
    double sockg_plantFraction  
    double sockg_xylan_g_per_kg  
    double sockg_arabinanStd_g_per_kg  
}
SockgBioMassEnergy {
    double sockg_mineralMatter_g_per_kg  
    string sockg_treatmentId  
    double sockg_grossCalorificValueStd_MJ_per_kg  
    double sockg_grossCalorificValue_MJ_per_kg  
    string sockg_measBiomassEnergy_UID  
    double sockg_volatileMatterStd_g_per_kg  
    string sockg_growthStage  
    double sockg_growthStage  
    double sockg_volatileMatter_g_per_kg  
    string sockg_crop  
    double sockg_crop  
    string sockg_plantFraction  
    double sockg_plantFraction  
    double sockg_mineralMatterStd_g_per_kg  
    string sockg_date  
    double sockg_date  
}
SockgBioMassMineral {
    double sockg_magnesiumConcentration_g_per_kg  
    string sockg_treatmentId  
    double sockg_chlorineConcentration_g_per_kg  
    double sockg_sulfurConcentration_g_per_kg  
    double sockg_magnesiumConcentrationStd_g_per_kg  
    string sockg_measBiomassMinAn_UID  
    double sockg_ironConcentrationStd_mg_per_kg  
    string sockg_crop  
    double sockg_crop  
    double sockg_nitrogenConcentration_g_per_kg  
    double sockg_chlorineConcentrationStd_g_per_kg  
    double sockg_manganeseConcentration_mg_per_kg  
    double sockg_copperConcentrationStd_mg_per_kg  
    double sockg_sodiumConcentration_g_per_kg  
    double sockg_boronConcentrationStd_mg_per_kg  
    double sockg_carbonConcentration_g_per_kg  
    string sockg_plantFraction  
    double sockg_plantFraction  
    string sockg_growthStage  
    double sockg_growthStage  
    double sockg_aluminumConcentrationStd_mg_per_kg  
    double sockg_potassiumConcentrationStd_g_per_kg  
    double sockg_phosphorusConcentrationStd_g_per_kg  
    double sockg_aluminumConcentration_mg_per_kg  
    double sockg_nitrogenConcentrationStd_g_per_kg  
    double sockg_calciumConcentrationStd_g_per_kg  
    double sockg_zincConcentrationStd_mg_per_kg  
    double sockg_sodiumConcentrationStd_g_per_kg  
    double sockg_carbonConcentrationStd_g_per_kg  
    string sockg_date  
    double sockg_date  
    double sockg_manganeseConcentrationStd_mg_per_kg  
    double sockg_potassiumConcentration_g_per_kg  
    double sockg_sulfurConcentrationStd_g_per_kg  
    double sockg_phosphorusConcentration_g_per_kg  
    double sockg_zincConcentration_mg_per_kg  
    double sockg_calciumConcentration_g_per_kg  
    double sockg_ironConcentration_mg_per_kg  
    double sockg_boronConcentration_mg_per_kg  
    double sockg_copperConcentration_mg_per_kg  
}
SockgBook {
    string sockg_bookName  
}
SockgCity {
    string sockg_cityName  
}
SockgCountry {
    string sockg_countryName  
}
SockgCounty {
    string sockg_countyName  
}
SockgCropGrowthStage {
    string sockg_date  
    double sockg_date  
    string sockg_treatmentId  
    string sockg_growthStage  
    double sockg_growthStage  
    string sockg_mgtGrowthStages_UID  
}
SockgDepartment {
    string sockg_departmentName  
}
SockgExperiment {
    string sockg_startDate  
    double sockg_startDate  
    string sockg_experimentName  
    double sockg_endDate  
    string sockg_endDate  
    string sockg_projectName  
}
SockgExperimentalUnit {
    double sockg_changeInManagement  
    string sockg_expUnit_UID  
    string sockg_expUnitId  
    double sockg_endDate  
    string sockg_endDate  
    string sockg_startDate  
    double sockg_startDate  
}
SockgField {
    double sockg_longitude_decimal_deg  
    double sockg_elevation_m  
    string sockg_fieldId  
    double sockg_latitude_decimal_deg  
}
SockgGasNutrientLoss {
    double sockg_nitrousOxideStd_g_ha  
    string sockg_expUnit_UID  
    string sockg_fieldId  
    string sockg_expUnitId  
    string sockg_measGasNutrientLoss_UID  
    string sockg_date  
    double sockg_date  
    double sockg_ammoniaNitrogenStd_kg_ha  
    double sockg_nitrousOxides_g_ha  
    double sockg_modelIfSimulated  
    string sockg_modelIfSimulated  
    double sockg_samplingStartStopInterval  
    string sockg_samplingStartStopInterval  
    double sockg_nitrogenGasStd_g_ha  
    double sockg_nitrousOxide_g_ha  
    string sockg_treatmentId  
    double sockg_ammoniaNitrogen_kg_ha  
    double sockg_nitrogenGas_g_ha  
    double sockg_time  
    string sockg_time  
    string sockg_growthStage  
    double sockg_growthStage  
    string sockg_crop  
    double sockg_crop  
    double sockg_nitrousOxidesStd_g_ha  
}
SockgGasSample {
    double sockg_methane_gC_per_ha_per_d  
    double sockg_airTemperature_degC  
    double sockg_time  
    string sockg_time  
    double sockg_methaneStd_gC_per_ha_per_d  
    double sockg_carbonDioxide_gC_per_ha_per_d  
    integer sockg_soilMoistureDepth_cm  
    double sockg_soilTemperatureStd_degC  
    double sockg_soilTemperature_degC  
    string sockg_treatmentId  
    integer sockg_isNitrousOxideInterpolated  
    double sockg_soilMoisture_percent_volume  
    string sockg_date  
    double sockg_date  
    integer sockg_isCarbonDioxideInterpolated  
    string sockg_chamberPlacement  
    double sockg_chamberPlacement  
    double sockg_carbonDioxideStd_gC_per_ha_per_d  
    double sockg_nitrousOxideStd_gN_per_ha_per_d  
    double sockg_airTemperatureStd_degC  
    string sockg_measGHGFlux_UID  
    double sockg_nitrousOxide_gN_per_ha_per_d  
    string sockg_crop  
    double sockg_crop  
    integer sockg_isMethaneInterpolated  
}
SockgGrazing {
    double sockg_belowgroundNetPrimaryProductivityNitrogen_kgN_per_ha_per_yr  
    double sockg_abovegroundNetPrimaryProductivityCarbon_kgC_per_ha_per_yr  
    double sockg_abovegroundNetPrimaryProductivityNitrogenStd_kgN_per_ha_per_yr  
    double sockg_belowGroundBiomassNitrogenStd_kgN_per_ha  
    double sockg_aboveGroundBiomassNitrogen_kgN_per_ha  
    double sockg_abovegroundNetPrimaryProductivityCarbonStd_kgC_per_ha_per_yr  
    string sockg_speciesMix  
    double sockg_abovegroundNetPrimaryProductivityNitrogen_kgN_per_ha_per_yr  
    string sockg_date  
    double sockg_date  
    double sockg_belowGroundBiomassCarbonStd_kgC_per_ha  
    double sockg_belowGroundBiomassCarbon_kgC_per_ha  
    double sockg_belowgroundNetPrimaryProductivityNitrogenStd_kgN_per_ha_per_yr  
    double sockg_groundCoverPercentageStd  
    double sockg_groundCoverPercentage  
    string sockg_growthStage  
    double sockg_growthStage  
    double sockg_ligninPercentageStd  
    string sockg_broadleafOrGrass  
    double sockg_belowgroundNetPrimaryProductivityCarbon_kgC_per_ha_per_yr  
    double sockg_ligninPercentage  
    string sockg_treatmentId  
    double sockg_leafAreaIndexDry_kg_per_ha  
    double sockg_aboveGroundBiomassNitrogenStd_kgN_per_ha  
    double sockg_aboveGroundBiomassCarbon_kgC_per_ha  
    double sockg_leafAreaIndexDryStd_kg_per_ha  
    double sockg_aboveGroundBiomassDryStd_kg_per_ha  
    double sockg_aboveGroundBiomassCarbonStd_kgC_per_ha  
    double sockg_aboveGroundBiomassDry_kg_per_ha  
    double sockg_belowgroundNetPrimaryProductivityCarbonStd_kgC_per_ha_per_yr  
    double sockg_biomassNitrogenPercentage  
    string sockg_measGrazingPlants_UID  
    double sockg_belowGroundBiomassNitrogen_kgN_per_ha  
}
SockgGrazingManagementEvent {
    string sockg_animalSpecies  
    double sockg_burnIntensity  
    double sockg_yearsBetweenBurns  
    string sockg_treatmentId  
    double sockg_otherEvents  
    string sockg_otherEvents  
    string sockg_startDate  
    double sockg_startDate  
    string sockg_mgtGrazing_UID  
    string sockg_animalClass  
    double sockg_animalClass  
    double sockg_endDate  
    string sockg_endDate  
    double sockg_stockingRate_number_animals_per_ha  
}
SockgHarvest {
    double sockg_aboveGroundBiomassStd_kg_per_ha  
    double sockg_unitGrainWeightStd_mg  
    double sockg_grainMoisturePercentStd  
    double sockg_grainCarbon_kgC_per_ha  
    double sockg_rootNitrogenContentStd_kgN_per_ha  
    double sockg_unitGrainWeight_mg  
    double sockg_aboveGroundBiomass_kg_per_ha  
    double sockg_grainNitrogen_kgN_per_ha  
    double sockg_rootMoisturePercentStd  
    double sockg_grainYield_kg_per_ha  
    double sockg_nonHarvestedResidueMoisturePercent  
    double sockg_cornEarHeight_cm  
    double sockg_driedHarvestedResidue_kg_per_ha  
    double sockg_nonHarvestedResidueMoisturePercentStd  
    double sockg_rootDryMatterStd_kg_per_ha  
    string sockg_harvestedFrac  
    double sockg_harvestedFrac  
    string sockg_growthStage  
    double sockg_growthStage  
    double sockg_cornEarHeightStd_cm  
    double sockg_rootMoisturePercent  
    double sockg_nonHarvestedResidueNitrogenContent_kgN_per_ha  
    double sockg_nonHarvestedResidueCarbonContentStd_kgC_per_ha  
    double sockg_nonHarvestedResidueCarbonContent_kgC_per_ha  
    double sockg_grainNitrogenStd_kgN_per_ha  
    double sockg_rootNitrogenContent_kgN_per_ha  
    double sockg_driedHarvestedResidueStd_kg_per_ha  
    double sockg_rootCarbonContentStd_kgC_per_ha  
    double sockg_rootCarbonContent_kgC_per_ha  
    double sockg_nonHarvestedResidueMassStd_kg_per_ha  
    string sockg_measResidueMgnt_UID  
    double sockg_grainYieldStd_kg_per_ha  
    double sockg_rootDryMatter_kg_per_ha  
    double sockg_grainMoisturePercent  
    string sockg_treatmentId  
    string sockg_date  
    double sockg_date  
    double sockg_grainCarbonStd_kgC_per_ha  
    double sockg_nonHarvestedResidueMass_kg_per_ha  
    double sockg_nonHarvestedResidueNitrogenContentStd_kgN_per_ha  
}
SockgHarvestFraction {
    double sockg_dryBiomass_kg_per_ha  
    double sockg_dryBiomassStd_kg_per_ha  
    double sockg_nitrogen_kgN_per_ha  
    string sockg_measHarvestFraction_UID  
    double sockg_carbonStd_kgC_per_ha  
    double sockg_carbon_kgC_per_ha  
    string sockg_treatmentId  
    double sockg_moisturePercent  
    string sockg_plantFraction  
    double sockg_plantFraction  
    double sockg_grainWeight_mg_per_kernel  
    double sockg_moisturePercentStd  
    double sockg_nitrogenStd_kgN_per_ha  
    double sockg_grainWeightStd_mg_per_lernel  
    string sockg_growthStage  
    double sockg_growthStage  
}
SockgNutrientEfficiency {
    string sockg_crop  
    double sockg_crop  
    string sockg_expUnit_UID  
    string sockg_growthStage  
    double sockg_growthStage  
    double sockg_nitrogenUseEfficiency_kg_ha  
    string sockg_fieldId  
    string sockg_plantFraction  
    double sockg_plantFraction  
    string sockg_expUnitId  
    double sockg_nitrogenUseEfficiencyPct  
    double sockg_nutrientEfficiencyRatio_kg_kg  
    double sockg_agronomicEfficiency_kg_kg  
    string sockg_date  
    double sockg_date  
    string sockg_treatmentId  
    string sockg_measNutrEff_UID  
    double sockg_fracNitrogen_kg_ha  
}
SockgOrganization {
    string sockg_organizationName  
}
SockgPerson {
    string sockg_email  
    double sockg_email  
    double sockg_note  
    string sockg_note  
    string sockg_persons_UID  
    double sockg_phoneNumber  
    string sockg_phoneNumber  
    string sockg_website  
    double sockg_website  
    string sockg_middleName  
    double sockg_middleName  
    string sockg_suffix  
    double sockg_suffix  
    string sockg_roleInStudy  
    double sockg_roleInStudy  
    string sockg_firstName  
    string sockg_lastName  
    string sockg_isPrimaryContact  
    double sockg_isPrimaryContact  
    string sockg_profession  
    double sockg_profession  
}
SockgPesticide {
    double sockg_pesticidePlacement  
    string sockg_pesticidePlacement  
    string sockg_pesticideActiveIngredientType  
    double sockg_pesticideActiveIngredientType  
    double sockg_pesticideTarget  
    string sockg_pesticideTarget  
    string sockg_pesticide_UID  
    double sockg_totalPesticideAmount_kg_per_ha  
}
SockgPlantingEvent {
    double sockg_plantingMethod  
    string sockg_plantingMethod  
    double sockg_rowWidth_cm  
    string sockg_cultivar  
    double sockg_cultivar  
    double sockg_depth_cm  
    string sockg_mgtPlanting_UID  
}
SockgProject {
    string sockg_projectName  
}
SockgPublication {
    string sockg_title  
    double sockg_title  
    string sockg_identifier  
    string sockg_correspondingAuthor  
    double sockg_correspondingAuthor  
    string sockg_author  
    string sockg_citation  
}
SockgResidueManagementEvent {
    string sockg_stageAtHarvest  
    double sockg_stageAtHarvest  
    double sockg_perennialStandAge_years  
    integer sockg_rowsHarvestedPercent  
    string sockg_equipmentType  
    double sockg_equipmentType  
    string sockg_treatmentId  
    string sockg_date  
    double sockg_date  
    string sockg_mgtResidue_UID  
}
SockgRotation {
    string sockg_rotationDescriptor  
}
SockgSite {
    double sockg_siteIdDescriptor  
    double sockg_majorLandResourceArea  
    string sockg_siteSpatialDescription  
    double sockg_siteNativeVegetation  
    string sockg_siteId  
    double sockg_postalCodeNumber  
    double sockg_siteHistory  
}
SockgSoilBiologicalSample {
    double sockg_particulateOrganicMatterStd_gC_per_kg  
    double sockg_carbonMicrobialBiomassStd_mgC_per_kg  
    double sockg_organicPlantMaterial_gC_per_kg  
    double sockg_alkPhosphatase_mg_per_kg_per_hr  
    double sockg_acidPhosphatase_mg_per_kg_per_hr  
    double sockg_glomalinStd_g_per_kg  
    double sockg_glucosidaseStd_mg_per_kg_per_hr  
    double sockg_glucosidase_mg_per_kg_per_hr  
    double sockg_carbonMicrobialBiomass_mgC_per_kg  
    double sockg_lowerDepth_cm  
    integer sockg_lowerDepth_cm  
    double sockg_glucosaminidase_mg_per_kg_per_hr  
    double sockg_glomalin_g_per_kg  
    double sockg_upperDepth_cm  
    integer sockg_upperDepth_cm  
    double sockg_glucosaminidaseStd_mg_per_kg_per_hr  
    string sockg_date  
    double sockg_date  
    double sockg_particulateOrganicMatter_gC_per_kg  
    double sockg_organicPlantMaterialStd_gC_per_kg  
    string sockg_treatmentId  
    double sockg_nitrogenMicrobialBiomass_mgN_per_kg  
    double sockg_nitrogenMicrobialBiomassStd_mgN_per_kg  
    double sockg_alkPhosphataseStd_mg_per_kg_per_hr  
    string sockg_measSoilBiol_UID  
    double sockg_acidPhosphataseStd_mg_per_kg_per_hr  
}
SockgSoilChemicalSample {
    double sockg_extractableZinc_mgZn_per_kg  
    double sockg_nitrateStd_mgN_per_kg  
    string sockg_date  
    double sockg_date  
    double sockg_lowerDepth_cm  
    integer sockg_lowerDepth_cm  
    double sockg_inorganicCarbon_gC_per_kg  
    string sockg_measSoilChem_UID  
    double sockg_extractableCalciumStd_mgCa_per_kg  
    double sockg_extractableManganese_mgMN_per_kg  
    double sockg_nitrites_mgN_per_kg  
    double sockg_organicCarbonStd_gC_per_kg  
    double sockg_extractableIronStd_mgFe_per_kg  
    double sockg_mineralCarbon_gC_per_kg  
    double sockg_ammoniumStd_mgN_per_kg  
    double sockg_extractableCalcium_mgCa_per_kg  
    double sockg_potassium_mgK_per_kg  
    double sockg_electricalConductivity_siemens_per_m  
    double sockg_ph  
    double sockg_extractableIron_mgFe_per_kg  
    double sockg_solubleOrganicCarbonStd_mgC_per_kg  
    double sockg_electricalConductivityStd_siemens_per_m  
    double sockg_inorganicCarbonStd_gC_per_kg  
    double sockg_extractableZincStd_mgZn_per_kg  
    double sockg_organicCarbon_gC_per_kg  
    double sockg_nitrate_mgN_per_kg  
    double sockg_potassiumStd_mgK_per_kg  
    double sockg_mineralizableNitrogen_gN_per_kg  
    double sockg_totalSoilNitrogenStd_gN_per_kg  
    double sockg_mineralizableNitrogenStd_gN_per_kg  
    double sockg_solubleOrganicCarbon_mgC_per_kg  
    double sockg_extractableCopperStd_mgCu_per_kg  
    string sockg_treatmentId  
    double sockg_upperDepth_cm  
    integer sockg_upperDepth_cm  
    double sockg_phosphorus_mgP_per_kg  
    double sockg_extractableCopper_mgCu_per_kg  
    double sockg_cationExchangeCapacityStd_cmol_per_kg  
    double sockg_extractableManganeseStd_mgMN_per_kg  
    double sockg_totalSoilNitrogen_gN_per_kg  
    double sockg_nitritesStd_mgN_per_kg  
    double sockg_extractableMagnesium_mgMg_per_kg  
    double sockg_cationExchangeCapacity_cmol_per_kg  
    double sockg_mineralCarbonStd_gC_per_kg  
    double sockg_totalSoilCarbonStd_gC_per_kg  
    double sockg_extractableMagnesiumStd_mgMg_per_kg  
    double sockg_phosphorusStd_mgP_per_kg  
    double sockg_totalSoilCarbon_gC_per_kg  
    double sockg_ammonium_mgN_per_kg  
}
SockgSoilCover {
    double sockg_soilWithResidueCoverPercent  
    string sockg_measSoilCover_UID  
    string sockg_date  
    double sockg_date  
}
SockgSoilPhysicalSample {
    double sockg_wiltingPoint_percent_volume  
    double sockg_aggregationPercent  
    double sockg_upperDepth_cm  
    integer sockg_upperDepth_cm  
    double sockg_wiltingPointStd_percent_volume  
    double sockg_lowerDepth_cm  
    integer sockg_lowerDepth_cm  
    double sockg_clayPercent  
    string sockg_date  
    double sockg_date  
    double sockg_saturatedHydraulicConductivityStd_cm_per_sec  
    double sockg_macroAggregatesPercentStd  
    double sockg_sandPercent  
    double sockg_siltPercent  
    double sockg_waterStableAggregatesPercentStd  
    string sockg_treatmentId  
    double sockg_waterStableAggregatePercent  
    double sockg_moistureReleaseCurve  
    double sockg_saturatedHydraulicConductivity_cm_per_sec  
    double sockg_nearInfraredCarbonStd_gC_per_kg  
    string sockg_measSoilPhys_UID  
    double sockg_bulkDensity_g_per_cm_cubed  
    double sockg_bulkDensityStd_g_per_cm_cubed  
    double sockg_nearInfraredCarbon_gC_per_kg  
}
SockgState {
    string sockg_stateProvince  
}
SockgTillage {
    string sockg_mgtTillage_UID  
}
SockgTreatment {
    string sockg_fertilizerAmendmentClass  
    double sockg_fertilizerAmendmentClass  
    string sockg_organicManagement  
    string sockg_treatmentDescriptor  
    double sockg_tileDrainage  
    string sockg_tileDrainage  
    string sockg_tillageDescriptor  
    double sockg_tillageDescriptor  
    string sockg_projectScenario  
    double sockg_grazingRate  
    string sockg_grazingRate  
    double sockg_coverCrop  
    string sockg_coverCrop  
    string sockg_residueRemoval  
    string sockg_irrigation  
    double sockg_nitrogenTreatmentDescriptor  
    string sockg_nitrogenTreatmentDescriptor  
    string sockg_treatmentId  
}
SockgVersion {
    string sockg_versionDate  
}
SockgWaterQualityArea {
    double sockg_soilOrganicCarbon_kgC_ha  
    double sockg_dissolvedManganese_gMn_ha  
    double sockg_erosionSedimentStd_t_ha  
    double sockg_dissolvedBoron_gB_ha  
    double sockg_ph  
    double sockg_totalChloride_kg_ha  
    double sockg_dissolvedMagnesium_kgMg_ha  
    double sockg_dissolvedPotassiumStd_kgK_ha  
    string sockg_treatmentId  
    double sockg_dissolvedPotassium_kgK_ha  
    double sockg_dissolvedSodium_kgNa_ha  
    double sockg_soilOrganicCarbonStd_kgC_ha  
    double sockg_dissolvedCalciumStd_kgCa_ha  
    double sockg_totalDissolvedNitrogen_kgN_ha  
    double sockg_dissovledSiliconStd_kgSi_ha  
    string sockg_measWaterQualityArea_UID  
    double sockg_nitrateNitrogen_kg_ha  
    double sockg_nitrateStd_kgN_ha  
    double sockg_modelIfSimulated  
    string sockg_modelIfSimulated  
    double sockg_totalDissolvedNitrogenStd_kgN_ha  
    double sockg_erosionSediment_t_ha  
    double sockg_dissolvedSulfur_kgS_ha  
    string sockg_expUnitId  
    double sockg_totalDissolvedPhosphorus_kgP_ha  
    double sockg_waterStd_mm  
    string sockg_crop  
    double sockg_crop  
    double sockg_erosionTotalSolidsStd_t_ha  
    double sockg_totalPhosphorusStd_kgP_ha  
    string sockg_fieldId  
    double sockg_dissolvedCopperStd_gCu_ha  
    double sockg_dissolvedCalcium_kgCa_ha  
    string sockg_surfaceOrLeaching  
    double sockg_erosionTotalSuspendedSolids_t_ha  
    double sockg_samplingStartStopInterval  
    string sockg_samplingStartStopInterval  
    double sockg_dissolvedZinc_gZn_ha  
    double sockg_electricalConductivity_ms_cm  
    double sockg_erosionMethod  
    double sockg_dissolvedManganeseStd_gMn_ha  
    double sockg_dissolvedIronStd_gFe_ha  
    double sockg_dissolvedCopper_gCu_ha  
    double sockg_dissolvedIron_gFe_ha  
    double sockg_dissolvedSulfurStd_kgS_ha  
    double sockg_dissolvedSilicon_kgSi_ha  
    double sockg_phStd  
    double sockg_totalDissolvedPhosphorusStd_jgP_ha  
    double sockg_dissovledSodiumStd_kgNa_ha  
    double sockg_dissolvedMagnesiumStd_kgMg_ha  
    double sockg_totalNitrogenStd_kgN_ha  
    double sockg_time  
    string sockg_time  
    double sockg_dissolvedMolybdenum_gMo_ha  
    string sockg_growthStage  
    double sockg_growthStage  
    double sockg_erosionTotalSuspendedSolidsStd_t_ha  
    double sockg_lossesOrDeposition  
    string sockg_lossesOrDeposition  
    double sockg_dissolvedZincStd_gZn_ha  
    double sockg_electricalConductivityStd_ms_cm  
    double sockg_dissolvedBoronStd_gB_ha  
    double sockg_inorganicNitrogenStd_kgN_ha  
    double sockg_dissolvedMolybdenumStd_gMo_ha  
    string sockg_date  
    double sockg_date  
    double sockg_erosionTotalSolids_t_ha  
}
SockgWaterQualityConc {
    double sockg_samplingStartStopInterval  
    string sockg_samplingStartStopInterval  
    double sockg_erosionTotalSuspendedSolidsStd_kg  
    double sockg_erosionSedimentStd_kg  
    string sockg_measWaterQualityConc_UID  
    double sockg_erosionSediment_kg  
    string sockg_treatmentId  
    double sockg_ph  
    double sockg_waterStd_mm  
    string sockg_surfaceOrLeaching  
    double sockg_phStd  
    string sockg_date  
    double sockg_date  
    string sockg_expUnitId  
    double sockg_electricalConductivityStd_ms_cm  
    double sockg_electricalConductivity_ms_cm  
    string sockg_growthStage  
    double sockg_growthStage  
    double sockg_water_mm  
    integer sockg_samplingDepth_cm  
    double sockg_erosionTotalSolids_kg  
    double sockg_erosionTotalSolidsStd_kg  
    string sockg_expUnit_UID  
    double sockg_erosionMethod  
    string sockg_fieldId  
    double sockg_time  
    string sockg_time  
    double sockg_modelIfSimulated  
    string sockg_modelIfSimulated  
    double sockg_erosionTotalSuspendedSolids_kg  
    string sockg_crop  
    double sockg_crop  
}
SockgWeatherObservation {
    double sockg_windSpeed_m_per_s  
    double sockg_precipitation_mm_per_d  
    double sockg_tempMax_degC  
    double sockg_weatherBadValueFlag  
    double sockg_windDirectionDegFromNorth  
    double sockg_atmosphericNitrogenDeposition_kg_per_ha_per_d  
    double sockg_relativeHumidityPercent  
    double sockg_soilTemp5cm_degC  
    double sockg_snow_mm_per_d  
    string sockg_date  
    double sockg_date  
    double sockg_solarRadiationBareSoil_MJ_per_m_squared_per_d  
    double sockg_closedPanEvaporation_mm_per_d  
    double sockg_tempMin_degC  
    double sockg_openPanEvaporation_mm_per_d  
    double sockg_solarRadiationVegetatedGround_MJ_per_m_squared_per_d  
    string sockg_weatherDaily_UID  
    double sockg_soilTemp10cm_degC  
}
SockgWeatherStation {
    double sockg_elevation_m  
    string sockg_weatherStationId  
}
SockgWindErosionArea {
    double sockg_silicon_kg_ha  
    double sockg_electricalConductivity_ms_cm  
    double sockg_potassiumStd_kg_ha  
    double sockg_inorganicNitrogenStd_kgN_ha  
    double sockg_phosphorusStd_kg_ha  
    double sockg_totalNitrogen_kg_ha  
    double sockg_molybdenum_g_ha  
    string sockg_fieldId  
    double sockg_boronStd_g_ha  
    double sockg_samplingStartStopInterval  
    string sockg_samplingStartStopInterval  
    double sockg_iron_g_ha  
    string sockg_treatmentId  
    double sockg_manganese_g_ha  
    double sockg_sulfur_kg_ha  
    double sockg_aluminumStd_kg_ha  
    double sockg_erosionMethod  
    string sockg_expUnit_UID  
    double sockg_totalNitrogenStd_kgN_ha  
    double sockg_lossesOrDeposition  
    string sockg_lossesOrDeposition  
    string sockg_growthStage  
    double sockg_growthStage  
    double sockg_inorganicNitrogen_kgN_ha  
    double sockg_zinc_g_ha  
    string sockg_measWindErosionArea_UID  
    double sockg_calcium_kg_ha  
    double sockg_molybdenumStd_g_ha  
    double sockg_sulfurStd_kg_ha  
    string sockg_crop  
    double sockg_crop  
    double sockg_copper_g_ha  
    double sockg_phosphorus_kg_ha  
    double sockg_magnesium_kg_ha  
    double sockg_ironStd_g_ha  
    double sockg_soilOrganicCarbonStd_kgC_ha  
    double sockg_siliconStd_kg_ha  
    double sockg_calciumStd_kg_ha  
    double sockg_sodiumStd_kg_ha  
    double sockg_nitrateStd_kgN_ha  
    double sockg_nitrate_kg_ha  
    double sockg_soilStd_t_ha  
    double sockg_phStd  
    double sockg_modelIfSimulated  
    string sockg_modelIfSimulated  
    string sockg_expUnitId  
    double sockg_zincStd_g_ha  
    double sockg_potassium_kg_ha  
    double sockg_time  
    string sockg_time  
    double sockg_ph  
    double sockg_sodium_kg_ha  
    double sockg_electricalConductivityStd_ms_cm  
    double sockg_copperStd_g_ha  
    double sockg_magnesiumStd_kg_ha  
    double sockg_manganeseStd_g_ha  
    double sockg_aluminum_kg_ha  
    string sockg_date  
    double sockg_date  
    double sockg_boron_g_ha  
    double sockg_soil_t_ha  
}
SockgYieldNutrientUptake {
    double sockg_fracBoron_gB_ha  
    double sockg_fracProductivityStd_kg_ha  
    double sockg_fracCarbonStd_kgC_ha  
    double sockg_fracNitrogenStd_kgN_ha  
    double sockg_fracZincStd_gZn_ha  
    string sockg_crop  
    double sockg_crop  
    string sockg_measYieldNutUptake_UID  
    double sockg_fracSulfur_kgS_ha  
    double sockg_modelIfSimulated  
    string sockg_modelIfSimulated  
    double sockg_fracMolybdenumStd_gMo_ha  
    double sockg_fracPotassiumStd_kgK_ha  
    string sockg_plantFraction  
    double sockg_plantFraction  
    double sockg_grainWeightKernelYnu_mg  
    double sockg_fracMagnesium_kgMg_ha  
    double sockg_fracCarbon_kgC_ha  
    double sockg_fracManganeseStd_gMn_ha  
    string sockg_treatmentId  
    double sockg_fracCopperStd_gCu_ha  
    double sockg_fracMagnesiumStd_kgMg_ha  
    double sockg_fracIron_gFe_ha  
    double sockg_fracCalcium_kgCa_ha  
    double sockg_fracPhosphorus_kgP_ha  
    string sockg_fieldId  
    double sockg_fracIronStd_gFe_ha  
    double sockg_fracMoisturePercentStd  
    string sockg_expUnit_UID  
    double sockg_fracZinc_gZn_ha  
    double sockg_fracSulfurStd_kgS_ha  
    double sockg_fracPotassium_kgK_ha  
    double sockg_fracMoisturePercent  
    double sockg_fracCopper_gCu_ha  
    double sockg_fracMolybdenum_gMo_ha  
    double sockg_fracCalciumStd_kgCa_ha  
    string sockg_date  
    double sockg_date  
    double sockg_fracBoronStd_gB_ha  
    string sockg_expUnitId  
    double sockg_grainWeightKernelYnuStd_mg  
    double sockg_fracCropProductivity_kg_ha  
    double sockg_fracManganese_gMn_ha  
    string sockg_growthStage  
    double sockg_growthStage  
    double sockg_fracPhosphorusStd_kgP_ha  
    double sockg_fracNitrogen_kgN_ha  
}

SockgAmendment ||--|o SockgPesticide : "sockg_hasPesticide"
SockgCountry ||--|o SockgState : "sockg_hasState"
SockgCounty ||--|o SockgCity : "sockg_hasCity"
SockgDepartment ||--|o SockgOrganization : "sockg_departmentOf"
SockgExperiment ||--|o SockgTreatment : "sockg_hasTreatment"
SockgExperiment ||--|o SockgSite : "sockg_happenedInSite"
SockgExperimentalUnit ||--|o SockgSoilBiologicalSample : "sockg_hasBioSample"
SockgExperimentalUnit ||--|o SockgSoilChemicalSample : "sockg_hasChemSample"
SockgExperimentalUnit ||--|o SockgSoilPhysicalSample : "sockg_hasPhySample"
SockgExperimentalUnit ||--|o SockgHarvestFraction : "sockg_hasHarvestFractionData"
SockgExperimentalUnit ||--|o SockgBioMassMineral : "sockg_hasBioMassMineralData"
SockgExperimentalUnit ||--|o SockgGasSample : "sockg_hasGasSample"
SockgExperimentalUnit ||--|o SockgGrazing : "sockg_hasGrazingData"
SockgExperimentalUnit ||--|o SockgTillage : "sockg_hasTillage"
SockgExperimentalUnit ||--|o SockgAmendment : "sockg_hasAmendment"
SockgExperimentalUnit ||--|o SockgCropGrowthStage : "sockg_tracksGrowth"
SockgExperimentalUnit ||--|o SockgGrazingManagementEvent : "sockg_hasGrazingManagementEvent"
SockgExperimentalUnit ||--|o SockgHarvest : "sockg_isHarvested"
SockgExperimentalUnit ||--|o SockgField : "sockg_locatedInField"
SockgExperimentalUnit ||--|o SockgBioMassEnergy : "sockg_hasBioMassEnergyData"
SockgExperimentalUnit ||--|o SockgBioMassCarbohydrate : "sockg_hasBioMassCarbohydrateData"
SockgExperimentalUnit ||--|o SockgResidueManagementEvent : "sockg_hasResidueManagementEvent"
SockgGasNutrientLoss ||--|o SockgExperimentalUnit : "sockg_hasGasNutrientData"
SockgOrganization ||--|o SockgExperiment : "sockg_fundsExperiment"
SockgPerson ||--|o SockgSite : "sockg_worksIn"
SockgPerson ||--|o SockgDepartment : "sockg_worksAtDepartment"
SockgPerson ||--|o SockgOrganization : "sockg_worksFor"
SockgPlantingEvent ||--|o SockgExperimentalUnit : "sockg_plantingAt"
SockgPublication ||--|o SockgSite : "sockg_studiesSite"
SockgSite ||--|o SockgCounty : "sockg_locatedInCounty"
SockgSite ||--|o SockgState : "sockg_locatedInState"
SockgSite ||--|o SockgCity : "sockg_locatedInCity"
SockgSite ||--|o SockgCountry : "sockg_locatedInCountry"
SockgSite ||--|o SockgField : "sockg_hasField"
SockgState ||--|o SockgCounty : "sockg_hasCounty"
SockgTreatment ||--|o SockgRotation : "sockg_hasRotation"
SockgWaterQualityArea ||--|o SockgExperimentalUnit : "sockg_hasWaterQualityAreaData"
SockgWaterQualityArea ||--|o SockgField : "sockg_waterQualityAreaDataAt"
SockgWaterQualityArea ||--|o SockgTreatment : "sockg_waterQualityAreaTreatment"
SockgWaterQualityConc ||--|o SockgTreatment : "sockg_waterQualityConcTreatment"
SockgWaterQualityConc ||--|o SockgExperimentalUnit : "sockg_hasWaterQualityConcData"
SockgWaterQualityConc ||--|o SockgField : "sockg_waterQualityConcDataAt"
SockgWeatherObservation ||--|o SockgSite : "sockg_weatherRecordedAt"
SockgWeatherObservation ||--|o SockgField : "sockg_weatherAtField"
SockgWeatherStation ||--|o SockgWeatherObservation : "sockg_weatherRecordedBy"
SockgWeatherStation ||--|o SockgField : "sockg_recordsWeatherForField"
SockgWeatherStation ||--|o SockgSite : "sockg_recordsWeatherForSite"
SockgWindErosionArea ||--|o SockgExperimentalUnit : "sockg_hasWindErosionData"
SockgWindErosionArea ||--|o SockgTreatment : "sockg_windErosionTreatment"
SockgWindErosionArea ||--|o SockgField : "sockg_windErosionDataAt"
SockgYieldNutrientUptake ||--|o SockgExperimentalUnit : "sockg_hasYieldNutrUptakeData"
SockgYieldNutrientUptake ||--|o SockgField : "sockg_yieldNutrUptakeDataAt"
SockgYieldNutrientUptake ||--|o SockgTreatment : "sockg_yieldNutrUptakeTreatment"

```


## IRI prefixes

* linkml: https://w3id.org/linkml/
* sockg: http://www.semanticweb.org/sockg/ontologies/2024/0/soil-carbon-ontology/
* xsd: http://www.w3.org/2001/XMLSchema#



## Classes

| Class | Description |
| --- | --- |
| [SockgAmendment](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgAmendment.md) | No type description provided<br/>| 
| [SockgBioMassCarbohydrate](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgBioMassCarbohydrate.md) | No type description provided<br/>| 
| [SockgBioMassEnergy](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgBioMassEnergy.md) | No type description provided<br/>| 
| [SockgBioMassMineral](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgBioMassMineral.md) | No type description provided<br/>| 
| [SockgBook](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgBook.md) | No type description provided<br/>| 
| [SockgCity](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgCity.md) | No type description provided<br/>| 
| [SockgCountry](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgCountry.md) | No type description provided<br/>| 
| [SockgCounty](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgCounty.md) | No type description provided<br/>| 
| [SockgCropGrowthStage](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgCropGrowthStage.md) | No type description provided<br/>| 
| [SockgDepartment](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgDepartment.md) | No type description provided<br/>| 
| [SockgExperiment](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgExperiment.md) | No type description provided<br/>| 
| [SockgExperimentalUnit](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgExperimentalUnit.md) | No type description provided<br/>| 
| [SockgField](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgField.md) | No type description provided<br/>| 
| [SockgGasNutrientLoss](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgGasNutrientLoss.md) | No type description provided<br/>| 
| [SockgGasSample](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgGasSample.md) | No type description provided<br/>| 
| [SockgGrazing](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgGrazing.md) | No type description provided<br/>| 
| [SockgGrazingManagementEvent](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgGrazingManagementEvent.md) | No type description provided<br/>| 
| [SockgHarvest](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgHarvest.md) | No type description provided<br/>| 
| [SockgHarvestFraction](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgHarvestFraction.md) | No type description provided<br/>| 
| [SockgNutrientEfficiency](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgNutrientEfficiency.md) | No type description provided<br/>| 
| [SockgOrganization](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgOrganization.md) | No type description provided<br/>| 
| [SockgPerson](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgPerson.md) | No type description provided<br/>| 
| [SockgPesticide](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgPesticide.md) | No type description provided<br/>| 
| [SockgPlantingEvent](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgPlantingEvent.md) | No type description provided<br/>| 
| [SockgProject](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgProject.md) | No type description provided<br/>| 
| [SockgPublication](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgPublication.md) | No type description provided<br/>| 
| [SockgResidueManagementEvent](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgResidueManagementEvent.md) | No type description provided<br/>| 
| [SockgRotation](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgRotation.md) | No type description provided<br/>| 
| [SockgSite](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgSite.md) | No type description provided<br/>| 
| [SockgSoilBiologicalSample](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgSoilBiologicalSample.md) | No type description provided<br/>| 
| [SockgSoilChemicalSample](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgSoilChemicalSample.md) | No type description provided<br/>| 
| [SockgSoilCover](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgSoilCover.md) | No type description provided<br/>| 
| [SockgSoilPhysicalSample](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgSoilPhysicalSample.md) | No type description provided<br/>| 
| [SockgState](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgState.md) | No type description provided<br/>| 
| [SockgTillage](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgTillage.md) | No type description provided<br/>| 
| [SockgTreatment](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgTreatment.md) | No type description provided<br/>| 
| [SockgVersion](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgVersion.md) | No type description provided<br/>| 
| [SockgWaterQualityArea](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgWaterQualityArea.md) | No type description provided<br/>| 
| [SockgWaterQualityConc](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgWaterQualityConc.md) | No type description provided<br/>| 
| [SockgWeatherObservation](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgWeatherObservation.md) | No type description provided<br/>| 
| [SockgWeatherStation](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgWeatherStation.md) | No type description provided<br/>| 
| [SockgWindErosionArea](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgWindErosionArea.md) | No type description provided<br/>| 
| [SockgYieldNutrientUptake](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/SockgYieldNutrientUptake.md) | No type description provided<br/>| 





## Slots

| Slot | Description |
| --- | --- |
| [sockg_aboveGroundBiomass_kg_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_aboveGroundBiomass_kg_per_ha.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_aboveGroundBiomassCarbon_kgC_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_aboveGroundBiomassCarbon_kgC_per_ha.md) | No slot description provided<br/>6995 occurrences with subject type sockg:Grazing and object type xsd:double.|
| [sockg_aboveGroundBiomassCarbonStd_kgC_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_aboveGroundBiomassCarbonStd_kgC_per_ha.md) | No slot description provided<br/>6995 occurrences with subject type sockg:Grazing and object type xsd:double.|
| [sockg_aboveGroundBiomassDry_kg_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_aboveGroundBiomassDry_kg_per_ha.md) | No slot description provided<br/>6995 occurrences with subject type sockg:Grazing and object type xsd:double.|
| [sockg_aboveGroundBiomassDryStd_kg_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_aboveGroundBiomassDryStd_kg_per_ha.md) | No slot description provided<br/>6995 occurrences with subject type sockg:Grazing and object type xsd:double.|
| [sockg_aboveGroundBiomassNitrogen_kgN_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_aboveGroundBiomassNitrogen_kgN_per_ha.md) | No slot description provided<br/>6995 occurrences with subject type sockg:Grazing and object type xsd:double.|
| [sockg_aboveGroundBiomassNitrogenStd_kgN_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_aboveGroundBiomassNitrogenStd_kgN_per_ha.md) | No slot description provided<br/>6995 occurrences with subject type sockg:Grazing and object type xsd:double.|
| [sockg_aboveGroundBiomassStd_kg_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_aboveGroundBiomassStd_kg_per_ha.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_abovegroundNetPrimaryProductivityCarbon_kgC_per_ha_per_yr](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_abovegroundNetPrimaryProductivityCarbon_kgC_per_ha_per_yr.md) | No slot description provided<br/>6995 occurrences with subject type sockg:Grazing and object type xsd:double.|
| [sockg_abovegroundNetPrimaryProductivityCarbonStd_kgC_per_ha_per_yr](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_abovegroundNetPrimaryProductivityCarbonStd_kgC_per_ha_per_yr.md) | No slot description provided<br/>6995 occurrences with subject type sockg:Grazing and object type xsd:double.|
| [sockg_abovegroundNetPrimaryProductivityNitrogen_kgN_per_ha_per_yr](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_abovegroundNetPrimaryProductivityNitrogen_kgN_per_ha_per_yr.md) | No slot description provided<br/>6995 occurrences with subject type sockg:Grazing and object type xsd:double.|
| [sockg_abovegroundNetPrimaryProductivityNitrogenStd_kgN_per_ha_per_yr](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_abovegroundNetPrimaryProductivityNitrogenStd_kgN_per_ha_per_yr.md) | No slot description provided<br/>6995 occurrences with subject type sockg:Grazing and object type xsd:double.|
| [sockg_acidDetFiber_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_acidDetFiber_g_per_kg.md) | No slot description provided<br/>1367 occurrences with subject type sockg:BioMassCarbohydrate and object type xsd:double.|
| [sockg_acidDetFiberStd_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_acidDetFiberStd_g_per_kg.md) | No slot description provided<br/>1367 occurrences with subject type sockg:BioMassCarbohydrate and object type xsd:double.|
| [sockg_acidInsolubleLignin_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_acidInsolubleLignin_g_per_kg.md) | No slot description provided<br/>1367 occurrences with subject type sockg:BioMassCarbohydrate and object type xsd:double.|
| [sockg_acidInsolubleLigninStd_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_acidInsolubleLigninStd_g_per_kg.md) | No slot description provided<br/>1367 occurrences with subject type sockg:BioMassCarbohydrate and object type xsd:double.|
| [sockg_acidPhosphatase_mg_per_kg_per_hr](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_acidPhosphatase_mg_per_kg_per_hr.md) | No slot description provided<br/>18222 occurrences with subject type sockg:SoilBiologicalSample and object type xsd:double.|
| [sockg_acidPhosphataseStd_mg_per_kg_per_hr](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_acidPhosphataseStd_mg_per_kg_per_hr.md) | No slot description provided<br/>18222 occurrences with subject type sockg:SoilBiologicalSample and object type xsd:double.|
| [sockg_acidSolubleLignin_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_acidSolubleLignin_g_per_kg.md) | No slot description provided<br/>1367 occurrences with subject type sockg:BioMassCarbohydrate and object type xsd:double.|
| [sockg_acidSolubleLigninStd_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_acidSolubleLigninStd_g_per_kg.md) | No slot description provided<br/>1367 occurrences with subject type sockg:BioMassCarbohydrate and object type xsd:double.|
| [sockg_aggregationPercent](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_aggregationPercent.md) | No slot description provided<br/>28082 occurrences with subject type sockg:SoilPhysicalSample and object type xsd:double.|
| [sockg_agronomicEfficiency_kg_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_agronomicEfficiency_kg_kg.md) | No slot description provided<br/>2791 occurrences with subject type sockg:NutrientEfficiency and object type xsd:double.|
| [sockg_airTemperature_degC](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_airTemperature_degC.md) | No slot description provided<br/>107354 occurrences with subject type sockg:GasSample and object type xsd:double.|
| [sockg_airTemperatureStd_degC](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_airTemperatureStd_degC.md) | No slot description provided<br/>107354 occurrences with subject type sockg:GasSample and object type xsd:double.|
| [sockg_alkPhosphatase_mg_per_kg_per_hr](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_alkPhosphatase_mg_per_kg_per_hr.md) | No slot description provided<br/>18222 occurrences with subject type sockg:SoilBiologicalSample and object type xsd:double.|
| [sockg_alkPhosphataseStd_mg_per_kg_per_hr](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_alkPhosphataseStd_mg_per_kg_per_hr.md) | No slot description provided<br/>18222 occurrences with subject type sockg:SoilBiologicalSample and object type xsd:double.|
| [sockg_aluminum_kg_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_aluminum_kg_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_aluminumConcentration_mg_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_aluminumConcentration_mg_per_kg.md) | No slot description provided<br/>6723 occurrences with subject type sockg:BioMassMineral and object type xsd:double.|
| [sockg_aluminumConcentrationStd_mg_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_aluminumConcentrationStd_mg_per_kg.md) | No slot description provided<br/>6723 occurrences with subject type sockg:BioMassMineral and object type xsd:double.|
| [sockg_aluminumStd_kg_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_aluminumStd_kg_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_amendmentPlacement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_amendmentPlacement.md) | No slot description provided<br/>22264 occurrences with subject type sockg:Amendment and object type string.<br/>15532 occurrences with subject type sockg:Amendment and object type xsd:double.|
| [sockg_ammoniaNitrogen_kg_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_ammoniaNitrogen_kg_ha.md) | No slot description provided<br/>748 occurrences with subject type sockg:GasNutrientLoss and object type xsd:double.|
| [sockg_ammoniaNitrogenStd_kg_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_ammoniaNitrogenStd_kg_ha.md) | No slot description provided<br/>748 occurrences with subject type sockg:GasNutrientLoss and object type xsd:double.|
| [sockg_ammonium_mgN_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_ammonium_mgN_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_ammoniumStd_mgN_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_ammoniumStd_mgN_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_animalClass](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_animalClass.md) | No slot description provided<br/>1833 occurrences with subject type sockg:GrazingManagementEvent and object type string.<br/>118 occurrences with subject type sockg:GrazingManagementEvent and object type xsd:double.|
| [sockg_animalSpecies](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_animalSpecies.md) | No slot description provided<br/>1951 occurrences with subject type sockg:GrazingManagementEvent and object type string.|
| [sockg_arabinan_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_arabinan_g_per_kg.md) | No slot description provided<br/>1367 occurrences with subject type sockg:BioMassCarbohydrate and object type xsd:double.|
| [sockg_arabinanStd_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_arabinanStd_g_per_kg.md) | No slot description provided<br/>1367 occurrences with subject type sockg:BioMassCarbohydrate and object type xsd:double.|
| [sockg_ash_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_ash_g_per_kg.md) | No slot description provided<br/>1367 occurrences with subject type sockg:BioMassCarbohydrate and object type xsd:double.|
| [sockg_ashStd_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_ashStd_g_per_kg.md) | No slot description provided<br/>1367 occurrences with subject type sockg:BioMassCarbohydrate and object type xsd:double.|
| [sockg_atmosphericNitrogenDeposition_kg_per_ha_per_d](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_atmosphericNitrogenDeposition_kg_per_ha_per_d.md) | No slot description provided<br/>147305 occurrences with subject type sockg:WeatherObservation and object type xsd:double.|
| [sockg_author](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_author.md) | No slot description provided<br/>114 occurrences with subject type sockg:Publication and object type string.|
| [sockg_belowGroundBiomassCarbon_kgC_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_belowGroundBiomassCarbon_kgC_per_ha.md) | No slot description provided<br/>6995 occurrences with subject type sockg:Grazing and object type xsd:double.|
| [sockg_belowGroundBiomassCarbonStd_kgC_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_belowGroundBiomassCarbonStd_kgC_per_ha.md) | No slot description provided<br/>6995 occurrences with subject type sockg:Grazing and object type xsd:double.|
| [sockg_belowGroundBiomassNitrogen_kgN_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_belowGroundBiomassNitrogen_kgN_per_ha.md) | No slot description provided<br/>6995 occurrences with subject type sockg:Grazing and object type xsd:double.|
| [sockg_belowGroundBiomassNitrogenStd_kgN_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_belowGroundBiomassNitrogenStd_kgN_per_ha.md) | No slot description provided<br/>6995 occurrences with subject type sockg:Grazing and object type xsd:double.|
| [sockg_belowgroundNetPrimaryProductivityCarbon_kgC_per_ha_per_yr](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_belowgroundNetPrimaryProductivityCarbon_kgC_per_ha_per_yr.md) | No slot description provided<br/>6995 occurrences with subject type sockg:Grazing and object type xsd:double.|
| [sockg_belowgroundNetPrimaryProductivityCarbonStd_kgC_per_ha_per_yr](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_belowgroundNetPrimaryProductivityCarbonStd_kgC_per_ha_per_yr.md) | No slot description provided<br/>6995 occurrences with subject type sockg:Grazing and object type xsd:double.|
| [sockg_belowgroundNetPrimaryProductivityNitrogen_kgN_per_ha_per_yr](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_belowgroundNetPrimaryProductivityNitrogen_kgN_per_ha_per_yr.md) | No slot description provided<br/>6995 occurrences with subject type sockg:Grazing and object type xsd:double.|
| [sockg_belowgroundNetPrimaryProductivityNitrogenStd_kgN_per_ha_per_yr](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_belowgroundNetPrimaryProductivityNitrogenStd_kgN_per_ha_per_yr.md) | No slot description provided<br/>6995 occurrences with subject type sockg:Grazing and object type xsd:double.|
| [sockg_biomassNitrogenPercentage](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_biomassNitrogenPercentage.md) | No slot description provided<br/>6995 occurrences with subject type sockg:Grazing and object type xsd:double.|
| [sockg_bookName](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_bookName.md) | No slot description provided<br/>2 occurrences with subject type sockg:Book and object type string.|
| [sockg_boron_g_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_boron_g_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_boronConcentration_mg_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_boronConcentration_mg_per_kg.md) | No slot description provided<br/>6723 occurrences with subject type sockg:BioMassMineral and object type xsd:double.|
| [sockg_boronConcentrationStd_mg_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_boronConcentrationStd_mg_per_kg.md) | No slot description provided<br/>6723 occurrences with subject type sockg:BioMassMineral and object type xsd:double.|
| [sockg_boronStd_g_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_boronStd_g_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_broadleafOrGrass](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_broadleafOrGrass.md) | No slot description provided<br/>6995 occurrences with subject type sockg:Grazing and object type string.|
| [sockg_bulkDensity_g_per_cm_cubed](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_bulkDensity_g_per_cm_cubed.md) | No slot description provided<br/>28082 occurrences with subject type sockg:SoilPhysicalSample and object type xsd:double.|
| [sockg_bulkDensityStd_g_per_cm_cubed](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_bulkDensityStd_g_per_cm_cubed.md) | No slot description provided<br/>28082 occurrences with subject type sockg:SoilPhysicalSample and object type xsd:double.|
| [sockg_burnIntensity](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_burnIntensity.md) | No slot description provided<br/>1951 occurrences with subject type sockg:GrazingManagementEvent and object type xsd:double.|
| [sockg_calcium_kg_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_calcium_kg_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_calciumConcentration_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_calciumConcentration_g_per_kg.md) | No slot description provided<br/>6723 occurrences with subject type sockg:BioMassMineral and object type xsd:double.|
| [sockg_calciumConcentrationStd_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_calciumConcentrationStd_g_per_kg.md) | No slot description provided<br/>6723 occurrences with subject type sockg:BioMassMineral and object type xsd:double.|
| [sockg_calciumStd_kg_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_calciumStd_kg_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_carbon_kgC_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_carbon_kgC_per_ha.md) | No slot description provided<br/>9470 occurrences with subject type sockg:HarvestFraction and object type xsd:double.|
| [sockg_carbonConcentration_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_carbonConcentration_g_per_kg.md) | No slot description provided<br/>6723 occurrences with subject type sockg:BioMassMineral and object type xsd:double.|
| [sockg_carbonConcentrationStd_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_carbonConcentrationStd_g_per_kg.md) | No slot description provided<br/>6723 occurrences with subject type sockg:BioMassMineral and object type xsd:double.|
| [sockg_carbonDioxide_gC_per_ha_per_d](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_carbonDioxide_gC_per_ha_per_d.md) | No slot description provided<br/>107354 occurrences with subject type sockg:GasSample and object type xsd:double.|
| [sockg_carbonDioxideStd_gC_per_ha_per_d](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_carbonDioxideStd_gC_per_ha_per_d.md) | No slot description provided<br/>107354 occurrences with subject type sockg:GasSample and object type xsd:double.|
| [sockg_carbonMicrobialBiomass_mgC_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_carbonMicrobialBiomass_mgC_per_kg.md) | No slot description provided<br/>18222 occurrences with subject type sockg:SoilBiologicalSample and object type xsd:double.|
| [sockg_carbonMicrobialBiomassStd_mgC_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_carbonMicrobialBiomassStd_mgC_per_kg.md) | No slot description provided<br/>18222 occurrences with subject type sockg:SoilBiologicalSample and object type xsd:double.|
| [sockg_carbonStd_kgC_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_carbonStd_kgC_per_ha.md) | No slot description provided<br/>9470 occurrences with subject type sockg:HarvestFraction and object type xsd:double.|
| [sockg_cationExchangeCapacity_cmol_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_cationExchangeCapacity_cmol_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_cationExchangeCapacityStd_cmol_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_cationExchangeCapacityStd_cmol_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_chamberPlacement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_chamberPlacement.md) | No slot description provided<br/>103543 occurrences with subject type sockg:GasSample and object type string.<br/>3811 occurrences with subject type sockg:GasSample and object type xsd:double.|
| [sockg_changeInManagement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_changeInManagement.md) | No slot description provided<br/>3809 occurrences with subject type sockg:ExperimentalUnit and object type xsd:double.|
| [sockg_chlorineConcentration_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_chlorineConcentration_g_per_kg.md) | No slot description provided<br/>6723 occurrences with subject type sockg:BioMassMineral and object type xsd:double.|
| [sockg_chlorineConcentrationStd_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_chlorineConcentrationStd_g_per_kg.md) | No slot description provided<br/>6723 occurrences with subject type sockg:BioMassMineral and object type xsd:double.|
| [sockg_citation](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_citation.md) | No slot description provided<br/>114 occurrences with subject type sockg:Publication and object type string.|
| [sockg_cityName](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_cityName.md) | No slot description provided<br/>33 occurrences with subject type sockg:City and object type string.|
| [sockg_clayPercent](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_clayPercent.md) | No slot description provided<br/>28082 occurrences with subject type sockg:SoilPhysicalSample and object type xsd:double.|
| [sockg_closedPanEvaporation_mm_per_d](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_closedPanEvaporation_mm_per_d.md) | No slot description provided<br/>147305 occurrences with subject type sockg:WeatherObservation and object type xsd:double.|
| [sockg_copper_g_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_copper_g_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_copperConcentration_mg_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_copperConcentration_mg_per_kg.md) | No slot description provided<br/>6723 occurrences with subject type sockg:BioMassMineral and object type xsd:double.|
| [sockg_copperConcentrationStd_mg_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_copperConcentrationStd_mg_per_kg.md) | No slot description provided<br/>6723 occurrences with subject type sockg:BioMassMineral and object type xsd:double.|
| [sockg_copperStd_g_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_copperStd_g_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_cornEarHeight_cm](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_cornEarHeight_cm.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_cornEarHeightStd_cm](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_cornEarHeightStd_cm.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_correspondingAuthor](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_correspondingAuthor.md) | No slot description provided<br/>105 occurrences with subject type sockg:Publication and object type string.<br/>9 occurrences with subject type sockg:Publication and object type xsd:double.|
| [sockg_countryName](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_countryName.md) | No slot description provided<br/>3 occurrences with subject type sockg:Country and object type string.|
| [sockg_countyName](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_countyName.md) | No slot description provided<br/>33 occurrences with subject type sockg:County and object type string.|
| [sockg_coverCrop](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_coverCrop.md) | No slot description provided<br/>575 occurrences with subject type sockg:Treatment and object type xsd:double.<br/>194 occurrences with subject type sockg:Treatment and object type string.|
| [sockg_crop](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_crop.md) | No slot description provided<br/>2791 occurrences with subject type sockg:NutrientEfficiency and object type string.<br/>105046 occurrences with subject type sockg:GasSample and object type string.<br/>6723 occurrences with subject type sockg:BioMassMineral and object type string.<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type string.<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.<br/>1367 occurrences with subject type sockg:BioMassCarbohydrate and object type string.<br/>799 occurrences with subject type sockg:BioMassEnergy and object type string.<br/>2308 occurrences with subject type sockg:GasSample and object type xsd:double.<br/>553 occurrences with subject type sockg:WaterQualityConc and object type string.<br/>698 occurrences with subject type sockg:GasNutrientLoss and object type xsd:double.<br/>926 occurrences with subject type sockg:WaterQualityConc and object type xsd:double.<br/>50 occurrences with subject type sockg:GasNutrientLoss and object type string.<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_crudeProtein_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_crudeProtein_g_per_kg.md) | No slot description provided<br/>1367 occurrences with subject type sockg:BioMassCarbohydrate and object type xsd:double.|
| [sockg_crudeProteinStd_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_crudeProteinStd_g_per_kg.md) | No slot description provided<br/>1367 occurrences with subject type sockg:BioMassCarbohydrate and object type xsd:double.|
| [sockg_cultivar](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_cultivar.md) | No slot description provided<br/>20817 occurrences with subject type sockg:PlantingEvent and object type string.<br/>2633 occurrences with subject type sockg:PlantingEvent and object type xsd:double.|
| [sockg_date](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_date.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type string.<br/>147304 occurrences with subject type sockg:WeatherObservation and object type string.<br/>107354 occurrences with subject type sockg:GasSample and object type string.<br/>28082 occurrences with subject type sockg:SoilPhysicalSample and object type string.<br/>6995 occurrences with subject type sockg:Grazing and object type string.<br/>4896 occurrences with subject type sockg:CropGrowthStage and object type string.<br/>18222 occurrences with subject type sockg:SoilBiologicalSample and object type string.<br/>18304 occurrences with subject type sockg:Harvest and object type string.<br/>6723 occurrences with subject type sockg:BioMassMineral and object type string.<br/>3308 occurrences with subject type sockg:ResidueManagementEvent and object type string.<br/>2791 occurrences with subject type sockg:NutrientEfficiency and object type string.<br/>1367 occurrences with subject type sockg:BioMassCarbohydrate and object type string.<br/>1479 occurrences with subject type sockg:WaterQualityConc and object type string.<br/>748 occurrences with subject type sockg:GasNutrientLoss and object type string.<br/>1034 occurrences with subject type sockg:SoilCover and object type string.<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type string.<br/>52 occurrences with subject type sockg:Harvest and object type xsd:double.<br/>799 occurrences with subject type sockg:BioMassEnergy and object type string.<br/>667 occurrences with subject type sockg:WaterQualityArea and object type string.<br/>15 occurrences with subject type sockg:WindErosionArea and object type string.<br/>1 occurrences with subject type sockg:WeatherObservation and object type xsd:double.|
| [sockg_departmentName](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_departmentName.md) | No slot description provided<br/>33 occurrences with subject type sockg:Department and object type string.|
| [sockg_departmentOf](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_departmentOf.md) | No slot description provided<br/>11 occurrences with subject type sockg:Department and object type sockg:Organization.|
| [sockg_depth_cm](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_depth_cm.md) | No slot description provided<br/>23450 occurrences with subject type sockg:PlantingEvent and object type xsd:double.|
| [sockg_dissolvedBoron_gB_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_dissolvedBoron_gB_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_dissolvedBoronStd_gB_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_dissolvedBoronStd_gB_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_dissolvedCalcium_kgCa_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_dissolvedCalcium_kgCa_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_dissolvedCalciumStd_kgCa_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_dissolvedCalciumStd_kgCa_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_dissolvedCopper_gCu_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_dissolvedCopper_gCu_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_dissolvedCopperStd_gCu_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_dissolvedCopperStd_gCu_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_dissolvedIron_gFe_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_dissolvedIron_gFe_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_dissolvedIronStd_gFe_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_dissolvedIronStd_gFe_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_dissolvedMagnesium_kgMg_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_dissolvedMagnesium_kgMg_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_dissolvedMagnesiumStd_kgMg_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_dissolvedMagnesiumStd_kgMg_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_dissolvedManganese_gMn_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_dissolvedManganese_gMn_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_dissolvedManganeseStd_gMn_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_dissolvedManganeseStd_gMn_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_dissolvedMolybdenum_gMo_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_dissolvedMolybdenum_gMo_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_dissolvedMolybdenumStd_gMo_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_dissolvedMolybdenumStd_gMo_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_dissolvedPotassium_kgK_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_dissolvedPotassium_kgK_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_dissolvedPotassiumStd_kgK_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_dissolvedPotassiumStd_kgK_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_dissolvedSilicon_kgSi_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_dissolvedSilicon_kgSi_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_dissolvedSodium_kgNa_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_dissolvedSodium_kgNa_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_dissolvedSulfur_kgS_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_dissolvedSulfur_kgS_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_dissolvedSulfurStd_kgS_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_dissolvedSulfurStd_kgS_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_dissolvedZinc_gZn_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_dissolvedZinc_gZn_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_dissolvedZincStd_gZn_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_dissolvedZincStd_gZn_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_dissovledSiliconStd_kgSi_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_dissovledSiliconStd_kgSi_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_dissovledSodiumStd_kgNa_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_dissovledSodiumStd_kgNa_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_driedHarvestedResidue_kg_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_driedHarvestedResidue_kg_per_ha.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_driedHarvestedResidueStd_kg_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_driedHarvestedResidueStd_kg_per_ha.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_dryBiomass_kg_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_dryBiomass_kg_per_ha.md) | No slot description provided<br/>9470 occurrences with subject type sockg:HarvestFraction and object type xsd:double.|
| [sockg_dryBiomassStd_kg_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_dryBiomassStd_kg_per_ha.md) | No slot description provided<br/>9470 occurrences with subject type sockg:HarvestFraction and object type xsd:double.|
| [sockg_electricalConductivity_ms_cm](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_electricalConductivity_ms_cm.md) | No slot description provided<br/>1479 occurrences with subject type sockg:WaterQualityConc and object type xsd:double.<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_electricalConductivity_siemens_per_m](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_electricalConductivity_siemens_per_m.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_electricalConductivityStd_ms_cm](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_electricalConductivityStd_ms_cm.md) | No slot description provided<br/>1479 occurrences with subject type sockg:WaterQualityConc and object type xsd:double.<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_electricalConductivityStd_siemens_per_m](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_electricalConductivityStd_siemens_per_m.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_elevation_m](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_elevation_m.md) | No slot description provided<br/>58 occurrences with subject type sockg:Field and object type xsd:double.<br/>12 occurrences with subject type sockg:WeatherStation and object type xsd:double.|
| [sockg_email](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_email.md) | No slot description provided<br/>86 occurrences with subject type sockg:Person and object type string.<br/>12 occurrences with subject type sockg:Person and object type xsd:double.|
| [sockg_endDate](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_endDate.md) | No slot description provided<br/>37796 occurrences with subject type sockg:Amendment and object type xsd:double.<br/>2026 occurrences with subject type sockg:ExperimentalUnit and object type xsd:double.<br/>1783 occurrences with subject type sockg:ExperimentalUnit and object type string.<br/>1951 occurrences with subject type sockg:GrazingManagementEvent and object type string.<br/>55 occurrences with subject type sockg:Experiment and object type string.|
| [sockg_equipmentType](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_equipmentType.md) | No slot description provided<br/>3044 occurrences with subject type sockg:ResidueManagementEvent and object type string.<br/>264 occurrences with subject type sockg:ResidueManagementEvent and object type xsd:double.|
| [sockg_erosionMethod](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_erosionMethod.md) | No slot description provided<br/>1479 occurrences with subject type sockg:WaterQualityConc and object type xsd:double.<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_erosionSediment_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_erosionSediment_kg.md) | No slot description provided<br/>1479 occurrences with subject type sockg:WaterQualityConc and object type xsd:double.|
| [sockg_erosionSediment_t_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_erosionSediment_t_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_erosionSedimentStd_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_erosionSedimentStd_kg.md) | No slot description provided<br/>1479 occurrences with subject type sockg:WaterQualityConc and object type xsd:double.|
| [sockg_erosionSedimentStd_t_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_erosionSedimentStd_t_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_erosionTotalSolids_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_erosionTotalSolids_kg.md) | No slot description provided<br/>1479 occurrences with subject type sockg:WaterQualityConc and object type xsd:double.|
| [sockg_erosionTotalSolids_t_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_erosionTotalSolids_t_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_erosionTotalSolidsStd_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_erosionTotalSolidsStd_kg.md) | No slot description provided<br/>1479 occurrences with subject type sockg:WaterQualityConc and object type xsd:double.|
| [sockg_erosionTotalSolidsStd_t_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_erosionTotalSolidsStd_t_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_erosionTotalSuspendedSolids_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_erosionTotalSuspendedSolids_kg.md) | No slot description provided<br/>1479 occurrences with subject type sockg:WaterQualityConc and object type xsd:double.|
| [sockg_erosionTotalSuspendedSolids_t_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_erosionTotalSuspendedSolids_t_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_erosionTotalSuspendedSolidsStd_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_erosionTotalSuspendedSolidsStd_kg.md) | No slot description provided<br/>1479 occurrences with subject type sockg:WaterQualityConc and object type xsd:double.|
| [sockg_erosionTotalSuspendedSolidsStd_t_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_erosionTotalSuspendedSolidsStd_t_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_experimentName](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_experimentName.md) | No slot description provided<br/>55 occurrences with subject type sockg:Experiment and object type string.|
| [sockg_expUnit_UID](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_expUnit_UID.md) | No slot description provided<br/>3809 occurrences with subject type sockg:ExperimentalUnit and object type string.<br/>2791 occurrences with subject type sockg:NutrientEfficiency and object type string.<br/>748 occurrences with subject type sockg:GasNutrientLoss and object type string.<br/>1479 occurrences with subject type sockg:WaterQualityConc and object type string.<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type string.<br/>15 occurrences with subject type sockg:WindErosionArea and object type string.|
| [sockg_expUnitId](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_expUnitId.md) | No slot description provided<br/>3809 occurrences with subject type sockg:ExperimentalUnit and object type string.<br/>2791 occurrences with subject type sockg:NutrientEfficiency and object type string.<br/>748 occurrences with subject type sockg:GasNutrientLoss and object type string.<br/>1479 occurrences with subject type sockg:WaterQualityConc and object type string.<br/>667 occurrences with subject type sockg:WaterQualityArea and object type string.<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type string.<br/>15 occurrences with subject type sockg:WindErosionArea and object type string.|
| [sockg_extractableCalcium_mgCa_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_extractableCalcium_mgCa_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_extractableCalciumStd_mgCa_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_extractableCalciumStd_mgCa_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_extractableCopper_mgCu_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_extractableCopper_mgCu_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_extractableCopperStd_mgCu_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_extractableCopperStd_mgCu_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_extractableIron_mgFe_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_extractableIron_mgFe_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_extractableIronStd_mgFe_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_extractableIronStd_mgFe_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_extractableMagnesium_mgMg_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_extractableMagnesium_mgMg_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_extractableMagnesiumStd_mgMg_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_extractableMagnesiumStd_mgMg_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_extractableManganese_mgMN_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_extractableManganese_mgMN_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_extractableManganeseStd_mgMN_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_extractableManganeseStd_mgMN_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_extractableZinc_mgZn_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_extractableZinc_mgZn_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_extractableZincStd_mgZn_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_extractableZincStd_mgZn_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_fertilizerAmendmentClass](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fertilizerAmendmentClass.md) | No slot description provided<br/>653 occurrences with subject type sockg:Treatment and object type string.<br/>116 occurrences with subject type sockg:Treatment and object type xsd:double.|
| [sockg_fieldId](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fieldId.md) | No slot description provided<br/>2791 occurrences with subject type sockg:NutrientEfficiency and object type string.<br/>748 occurrences with subject type sockg:GasNutrientLoss and object type string.<br/>667 occurrences with subject type sockg:WaterQualityArea and object type string.<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type string.<br/>1479 occurrences with subject type sockg:WaterQualityConc and object type string.<br/>15 occurrences with subject type sockg:WindErosionArea and object type string.<br/>58 occurrences with subject type sockg:Field and object type string.|
| [sockg_firstName](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_firstName.md) | No slot description provided<br/>98 occurrences with subject type sockg:Person and object type string.|
| [sockg_fracBoron_gB_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fracBoron_gB_ha.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.|
| [sockg_fracBoronStd_gB_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fracBoronStd_gB_ha.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.|
| [sockg_fracCalcium_kgCa_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fracCalcium_kgCa_ha.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.|
| [sockg_fracCalciumStd_kgCa_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fracCalciumStd_kgCa_ha.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.|
| [sockg_fracCarbon_kgC_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fracCarbon_kgC_ha.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.|
| [sockg_fracCarbonStd_kgC_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fracCarbonStd_kgC_ha.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.|
| [sockg_fracCopper_gCu_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fracCopper_gCu_ha.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.|
| [sockg_fracCopperStd_gCu_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fracCopperStd_gCu_ha.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.|
| [sockg_fracCropProductivity_kg_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fracCropProductivity_kg_ha.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.|
| [sockg_fracIron_gFe_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fracIron_gFe_ha.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.|
| [sockg_fracIronStd_gFe_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fracIronStd_gFe_ha.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.|
| [sockg_fracMagnesium_kgMg_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fracMagnesium_kgMg_ha.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.|
| [sockg_fracMagnesiumStd_kgMg_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fracMagnesiumStd_kgMg_ha.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.|
| [sockg_fracManganese_gMn_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fracManganese_gMn_ha.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.|
| [sockg_fracManganeseStd_gMn_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fracManganeseStd_gMn_ha.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.|
| [sockg_fracMoisturePercent](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fracMoisturePercent.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.|
| [sockg_fracMoisturePercentStd](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fracMoisturePercentStd.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.|
| [sockg_fracMolybdenum_gMo_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fracMolybdenum_gMo_ha.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.|
| [sockg_fracMolybdenumStd_gMo_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fracMolybdenumStd_gMo_ha.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.|
| [sockg_fracNitrogen_kg_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fracNitrogen_kg_ha.md) | No slot description provided<br/>2791 occurrences with subject type sockg:NutrientEfficiency and object type xsd:double.|
| [sockg_fracNitrogen_kgN_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fracNitrogen_kgN_ha.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.|
| [sockg_fracNitrogenStd_kgN_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fracNitrogenStd_kgN_ha.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.|
| [sockg_fracPhosphorus_kgP_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fracPhosphorus_kgP_ha.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.|
| [sockg_fracPhosphorusStd_kgP_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fracPhosphorusStd_kgP_ha.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.|
| [sockg_fracPotassium_kgK_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fracPotassium_kgK_ha.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.|
| [sockg_fracPotassiumStd_kgK_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fracPotassiumStd_kgK_ha.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.|
| [sockg_fracProductivityStd_kg_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fracProductivityStd_kg_ha.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.|
| [sockg_fracSulfur_kgS_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fracSulfur_kgS_ha.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.|
| [sockg_fracSulfurStd_kgS_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fracSulfurStd_kgS_ha.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.|
| [sockg_fracZinc_gZn_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fracZinc_gZn_ha.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.|
| [sockg_fracZincStd_gZn_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fracZincStd_gZn_ha.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.|
| [sockg_fundsExperiment](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_fundsExperiment.md) | No slot description provided<br/>3 occurrences with subject type sockg:Organization and object type sockg:Experiment.|
| [sockg_galactan_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_galactan_g_per_kg.md) | No slot description provided<br/>1367 occurrences with subject type sockg:BioMassCarbohydrate and object type xsd:double.|
| [sockg_galactanStd_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_galactanStd_g_per_kg.md) | No slot description provided<br/>1367 occurrences with subject type sockg:BioMassCarbohydrate and object type xsd:double.|
| [sockg_glomalin_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_glomalin_g_per_kg.md) | No slot description provided<br/>18222 occurrences with subject type sockg:SoilBiologicalSample and object type xsd:double.|
| [sockg_glomalinStd_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_glomalinStd_g_per_kg.md) | No slot description provided<br/>18222 occurrences with subject type sockg:SoilBiologicalSample and object type xsd:double.|
| [sockg_glucan_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_glucan_g_per_kg.md) | No slot description provided<br/>1367 occurrences with subject type sockg:BioMassCarbohydrate and object type xsd:double.|
| [sockg_glucanStd_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_glucanStd_g_per_kg.md) | No slot description provided<br/>1367 occurrences with subject type sockg:BioMassCarbohydrate and object type xsd:double.|
| [sockg_glucosaminidase_mg_per_kg_per_hr](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_glucosaminidase_mg_per_kg_per_hr.md) | No slot description provided<br/>18222 occurrences with subject type sockg:SoilBiologicalSample and object type xsd:double.|
| [sockg_glucosaminidaseStd_mg_per_kg_per_hr](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_glucosaminidaseStd_mg_per_kg_per_hr.md) | No slot description provided<br/>18222 occurrences with subject type sockg:SoilBiologicalSample and object type xsd:double.|
| [sockg_glucosidase_mg_per_kg_per_hr](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_glucosidase_mg_per_kg_per_hr.md) | No slot description provided<br/>18222 occurrences with subject type sockg:SoilBiologicalSample and object type xsd:double.|
| [sockg_glucosidaseStd_mg_per_kg_per_hr](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_glucosidaseStd_mg_per_kg_per_hr.md) | No slot description provided<br/>18222 occurrences with subject type sockg:SoilBiologicalSample and object type xsd:double.|
| [sockg_grainCarbon_kgC_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_grainCarbon_kgC_per_ha.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_grainCarbonStd_kgC_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_grainCarbonStd_kgC_per_ha.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_grainMoisturePercent](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_grainMoisturePercent.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_grainMoisturePercentStd](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_grainMoisturePercentStd.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_grainNitrogen_kgN_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_grainNitrogen_kgN_per_ha.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_grainNitrogenStd_kgN_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_grainNitrogenStd_kgN_per_ha.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_grainWeight_mg_per_kernel](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_grainWeight_mg_per_kernel.md) | No slot description provided<br/>9470 occurrences with subject type sockg:HarvestFraction and object type xsd:double.|
| [sockg_grainWeightKernelYnu_mg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_grainWeightKernelYnu_mg.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.|
| [sockg_grainWeightKernelYnuStd_mg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_grainWeightKernelYnuStd_mg.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.|
| [sockg_grainWeightStd_mg_per_lernel](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_grainWeightStd_mg_per_lernel.md) | No slot description provided<br/>9470 occurrences with subject type sockg:HarvestFraction and object type xsd:double.|
| [sockg_grainYield_kg_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_grainYield_kg_per_ha.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_grainYieldStd_kg_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_grainYieldStd_kg_per_ha.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_grazingRate](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_grazingRate.md) | No slot description provided<br/>749 occurrences with subject type sockg:Treatment and object type xsd:double.<br/>20 occurrences with subject type sockg:Treatment and object type string.|
| [sockg_grossCalorificValue_MJ_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_grossCalorificValue_MJ_per_kg.md) | No slot description provided<br/>799 occurrences with subject type sockg:BioMassEnergy and object type xsd:double.|
| [sockg_grossCalorificValueStd_MJ_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_grossCalorificValueStd_MJ_per_kg.md) | No slot description provided<br/>799 occurrences with subject type sockg:BioMassEnergy and object type xsd:double.|
| [sockg_groundCoverPercentage](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_groundCoverPercentage.md) | No slot description provided<br/>6995 occurrences with subject type sockg:Grazing and object type xsd:double.|
| [sockg_groundCoverPercentageStd](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_groundCoverPercentageStd.md) | No slot description provided<br/>6995 occurrences with subject type sockg:Grazing and object type xsd:double.|
| [sockg_growthStage](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_growthStage.md) | No slot description provided<br/>17240 occurrences with subject type sockg:Harvest and object type string.<br/>6683 occurrences with subject type sockg:Grazing and object type string.<br/>6723 occurrences with subject type sockg:BioMassMineral and object type string.<br/>2791 occurrences with subject type sockg:NutrientEfficiency and object type string.<br/>9407 occurrences with subject type sockg:HarvestFraction and object type string.<br/>4896 occurrences with subject type sockg:CropGrowthStage and object type string.<br/>1367 occurrences with subject type sockg:BioMassCarbohydrate and object type string.<br/>799 occurrences with subject type sockg:BioMassEnergy and object type string.<br/>1116 occurrences with subject type sockg:Harvest and object type xsd:double.<br/>667 occurrences with subject type sockg:WaterQualityConc and object type xsd:double.<br/>812 occurrences with subject type sockg:WaterQualityConc and object type string.<br/>684 occurrences with subject type sockg:GasNutrientLoss and object type xsd:double.<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.<br/>312 occurrences with subject type sockg:Grazing and object type xsd:double.<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type string.<br/>64 occurrences with subject type sockg:GasNutrientLoss and object type string.<br/>15 occurrences with subject type sockg:WindErosionArea and object type string.<br/>63 occurrences with subject type sockg:HarvestFraction and object type xsd:double.|
| [sockg_happenedInSite](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_happenedInSite.md) | No slot description provided<br/>61 occurrences with subject type sockg:Experiment and object type sockg:Site.|
| [sockg_harvestedFrac](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_harvestedFrac.md) | No slot description provided<br/>18047 occurrences with subject type sockg:Harvest and object type string.<br/>309 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_hasAmendment](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_hasAmendment.md) | No slot description provided<br/>37796 occurrences with subject type sockg:ExperimentalUnit and object type sockg:Amendment.|
| [sockg_hasBioMassCarbohydrateData](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_hasBioMassCarbohydrateData.md) | No slot description provided<br/>1367 occurrences with subject type sockg:ExperimentalUnit and object type sockg:BioMassCarbohydrate.|
| [sockg_hasBioMassEnergyData](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_hasBioMassEnergyData.md) | No slot description provided<br/>799 occurrences with subject type sockg:ExperimentalUnit and object type sockg:BioMassEnergy.|
| [sockg_hasBioMassMineralData](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_hasBioMassMineralData.md) | No slot description provided<br/>6723 occurrences with subject type sockg:ExperimentalUnit and object type sockg:BioMassMineral.|
| [sockg_hasBioSample](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_hasBioSample.md) | No slot description provided<br/>16926 occurrences with subject type sockg:ExperimentalUnit and object type sockg:SoilBiologicalSample.|
| [sockg_hasChemSample](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_hasChemSample.md) | No slot description provided<br/>52537 occurrences with subject type sockg:ExperimentalUnit and object type sockg:SoilChemicalSample.|
| [sockg_hasCity](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_hasCity.md) | No slot description provided<br/>33 occurrences with subject type sockg:County and object type sockg:City.|
| [sockg_hasCounty](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_hasCounty.md) | No slot description provided<br/>34 occurrences with subject type sockg:State and object type sockg:County.|
| [sockg_hasField](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_hasField.md) | No slot description provided<br/>65 occurrences with subject type sockg:Site and object type sockg:Field.|
| [sockg_hasGasNutrientData](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_hasGasNutrientData.md) | No slot description provided<br/>748 occurrences with subject type sockg:GasNutrientLoss and object type sockg:ExperimentalUnit.|
| [sockg_hasGasSample](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_hasGasSample.md) | No slot description provided<br/>106447 occurrences with subject type sockg:ExperimentalUnit and object type sockg:GasSample.|
| [sockg_hasGrazingData](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_hasGrazingData.md) | No slot description provided<br/>6995 occurrences with subject type sockg:ExperimentalUnit and object type sockg:Grazing.|
| [sockg_hasGrazingManagementEvent](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_hasGrazingManagementEvent.md) | No slot description provided<br/>1951 occurrences with subject type sockg:ExperimentalUnit and object type sockg:GrazingManagementEvent.|
| [sockg_hasHarvestFractionData](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_hasHarvestFractionData.md) | No slot description provided<br/>9110 occurrences with subject type sockg:ExperimentalUnit and object type sockg:HarvestFraction.|
| [sockg_hasPesticide](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_hasPesticide.md) | No slot description provided<br/>42545 occurrences with subject type sockg:Amendment and object type sockg:Pesticide.|
| [sockg_hasPhySample](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_hasPhySample.md) | No slot description provided<br/>26786 occurrences with subject type sockg:ExperimentalUnit and object type sockg:SoilPhysicalSample.|
| [sockg_hasResidueManagementEvent](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_hasResidueManagementEvent.md) | No slot description provided<br/>3308 occurrences with subject type sockg:ExperimentalUnit and object type sockg:ResidueManagementEvent.|
| [sockg_hasRotation](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_hasRotation.md) | No slot description provided<br/>761 occurrences with subject type sockg:Treatment and object type sockg:Rotation.|
| [sockg_hasState](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_hasState.md) | No slot description provided<br/>20 occurrences with subject type sockg:Country and object type sockg:State.|
| [sockg_hasTillage](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_hasTillage.md) | No slot description provided<br/>27137 occurrences with subject type sockg:ExperimentalUnit and object type sockg:Tillage.|
| [sockg_hasTreatment](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_hasTreatment.md) | No slot description provided<br/>741 occurrences with subject type sockg:Experiment and object type sockg:Treatment.|
| [sockg_hasWaterQualityAreaData](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_hasWaterQualityAreaData.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type sockg:ExperimentalUnit.|
| [sockg_hasWaterQualityConcData](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_hasWaterQualityConcData.md) | No slot description provided<br/>1479 occurrences with subject type sockg:WaterQualityConc and object type sockg:ExperimentalUnit.|
| [sockg_hasWindErosionData](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_hasWindErosionData.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type sockg:ExperimentalUnit.|
| [sockg_hasYieldNutrUptakeData](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_hasYieldNutrUptakeData.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type sockg:ExperimentalUnit.|
| [sockg_identifier](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_identifier.md) | No slot description provided<br/>114 occurrences with subject type sockg:Publication and object type string.|
| [sockg_inorganicCarbon_gC_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_inorganicCarbon_gC_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_inorganicCarbonStd_gC_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_inorganicCarbonStd_gC_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_inorganicNitrogen_kgN_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_inorganicNitrogen_kgN_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_inorganicNitrogenStd_kgN_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_inorganicNitrogenStd_kgN_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_iron_g_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_iron_g_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_ironConcentration_mg_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_ironConcentration_mg_per_kg.md) | No slot description provided<br/>6723 occurrences with subject type sockg:BioMassMineral and object type xsd:double.|
| [sockg_ironConcentrationStd_mg_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_ironConcentrationStd_mg_per_kg.md) | No slot description provided<br/>6723 occurrences with subject type sockg:BioMassMineral and object type xsd:double.|
| [sockg_ironStd_g_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_ironStd_g_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_irrigation](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_irrigation.md) | No slot description provided<br/>769 occurrences with subject type sockg:Treatment and object type string.|
| [sockg_irrigationAmount_cm](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_irrigationAmount_cm.md) | No slot description provided<br/>37796 occurrences with subject type sockg:Amendment and object type xsd:double.|
| [sockg_irrigationNitrogen_mg_per_L](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_irrigationNitrogen_mg_per_L.md) | No slot description provided<br/>37796 occurrences with subject type sockg:Amendment and object type xsd:double.|
| [sockg_irrigationType](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_irrigationType.md) | No slot description provided<br/>33571 occurrences with subject type sockg:Amendment and object type xsd:double.<br/>4225 occurrences with subject type sockg:Amendment and object type string.|
| [sockg_isCarbonDioxideInterpolated](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_isCarbonDioxideInterpolated.md) | No slot description provided<br/>107354 occurrences with subject type sockg:GasSample and object type xsd:long.|
| [sockg_isHarvested](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_isHarvested.md) | No slot description provided<br/>18356 occurrences with subject type sockg:ExperimentalUnit and object type sockg:Harvest.|
| [sockg_isMethaneInterpolated](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_isMethaneInterpolated.md) | No slot description provided<br/>107354 occurrences with subject type sockg:GasSample and object type xsd:long.|
| [sockg_isNitrousOxideInterpolated](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_isNitrousOxideInterpolated.md) | No slot description provided<br/>107354 occurrences with subject type sockg:GasSample and object type xsd:long.|
| [sockg_isPrimaryContact](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_isPrimaryContact.md) | No slot description provided<br/>82 occurrences with subject type sockg:Person and object type string.<br/>16 occurrences with subject type sockg:Person and object type xsd:double.|
| [sockg_lastName](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_lastName.md) | No slot description provided<br/>98 occurrences with subject type sockg:Person and object type string.|
| [sockg_latitude_decimal_deg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_latitude_decimal_deg.md) | No slot description provided<br/>58 occurrences with subject type sockg:Field and object type xsd:double.|
| [sockg_leafAreaIndexDry_kg_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_leafAreaIndexDry_kg_per_ha.md) | No slot description provided<br/>6995 occurrences with subject type sockg:Grazing and object type xsd:double.|
| [sockg_leafAreaIndexDryStd_kg_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_leafAreaIndexDryStd_kg_per_ha.md) | No slot description provided<br/>6995 occurrences with subject type sockg:Grazing and object type xsd:double.|
| [sockg_lignin_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_lignin_g_per_kg.md) | No slot description provided<br/>1367 occurrences with subject type sockg:BioMassCarbohydrate and object type xsd:double.|
| [sockg_ligninPercentage](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_ligninPercentage.md) | No slot description provided<br/>6995 occurrences with subject type sockg:Grazing and object type xsd:double.|
| [sockg_ligninPercentageStd](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_ligninPercentageStd.md) | No slot description provided<br/>6995 occurrences with subject type sockg:Grazing and object type xsd:double.|
| [sockg_ligninStd_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_ligninStd_g_per_kg.md) | No slot description provided<br/>1367 occurrences with subject type sockg:BioMassCarbohydrate and object type xsd:double.|
| [sockg_locatedInCity](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_locatedInCity.md) | No slot description provided<br/>59 occurrences with subject type sockg:Site and object type sockg:City.|
| [sockg_locatedInCountry](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_locatedInCountry.md) | No slot description provided<br/>60 occurrences with subject type sockg:Site and object type sockg:Country.|
| [sockg_locatedInCounty](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_locatedInCounty.md) | No slot description provided<br/>61 occurrences with subject type sockg:Site and object type sockg:County.|
| [sockg_locatedInField](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_locatedInField.md) | No slot description provided<br/>3809 occurrences with subject type sockg:ExperimentalUnit and object type sockg:Field.|
| [sockg_locatedInState](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_locatedInState.md) | No slot description provided<br/>60 occurrences with subject type sockg:Site and object type sockg:State.|
| [sockg_longitude_decimal_deg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_longitude_decimal_deg.md) | No slot description provided<br/>58 occurrences with subject type sockg:Field and object type xsd:double.|
| [sockg_lossesOrDeposition](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_lossesOrDeposition.md) | No slot description provided<br/>549 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.<br/>118 occurrences with subject type sockg:WaterQualityArea and object type string.<br/>5 occurrences with subject type sockg:WindErosionArea and object type string.<br/>10 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_lowerDepth_cm](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_lowerDepth_cm.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.<br/>28082 occurrences with subject type sockg:SoilPhysicalSample and object type xsd:double.<br/>18222 occurrences with subject type sockg:SoilBiologicalSample and object type xsd:long.|
| [sockg_macroAggregatesPercentStd](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_macroAggregatesPercentStd.md) | No slot description provided<br/>28082 occurrences with subject type sockg:SoilPhysicalSample and object type xsd:double.|
| [sockg_magnesium_kg_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_magnesium_kg_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_magnesiumConcentration_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_magnesiumConcentration_g_per_kg.md) | No slot description provided<br/>6723 occurrences with subject type sockg:BioMassMineral and object type xsd:double.|
| [sockg_magnesiumConcentrationStd_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_magnesiumConcentrationStd_g_per_kg.md) | No slot description provided<br/>6723 occurrences with subject type sockg:BioMassMineral and object type xsd:double.|
| [sockg_magnesiumStd_kg_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_magnesiumStd_kg_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_majorLandResourceArea](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_majorLandResourceArea.md) | No slot description provided<br/>60 occurrences with subject type sockg:Site and object type xsd:double.|
| [sockg_manganese_g_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_manganese_g_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_manganeseConcentration_mg_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_manganeseConcentration_mg_per_kg.md) | No slot description provided<br/>6723 occurrences with subject type sockg:BioMassMineral and object type xsd:double.|
| [sockg_manganeseConcentrationStd_mg_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_manganeseConcentrationStd_mg_per_kg.md) | No slot description provided<br/>6723 occurrences with subject type sockg:BioMassMineral and object type xsd:double.|
| [sockg_manganeseStd_g_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_manganeseStd_g_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_mannan_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_mannan_g_per_kg.md) | No slot description provided<br/>1367 occurrences with subject type sockg:BioMassCarbohydrate and object type xsd:double.|
| [sockg_mannanStd_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_mannanStd_g_per_kg.md) | No slot description provided<br/>1367 occurrences with subject type sockg:BioMassCarbohydrate and object type xsd:double.|
| [sockg_measBiomassCHO_UID](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_measBiomassCHO_UID.md) | No slot description provided<br/>1367 occurrences with subject type sockg:BioMassCarbohydrate and object type string.|
| [sockg_measBiomassEnergy_UID](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_measBiomassEnergy_UID.md) | No slot description provided<br/>799 occurrences with subject type sockg:BioMassEnergy and object type string.|
| [sockg_measBiomassMinAn_UID](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_measBiomassMinAn_UID.md) | No slot description provided<br/>6723 occurrences with subject type sockg:BioMassMineral and object type string.|
| [sockg_measGasNutrientLoss_UID](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_measGasNutrientLoss_UID.md) | No slot description provided<br/>748 occurrences with subject type sockg:GasNutrientLoss and object type string.|
| [sockg_measGHGFlux_UID](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_measGHGFlux_UID.md) | No slot description provided<br/>107354 occurrences with subject type sockg:GasSample and object type string.|
| [sockg_measGrazingPlants_UID](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_measGrazingPlants_UID.md) | No slot description provided<br/>6995 occurrences with subject type sockg:Grazing and object type string.|
| [sockg_measHarvestFraction_UID](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_measHarvestFraction_UID.md) | No slot description provided<br/>9470 occurrences with subject type sockg:HarvestFraction and object type string.|
| [sockg_measNutrEff_UID](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_measNutrEff_UID.md) | No slot description provided<br/>2791 occurrences with subject type sockg:NutrientEfficiency and object type string.|
| [sockg_measResidueMgnt_UID](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_measResidueMgnt_UID.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type string.|
| [sockg_measSoilBiol_UID](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_measSoilBiol_UID.md) | No slot description provided<br/>18222 occurrences with subject type sockg:SoilBiologicalSample and object type string.|
| [sockg_measSoilChem_UID](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_measSoilChem_UID.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type string.|
| [sockg_measSoilCover_UID](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_measSoilCover_UID.md) | No slot description provided<br/>1034 occurrences with subject type sockg:SoilCover and object type string.|
| [sockg_measSoilPhys_UID](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_measSoilPhys_UID.md) | No slot description provided<br/>28082 occurrences with subject type sockg:SoilPhysicalSample and object type string.|
| [sockg_measWaterQualityArea_UID](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_measWaterQualityArea_UID.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type string.|
| [sockg_measWaterQualityConc_UID](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_measWaterQualityConc_UID.md) | No slot description provided<br/>1479 occurrences with subject type sockg:WaterQualityConc and object type string.|
| [sockg_measWindErosionArea_UID](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_measWindErosionArea_UID.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type string.|
| [sockg_measYieldNutUptake_UID](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_measYieldNutUptake_UID.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type string.|
| [sockg_methane_gC_per_ha_per_d](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_methane_gC_per_ha_per_d.md) | No slot description provided<br/>107354 occurrences with subject type sockg:GasSample and object type xsd:double.|
| [sockg_methaneStd_gC_per_ha_per_d](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_methaneStd_gC_per_ha_per_d.md) | No slot description provided<br/>107354 occurrences with subject type sockg:GasSample and object type xsd:double.|
| [sockg_mgtAmendments_UID](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_mgtAmendments_UID.md) | No slot description provided<br/>37796 occurrences with subject type sockg:Amendment and object type string.|
| [sockg_mgtGrazing_UID](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_mgtGrazing_UID.md) | No slot description provided<br/>1951 occurrences with subject type sockg:GrazingManagementEvent and object type string.|
| [sockg_mgtGrowthStages_UID](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_mgtGrowthStages_UID.md) | No slot description provided<br/>4896 occurrences with subject type sockg:CropGrowthStage and object type string.|
| [sockg_mgtPlanting_UID](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_mgtPlanting_UID.md) | No slot description provided<br/>23450 occurrences with subject type sockg:PlantingEvent and object type string.|
| [sockg_mgtResidue_UID](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_mgtResidue_UID.md) | No slot description provided<br/>3308 occurrences with subject type sockg:ResidueManagementEvent and object type string.|
| [sockg_mgtTillage_UID](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_mgtTillage_UID.md) | No slot description provided<br/>27137 occurrences with subject type sockg:Tillage and object type string.|
| [sockg_middleName](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_middleName.md) | No slot description provided<br/>65 occurrences with subject type sockg:Person and object type string.<br/>33 occurrences with subject type sockg:Person and object type xsd:double.|
| [sockg_mineralCarbon_gC_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_mineralCarbon_gC_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_mineralCarbonStd_gC_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_mineralCarbonStd_gC_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_mineralizableNitrogen_gN_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_mineralizableNitrogen_gN_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_mineralizableNitrogenStd_gN_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_mineralizableNitrogenStd_gN_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_mineralMatter_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_mineralMatter_g_per_kg.md) | No slot description provided<br/>799 occurrences with subject type sockg:BioMassEnergy and object type xsd:double.|
| [sockg_mineralMatterStd_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_mineralMatterStd_g_per_kg.md) | No slot description provided<br/>799 occurrences with subject type sockg:BioMassEnergy and object type xsd:double.|
| [sockg_modelIfSimulated](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_modelIfSimulated.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type xsd:double.<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.<br/>692 occurrences with subject type sockg:GasNutrientLoss and object type xsd:double.<br/>1466 occurrences with subject type sockg:WaterQualityConc and object type xsd:double.<br/>56 occurrences with subject type sockg:GasNutrientLoss and object type string.<br/>13 occurrences with subject type sockg:WaterQualityConc and object type string.<br/>4 occurrences with subject type sockg:WindErosionArea and object type string.<br/>11 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_moisturePercent](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_moisturePercent.md) | No slot description provided<br/>9470 occurrences with subject type sockg:HarvestFraction and object type xsd:double.|
| [sockg_moisturePercentStd](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_moisturePercentStd.md) | No slot description provided<br/>9470 occurrences with subject type sockg:HarvestFraction and object type xsd:double.|
| [sockg_moistureReleaseCurve](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_moistureReleaseCurve.md) | No slot description provided<br/>28082 occurrences with subject type sockg:SoilPhysicalSample and object type xsd:double.|
| [sockg_molybdenum_g_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_molybdenum_g_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_molybdenumStd_g_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_molybdenumStd_g_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_nearInfraredCarbon_gC_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nearInfraredCarbon_gC_per_kg.md) | No slot description provided<br/>28082 occurrences with subject type sockg:SoilPhysicalSample and object type xsd:double.|
| [sockg_nearInfraredCarbonStd_gC_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nearInfraredCarbonStd_gC_per_kg.md) | No slot description provided<br/>28082 occurrences with subject type sockg:SoilPhysicalSample and object type xsd:double.|
| [sockg_neutralDetFiber_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_neutralDetFiber_g_per_kg.md) | No slot description provided<br/>1367 occurrences with subject type sockg:BioMassCarbohydrate and object type xsd:double.|
| [sockg_neutralDetFiberStd_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_neutralDetFiberStd_g_per_kg.md) | No slot description provided<br/>1367 occurrences with subject type sockg:BioMassCarbohydrate and object type xsd:double.|
| [sockg_nitrate_kg_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nitrate_kg_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_nitrate_mgN_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nitrate_mgN_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_nitrateNitrogen_kg_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nitrateNitrogen_kg_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_nitrateStd_kgN_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nitrateStd_kgN_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_nitrateStd_mgN_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nitrateStd_mgN_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_nitrites_mgN_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nitrites_mgN_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_nitritesStd_mgN_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nitritesStd_mgN_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_nitrogen_kgN_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nitrogen_kgN_per_ha.md) | No slot description provided<br/>9470 occurrences with subject type sockg:HarvestFraction and object type xsd:double.|
| [sockg_nitrogenConcentration_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nitrogenConcentration_g_per_kg.md) | No slot description provided<br/>6723 occurrences with subject type sockg:BioMassMineral and object type xsd:double.|
| [sockg_nitrogenConcentrationStd_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nitrogenConcentrationStd_g_per_kg.md) | No slot description provided<br/>6723 occurrences with subject type sockg:BioMassMineral and object type xsd:double.|
| [sockg_nitrogenGas_g_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nitrogenGas_g_ha.md) | No slot description provided<br/>748 occurrences with subject type sockg:GasNutrientLoss and object type xsd:double.|
| [sockg_nitrogenGasStd_g_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nitrogenGasStd_g_ha.md) | No slot description provided<br/>748 occurrences with subject type sockg:GasNutrientLoss and object type xsd:double.|
| [sockg_nitrogenMicrobialBiomass_mgN_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nitrogenMicrobialBiomass_mgN_per_kg.md) | No slot description provided<br/>18222 occurrences with subject type sockg:SoilBiologicalSample and object type xsd:double.|
| [sockg_nitrogenMicrobialBiomassStd_mgN_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nitrogenMicrobialBiomassStd_mgN_per_kg.md) | No slot description provided<br/>18222 occurrences with subject type sockg:SoilBiologicalSample and object type xsd:double.|
| [sockg_nitrogenStd_kgN_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nitrogenStd_kgN_per_ha.md) | No slot description provided<br/>9470 occurrences with subject type sockg:HarvestFraction and object type xsd:double.|
| [sockg_nitrogenTreatmentDescriptor](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nitrogenTreatmentDescriptor.md) | No slot description provided<br/>19 occurrences with subject type sockg:Treatment and object type xsd:double.<br/>750 occurrences with subject type sockg:Treatment and object type string.|
| [sockg_nitrogenUseEfficiency_kg_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nitrogenUseEfficiency_kg_ha.md) | No slot description provided<br/>2791 occurrences with subject type sockg:NutrientEfficiency and object type xsd:double.|
| [sockg_nitrogenUseEfficiencyPct](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nitrogenUseEfficiencyPct.md) | No slot description provided<br/>2791 occurrences with subject type sockg:NutrientEfficiency and object type xsd:double.|
| [sockg_nitrousOxide_g_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nitrousOxide_g_ha.md) | No slot description provided<br/>748 occurrences with subject type sockg:GasNutrientLoss and object type xsd:double.|
| [sockg_nitrousOxide_gN_per_ha_per_d](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nitrousOxide_gN_per_ha_per_d.md) | No slot description provided<br/>107354 occurrences with subject type sockg:GasSample and object type xsd:double.|
| [sockg_nitrousOxides_g_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nitrousOxides_g_ha.md) | No slot description provided<br/>748 occurrences with subject type sockg:GasNutrientLoss and object type xsd:double.|
| [sockg_nitrousOxidesStd_g_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nitrousOxidesStd_g_ha.md) | No slot description provided<br/>748 occurrences with subject type sockg:GasNutrientLoss and object type xsd:double.|
| [sockg_nitrousOxideStd_g_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nitrousOxideStd_g_ha.md) | No slot description provided<br/>748 occurrences with subject type sockg:GasNutrientLoss and object type xsd:double.|
| [sockg_nitrousOxideStd_gN_per_ha_per_d](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nitrousOxideStd_gN_per_ha_per_d.md) | No slot description provided<br/>107354 occurrences with subject type sockg:GasSample and object type xsd:double.|
| [sockg_nonFiberCarbs_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nonFiberCarbs_g_per_kg.md) | No slot description provided<br/>1367 occurrences with subject type sockg:BioMassCarbohydrate and object type xsd:double.|
| [sockg_nonFiberCarbsStd_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nonFiberCarbsStd_g_per_kg.md) | No slot description provided<br/>1367 occurrences with subject type sockg:BioMassCarbohydrate and object type xsd:double.|
| [sockg_nonHarvestedResidueCarbonContent_kgC_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nonHarvestedResidueCarbonContent_kgC_per_ha.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_nonHarvestedResidueCarbonContentStd_kgC_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nonHarvestedResidueCarbonContentStd_kgC_per_ha.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_nonHarvestedResidueMass_kg_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nonHarvestedResidueMass_kg_per_ha.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_nonHarvestedResidueMassStd_kg_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nonHarvestedResidueMassStd_kg_per_ha.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_nonHarvestedResidueMoisturePercent](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nonHarvestedResidueMoisturePercent.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_nonHarvestedResidueMoisturePercentStd](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nonHarvestedResidueMoisturePercentStd.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_nonHarvestedResidueNitrogenContent_kgN_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nonHarvestedResidueNitrogenContent_kgN_per_ha.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_nonHarvestedResidueNitrogenContentStd_kgN_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nonHarvestedResidueNitrogenContentStd_kgN_per_ha.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_note](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_note.md) | No slot description provided<br/>86 occurrences with subject type sockg:Person and object type xsd:double.<br/>12 occurrences with subject type sockg:Person and object type string.|
| [sockg_nutrientEfficiencyRatio_kg_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_nutrientEfficiencyRatio_kg_kg.md) | No slot description provided<br/>2791 occurrences with subject type sockg:NutrientEfficiency and object type xsd:double.|
| [sockg_openPanEvaporation_mm_per_d](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_openPanEvaporation_mm_per_d.md) | No slot description provided<br/>147305 occurrences with subject type sockg:WeatherObservation and object type xsd:double.|
| [sockg_organicCarbon_gC_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_organicCarbon_gC_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_organicCarbonStd_gC_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_organicCarbonStd_gC_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_organicManagement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_organicManagement.md) | No slot description provided<br/>769 occurrences with subject type sockg:Treatment and object type string.|
| [sockg_organicPlantMaterial_gC_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_organicPlantMaterial_gC_per_kg.md) | No slot description provided<br/>18222 occurrences with subject type sockg:SoilBiologicalSample and object type xsd:double.|
| [sockg_organicPlantMaterialStd_gC_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_organicPlantMaterialStd_gC_per_kg.md) | No slot description provided<br/>18222 occurrences with subject type sockg:SoilBiologicalSample and object type xsd:double.|
| [sockg_organizationName](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_organizationName.md) | No slot description provided<br/>7 occurrences with subject type sockg:Organization and object type string.|
| [sockg_otherEvents](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_otherEvents.md) | No slot description provided<br/>1947 occurrences with subject type sockg:GrazingManagementEvent and object type xsd:double.<br/>4 occurrences with subject type sockg:GrazingManagementEvent and object type string.|
| [sockg_particulateOrganicMatter_gC_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_particulateOrganicMatter_gC_per_kg.md) | No slot description provided<br/>18222 occurrences with subject type sockg:SoilBiologicalSample and object type xsd:double.|
| [sockg_particulateOrganicMatterStd_gC_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_particulateOrganicMatterStd_gC_per_kg.md) | No slot description provided<br/>18222 occurrences with subject type sockg:SoilBiologicalSample and object type xsd:double.|
| [sockg_perennialStandAge_years](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_perennialStandAge_years.md) | No slot description provided<br/>3308 occurrences with subject type sockg:ResidueManagementEvent and object type xsd:double.|
| [sockg_persons_UID](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_persons_UID.md) | No slot description provided<br/>98 occurrences with subject type sockg:Person and object type string.|
| [sockg_pesticide_UID](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_pesticide_UID.md) | No slot description provided<br/>356 occurrences with subject type sockg:Pesticide and object type string.|
| [sockg_pesticideActiveIngredientType](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_pesticideActiveIngredientType.md) | No slot description provided<br/>353 occurrences with subject type sockg:Pesticide and object type string.<br/>3 occurrences with subject type sockg:Pesticide and object type xsd:double.|
| [sockg_pesticidePlacement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_pesticidePlacement.md) | No slot description provided<br/>126 occurrences with subject type sockg:Pesticide and object type xsd:double.<br/>230 occurrences with subject type sockg:Pesticide and object type string.|
| [sockg_pesticideTarget](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_pesticideTarget.md) | No slot description provided<br/>109 occurrences with subject type sockg:Pesticide and object type xsd:double.<br/>247 occurrences with subject type sockg:Pesticide and object type string.|
| [sockg_ph](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_ph.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.<br/>1479 occurrences with subject type sockg:WaterQualityConc and object type xsd:double.<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_phoneNumber](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_phoneNumber.md) | No slot description provided<br/>15 occurrences with subject type sockg:Person and object type xsd:double.<br/>83 occurrences with subject type sockg:Person and object type string.|
| [sockg_phosphorus_kg_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_phosphorus_kg_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_phosphorus_mgP_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_phosphorus_mgP_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_phosphorusConcentration_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_phosphorusConcentration_g_per_kg.md) | No slot description provided<br/>6723 occurrences with subject type sockg:BioMassMineral and object type xsd:double.|
| [sockg_phosphorusConcentrationStd_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_phosphorusConcentrationStd_g_per_kg.md) | No slot description provided<br/>6723 occurrences with subject type sockg:BioMassMineral and object type xsd:double.|
| [sockg_phosphorusStd_kg_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_phosphorusStd_kg_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_phosphorusStd_mgP_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_phosphorusStd_mgP_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_phStd](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_phStd.md) | No slot description provided<br/>1479 occurrences with subject type sockg:WaterQualityConc and object type xsd:double.<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_plantFraction](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_plantFraction.md) | No slot description provided<br/>9470 occurrences with subject type sockg:HarvestFraction and object type string.<br/>6723 occurrences with subject type sockg:BioMassMineral and object type string.<br/>2683 occurrences with subject type sockg:NutrientEfficiency and object type string.<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type string.<br/>1367 occurrences with subject type sockg:BioMassCarbohydrate and object type string.<br/>799 occurrences with subject type sockg:BioMassEnergy and object type string.<br/>108 occurrences with subject type sockg:NutrientEfficiency and object type xsd:double.|
| [sockg_plantingAt](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_plantingAt.md) | No slot description provided<br/>23450 occurrences with subject type sockg:PlantingEvent and object type sockg:ExperimentalUnit.|
| [sockg_plantingMethod](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_plantingMethod.md) | No slot description provided<br/>1136 occurrences with subject type sockg:PlantingEvent and object type xsd:double.<br/>22314 occurrences with subject type sockg:PlantingEvent and object type string.|
| [sockg_postalCodeNumber](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_postalCodeNumber.md) | No slot description provided<br/>60 occurrences with subject type sockg:Site and object type xsd:double.|
| [sockg_potassium_kg_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_potassium_kg_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_potassium_mgK_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_potassium_mgK_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_potassiumConcentration_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_potassiumConcentration_g_per_kg.md) | No slot description provided<br/>6723 occurrences with subject type sockg:BioMassMineral and object type xsd:double.|
| [sockg_potassiumConcentrationStd_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_potassiumConcentrationStd_g_per_kg.md) | No slot description provided<br/>6723 occurrences with subject type sockg:BioMassMineral and object type xsd:double.|
| [sockg_potassiumStd_kg_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_potassiumStd_kg_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_potassiumStd_mgK_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_potassiumStd_mgK_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_precipitation_mm_per_d](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_precipitation_mm_per_d.md) | No slot description provided<br/>147305 occurrences with subject type sockg:WeatherObservation and object type xsd:double.|
| [sockg_profession](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_profession.md) | No slot description provided<br/>93 occurrences with subject type sockg:Person and object type string.<br/>5 occurrences with subject type sockg:Person and object type xsd:double.|
| [sockg_projectName](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_projectName.md) | No slot description provided<br/>55 occurrences with subject type sockg:Experiment and object type string.<br/>9 occurrences with subject type sockg:Project and object type string.|
| [sockg_projectScenario](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_projectScenario.md) | No slot description provided<br/>769 occurrences with subject type sockg:Treatment and object type string.|
| [sockg_recordsWeatherForField](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_recordsWeatherForField.md) | No slot description provided<br/>14 occurrences with subject type sockg:WeatherStation and object type sockg:Field.|
| [sockg_recordsWeatherForSite](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_recordsWeatherForSite.md) | No slot description provided<br/>14 occurrences with subject type sockg:WeatherStation and object type sockg:Site.|
| [sockg_relativeHumidityPercent](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_relativeHumidityPercent.md) | No slot description provided<br/>147305 occurrences with subject type sockg:WeatherObservation and object type xsd:double.|
| [sockg_residueRemoval](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_residueRemoval.md) | No slot description provided<br/>769 occurrences with subject type sockg:Treatment and object type string.|
| [sockg_roleInStudy](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_roleInStudy.md) | No slot description provided<br/>93 occurrences with subject type sockg:Person and object type string.<br/>5 occurrences with subject type sockg:Person and object type xsd:double.|
| [sockg_rootCarbonContent_kgC_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_rootCarbonContent_kgC_per_ha.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_rootCarbonContentStd_kgC_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_rootCarbonContentStd_kgC_per_ha.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_rootDryMatter_kg_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_rootDryMatter_kg_per_ha.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_rootDryMatterStd_kg_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_rootDryMatterStd_kg_per_ha.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_rootMoisturePercent](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_rootMoisturePercent.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_rootMoisturePercentStd](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_rootMoisturePercentStd.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_rootNitrogenContent_kgN_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_rootNitrogenContent_kgN_per_ha.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_rootNitrogenContentStd_kgN_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_rootNitrogenContentStd_kgN_per_ha.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_rotationDescriptor](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_rotationDescriptor.md) | No slot description provided<br/>66 occurrences with subject type sockg:Rotation and object type string.|
| [sockg_rowsHarvestedPercent](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_rowsHarvestedPercent.md) | No slot description provided<br/>3308 occurrences with subject type sockg:ResidueManagementEvent and object type xsd:long.|
| [sockg_rowWidth_cm](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_rowWidth_cm.md) | No slot description provided<br/>23450 occurrences with subject type sockg:PlantingEvent and object type xsd:double.|
| [sockg_samplingDepth_cm](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_samplingDepth_cm.md) | No slot description provided<br/>1479 occurrences with subject type sockg:WaterQualityConc and object type xsd:long.|
| [sockg_samplingStartStopInterval](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_samplingStartStopInterval.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityConc and object type xsd:double.<br/>684 occurrences with subject type sockg:GasNutrientLoss and object type xsd:double.<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.<br/>812 occurrences with subject type sockg:WaterQualityConc and object type string.<br/>15 occurrences with subject type sockg:WindErosionArea and object type string.<br/>64 occurrences with subject type sockg:GasNutrientLoss and object type string.|
| [sockg_sandPercent](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_sandPercent.md) | No slot description provided<br/>28082 occurrences with subject type sockg:SoilPhysicalSample and object type xsd:double.|
| [sockg_saturatedHydraulicConductivity_cm_per_sec](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_saturatedHydraulicConductivity_cm_per_sec.md) | No slot description provided<br/>28082 occurrences with subject type sockg:SoilPhysicalSample and object type xsd:double.|
| [sockg_saturatedHydraulicConductivityStd_cm_per_sec](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_saturatedHydraulicConductivityStd_cm_per_sec.md) | No slot description provided<br/>28082 occurrences with subject type sockg:SoilPhysicalSample and object type xsd:double.|
| [sockg_silicon_kg_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_silicon_kg_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_siliconStd_kg_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_siliconStd_kg_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_siltPercent](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_siltPercent.md) | No slot description provided<br/>28082 occurrences with subject type sockg:SoilPhysicalSample and object type xsd:double.|
| [sockg_siteHistory](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_siteHistory.md) | No slot description provided<br/>60 occurrences with subject type sockg:Site and object type xsd:double.|
| [sockg_siteId](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_siteId.md) | No slot description provided<br/>60 occurrences with subject type sockg:Site and object type string.|
| [sockg_siteIdDescriptor](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_siteIdDescriptor.md) | No slot description provided<br/>60 occurrences with subject type sockg:Site and object type xsd:double.|
| [sockg_siteNativeVegetation](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_siteNativeVegetation.md) | No slot description provided<br/>60 occurrences with subject type sockg:Site and object type xsd:double.|
| [sockg_siteSpatialDescription](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_siteSpatialDescription.md) | No slot description provided<br/>60 occurrences with subject type sockg:Site and object type string.|
| [sockg_snow_mm_per_d](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_snow_mm_per_d.md) | No slot description provided<br/>147305 occurrences with subject type sockg:WeatherObservation and object type xsd:double.|
| [sockg_sodium_kg_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_sodium_kg_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_sodiumConcentration_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_sodiumConcentration_g_per_kg.md) | No slot description provided<br/>6723 occurrences with subject type sockg:BioMassMineral and object type xsd:double.|
| [sockg_sodiumConcentrationStd_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_sodiumConcentrationStd_g_per_kg.md) | No slot description provided<br/>6723 occurrences with subject type sockg:BioMassMineral and object type xsd:double.|
| [sockg_sodiumStd_kg_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_sodiumStd_kg_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_soil_t_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_soil_t_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_soilMoisture_percent_volume](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_soilMoisture_percent_volume.md) | No slot description provided<br/>107354 occurrences with subject type sockg:GasSample and object type xsd:double.|
| [sockg_soilMoistureDepth_cm](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_soilMoistureDepth_cm.md) | No slot description provided<br/>107354 occurrences with subject type sockg:GasSample and object type xsd:long.|
| [sockg_soilOrganicCarbon_kgC_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_soilOrganicCarbon_kgC_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_soilOrganicCarbonStd_kgC_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_soilOrganicCarbonStd_kgC_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_soilStd_t_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_soilStd_t_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_soilTemp10cm_degC](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_soilTemp10cm_degC.md) | No slot description provided<br/>147305 occurrences with subject type sockg:WeatherObservation and object type xsd:double.|
| [sockg_soilTemp5cm_degC](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_soilTemp5cm_degC.md) | No slot description provided<br/>147305 occurrences with subject type sockg:WeatherObservation and object type xsd:double.|
| [sockg_soilTemperature_degC](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_soilTemperature_degC.md) | No slot description provided<br/>107354 occurrences with subject type sockg:GasSample and object type xsd:double.|
| [sockg_soilTemperatureStd_degC](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_soilTemperatureStd_degC.md) | No slot description provided<br/>107354 occurrences with subject type sockg:GasSample and object type xsd:double.|
| [sockg_soilWithResidueCoverPercent](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_soilWithResidueCoverPercent.md) | No slot description provided<br/>1034 occurrences with subject type sockg:SoilCover and object type xsd:double.|
| [sockg_solarRadiationBareSoil_MJ_per_m_squared_per_d](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_solarRadiationBareSoil_MJ_per_m_squared_per_d.md) | No slot description provided<br/>147305 occurrences with subject type sockg:WeatherObservation and object type xsd:double.|
| [sockg_solarRadiationVegetatedGround_MJ_per_m_squared_per_d](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_solarRadiationVegetatedGround_MJ_per_m_squared_per_d.md) | No slot description provided<br/>147305 occurrences with subject type sockg:WeatherObservation and object type xsd:double.|
| [sockg_solubleOrganicCarbon_mgC_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_solubleOrganicCarbon_mgC_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_solubleOrganicCarbonStd_mgC_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_solubleOrganicCarbonStd_mgC_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_speciesMix](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_speciesMix.md) | No slot description provided<br/>6995 occurrences with subject type sockg:Grazing and object type string.|
| [sockg_stageAtHarvest](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_stageAtHarvest.md) | No slot description provided<br/>1650 occurrences with subject type sockg:ResidueManagementEvent and object type string.<br/>1658 occurrences with subject type sockg:ResidueManagementEvent and object type xsd:double.|
| [sockg_startDate](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_startDate.md) | No slot description provided<br/>37796 occurrences with subject type sockg:Amendment and object type string.<br/>3178 occurrences with subject type sockg:ExperimentalUnit and object type string.<br/>1951 occurrences with subject type sockg:GrazingManagementEvent and object type string.<br/>631 occurrences with subject type sockg:ExperimentalUnit and object type xsd:double.<br/>55 occurrences with subject type sockg:Experiment and object type string.|
| [sockg_stateProvince](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_stateProvince.md) | No slot description provided<br/>20 occurrences with subject type sockg:State and object type string.|
| [sockg_stockingRate_number_animals_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_stockingRate_number_animals_per_ha.md) | No slot description provided<br/>1951 occurrences with subject type sockg:GrazingManagementEvent and object type xsd:double.|
| [sockg_studiesSite](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_studiesSite.md) | No slot description provided<br/>123 occurrences with subject type sockg:Publication and object type sockg:Site.|
| [sockg_suffix](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_suffix.md) | No slot description provided<br/>32 occurrences with subject type sockg:Person and object type string.<br/>66 occurrences with subject type sockg:Person and object type xsd:double.|
| [sockg_sulfur_kg_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_sulfur_kg_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_sulfurConcentration_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_sulfurConcentration_g_per_kg.md) | No slot description provided<br/>6723 occurrences with subject type sockg:BioMassMineral and object type xsd:double.|
| [sockg_sulfurConcentrationStd_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_sulfurConcentrationStd_g_per_kg.md) | No slot description provided<br/>6723 occurrences with subject type sockg:BioMassMineral and object type xsd:double.|
| [sockg_sulfurStd_kg_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_sulfurStd_kg_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_surfaceOrLeaching](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_surfaceOrLeaching.md) | No slot description provided<br/>1479 occurrences with subject type sockg:WaterQualityConc and object type string.<br/>667 occurrences with subject type sockg:WaterQualityArea and object type string.|
| [sockg_tempMax_degC](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_tempMax_degC.md) | No slot description provided<br/>147305 occurrences with subject type sockg:WeatherObservation and object type xsd:double.|
| [sockg_tempMin_degC](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_tempMin_degC.md) | No slot description provided<br/>147305 occurrences with subject type sockg:WeatherObservation and object type xsd:double.|
| [sockg_tileDrainage](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_tileDrainage.md) | No slot description provided<br/>331 occurrences with subject type sockg:Treatment and object type xsd:double.<br/>438 occurrences with subject type sockg:Treatment and object type string.|
| [sockg_tillageDescriptor](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_tillageDescriptor.md) | No slot description provided<br/>719 occurrences with subject type sockg:Treatment and object type string.<br/>50 occurrences with subject type sockg:Treatment and object type xsd:double.|
| [sockg_time](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_time.md) | No slot description provided<br/>101883 occurrences with subject type sockg:GasSample and object type xsd:double.<br/>5471 occurrences with subject type sockg:GasSample and object type string.<br/>1479 occurrences with subject type sockg:WaterQualityConc and object type xsd:double.<br/>748 occurrences with subject type sockg:GasNutrientLoss and object type xsd:double.<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_title](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_title.md) | No slot description provided<br/>107 occurrences with subject type sockg:Publication and object type string.<br/>7 occurrences with subject type sockg:Publication and object type xsd:double.|
| [sockg_totalAmendmentAmount_kg_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_totalAmendmentAmount_kg_per_ha.md) | No slot description provided<br/>37796 occurrences with subject type sockg:Amendment and object type xsd:double.|
| [sockg_totalChloride_kg_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_totalChloride_kg_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_totalDissolvedNitrogen_kgN_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_totalDissolvedNitrogen_kgN_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_totalDissolvedNitrogenStd_kgN_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_totalDissolvedNitrogenStd_kgN_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_totalDissolvedPhosphorus_kgP_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_totalDissolvedPhosphorus_kgP_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_totalDissolvedPhosphorusStd_jgP_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_totalDissolvedPhosphorusStd_jgP_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_totalNitrogen_kg_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_totalNitrogen_kg_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_totalNitrogenAmount_kgN_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_totalNitrogenAmount_kgN_per_ha.md) | No slot description provided<br/>37796 occurrences with subject type sockg:Amendment and object type xsd:double.|
| [sockg_totalNitrogenStd_kgN_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_totalNitrogenStd_kgN_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_totalPesticideAmount_kg_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_totalPesticideAmount_kg_per_ha.md) | No slot description provided<br/>356 occurrences with subject type sockg:Pesticide and object type xsd:double.|
| [sockg_totalPhosphorusAmount_kgP_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_totalPhosphorusAmount_kgP_per_ha.md) | No slot description provided<br/>37796 occurrences with subject type sockg:Amendment and object type xsd:double.|
| [sockg_totalPhosphorusStd_kgP_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_totalPhosphorusStd_kgP_ha.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_totalPotassiumAmount_kgK_per_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_totalPotassiumAmount_kgK_per_ha.md) | No slot description provided<br/>37796 occurrences with subject type sockg:Amendment and object type xsd:double.|
| [sockg_totalSoilCarbon_gC_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_totalSoilCarbon_gC_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_totalSoilCarbonStd_gC_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_totalSoilCarbonStd_gC_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_totalSoilNitrogen_gN_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_totalSoilNitrogen_gN_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_totalSoilNitrogenStd_gN_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_totalSoilNitrogenStd_gN_per_kg.md) | No slot description provided<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.|
| [sockg_tracksGrowth](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_tracksGrowth.md) | No slot description provided<br/>4896 occurrences with subject type sockg:ExperimentalUnit and object type sockg:CropGrowthStage.|
| [sockg_treatmentDescriptor](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_treatmentDescriptor.md) | No slot description provided<br/>769 occurrences with subject type sockg:Treatment and object type string.|
| [sockg_treatmentId](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_treatmentId.md) | No slot description provided<br/>6723 occurrences with subject type sockg:BioMassMineral and object type string.<br/>107354 occurrences with subject type sockg:GasSample and object type string.<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type string.<br/>37796 occurrences with subject type sockg:Amendment and object type string.<br/>9470 occurrences with subject type sockg:HarvestFraction and object type string.<br/>28082 occurrences with subject type sockg:SoilPhysicalSample and object type string.<br/>18222 occurrences with subject type sockg:SoilBiologicalSample and object type string.<br/>4896 occurrences with subject type sockg:CropGrowthStage and object type string.<br/>6995 occurrences with subject type sockg:Grazing and object type string.<br/>1951 occurrences with subject type sockg:GrazingManagementEvent and object type string.<br/>799 occurrences with subject type sockg:BioMassEnergy and object type string.<br/>18356 occurrences with subject type sockg:Harvest and object type string.<br/>1479 occurrences with subject type sockg:WaterQualityConc and object type string.<br/>3308 occurrences with subject type sockg:ResidueManagementEvent and object type string.<br/>1367 occurrences with subject type sockg:BioMassCarbohydrate and object type string.<br/>667 occurrences with subject type sockg:WaterQualityArea and object type string.<br/>2791 occurrences with subject type sockg:NutrientEfficiency and object type string.<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type string.<br/>748 occurrences with subject type sockg:GasNutrientLoss and object type string.<br/>769 occurrences with subject type sockg:Treatment and object type string.<br/>15 occurrences with subject type sockg:WindErosionArea and object type string.|
| [sockg_type](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_type.md) | No slot description provided<br/>22884 occurrences with subject type sockg:Amendment and object type string.<br/>14912 occurrences with subject type sockg:Amendment and object type xsd:double.|
| [sockg_unitGrainWeight_mg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_unitGrainWeight_mg.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_unitGrainWeightStd_mg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_unitGrainWeightStd_mg.md) | No slot description provided<br/>18356 occurrences with subject type sockg:Harvest and object type xsd:double.|
| [sockg_upperDepth_cm](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_upperDepth_cm.md) | No slot description provided<br/>28082 occurrences with subject type sockg:SoilPhysicalSample and object type xsd:double.<br/>53833 occurrences with subject type sockg:SoilChemicalSample and object type xsd:double.<br/>18222 occurrences with subject type sockg:SoilBiologicalSample and object type xsd:long.|
| [sockg_versionDate](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_versionDate.md) | No slot description provided<br/>1 occurrences with subject type sockg:Version and object type string.|
| [sockg_volatileMatter_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_volatileMatter_g_per_kg.md) | No slot description provided<br/>799 occurrences with subject type sockg:BioMassEnergy and object type xsd:double.|
| [sockg_volatileMatterStd_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_volatileMatterStd_g_per_kg.md) | No slot description provided<br/>799 occurrences with subject type sockg:BioMassEnergy and object type xsd:double.|
| [sockg_water_mm](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_water_mm.md) | No slot description provided<br/>1479 occurrences with subject type sockg:WaterQualityConc and object type xsd:double.|
| [sockg_waterQualityAreaDataAt](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_waterQualityAreaDataAt.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type sockg:Field.|
| [sockg_waterQualityAreaTreatment](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_waterQualityAreaTreatment.md) | No slot description provided<br/>667 occurrences with subject type sockg:WaterQualityArea and object type sockg:Treatment.|
| [sockg_waterQualityConcDataAt](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_waterQualityConcDataAt.md) | No slot description provided<br/>1479 occurrences with subject type sockg:WaterQualityConc and object type sockg:Field.|
| [sockg_waterQualityConcTreatment](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_waterQualityConcTreatment.md) | No slot description provided<br/>1479 occurrences with subject type sockg:WaterQualityConc and object type sockg:Treatment.|
| [sockg_waterStableAggregatePercent](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_waterStableAggregatePercent.md) | No slot description provided<br/>28082 occurrences with subject type sockg:SoilPhysicalSample and object type xsd:double.|
| [sockg_waterStableAggregatesPercentStd](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_waterStableAggregatesPercentStd.md) | No slot description provided<br/>28082 occurrences with subject type sockg:SoilPhysicalSample and object type xsd:double.|
| [sockg_waterStd_mm](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_waterStd_mm.md) | No slot description provided<br/>1479 occurrences with subject type sockg:WaterQualityConc and object type xsd:double.<br/>667 occurrences with subject type sockg:WaterQualityArea and object type xsd:double.|
| [sockg_weatherAtField](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_weatherAtField.md) | No slot description provided<br/>147305 occurrences with subject type sockg:WeatherObservation and object type sockg:Field.|
| [sockg_weatherBadValueFlag](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_weatherBadValueFlag.md) | No slot description provided<br/>147305 occurrences with subject type sockg:WeatherObservation and object type xsd:double.|
| [sockg_weatherDaily_UID](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_weatherDaily_UID.md) | No slot description provided<br/>147305 occurrences with subject type sockg:WeatherObservation and object type string.|
| [sockg_weatherRecordedAt](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_weatherRecordedAt.md) | No slot description provided<br/>149473 occurrences with subject type sockg:WeatherObservation and object type sockg:Site.|
| [sockg_weatherRecordedBy](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_weatherRecordedBy.md) | No slot description provided<br/>39489 occurrences with subject type sockg:WeatherStation and object type sockg:WeatherObservation.|
| [sockg_weatherStationId](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_weatherStationId.md) | No slot description provided<br/>12 occurrences with subject type sockg:WeatherStation and object type string.|
| [sockg_website](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_website.md) | No slot description provided<br/>30 occurrences with subject type sockg:Person and object type string.<br/>68 occurrences with subject type sockg:Person and object type xsd:double.|
| [sockg_wiltingPoint_percent_volume](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_wiltingPoint_percent_volume.md) | No slot description provided<br/>28082 occurrences with subject type sockg:SoilPhysicalSample and object type xsd:double.|
| [sockg_wiltingPointStd_percent_volume](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_wiltingPointStd_percent_volume.md) | No slot description provided<br/>28082 occurrences with subject type sockg:SoilPhysicalSample and object type xsd:double.|
| [sockg_windDirectionDegFromNorth](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_windDirectionDegFromNorth.md) | No slot description provided<br/>147305 occurrences with subject type sockg:WeatherObservation and object type xsd:double.|
| [sockg_windErosionDataAt](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_windErosionDataAt.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type sockg:Field.|
| [sockg_windErosionTreatment](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_windErosionTreatment.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type sockg:Treatment.|
| [sockg_windSpeed_m_per_s](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_windSpeed_m_per_s.md) | No slot description provided<br/>147305 occurrences with subject type sockg:WeatherObservation and object type xsd:double.|
| [sockg_worksAtDepartment](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_worksAtDepartment.md) | No slot description provided<br/>91 occurrences with subject type sockg:Person and object type sockg:Department.|
| [sockg_worksFor](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_worksFor.md) | No slot description provided<br/>35 occurrences with subject type sockg:Person and object type sockg:Organization.|
| [sockg_worksIn](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_worksIn.md) | No slot description provided<br/>165 occurrences with subject type sockg:Person and object type sockg:Site.|
| [sockg_xylan_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_xylan_g_per_kg.md) | No slot description provided<br/>1367 occurrences with subject type sockg:BioMassCarbohydrate and object type xsd:double.|
| [sockg_xylanStd_g_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_xylanStd_g_per_kg.md) | No slot description provided<br/>1367 occurrences with subject type sockg:BioMassCarbohydrate and object type xsd:double.|
| [sockg_yearsBetweenBurns](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_yearsBetweenBurns.md) | No slot description provided<br/>1951 occurrences with subject type sockg:GrazingManagementEvent and object type xsd:double.|
| [sockg_yieldNutrUptakeDataAt](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_yieldNutrUptakeDataAt.md) | No slot description provided<br/>429 occurrences with subject type sockg:YieldNutrientUptake and object type sockg:Field.|
| [sockg_yieldNutrUptakeTreatment](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_yieldNutrUptakeTreatment.md) | No slot description provided<br/>409 occurrences with subject type sockg:YieldNutrientUptake and object type sockg:Treatment.|
| [sockg_zinc_g_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_zinc_g_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|
| [sockg_zincConcentration_mg_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_zincConcentration_mg_per_kg.md) | No slot description provided<br/>6723 occurrences with subject type sockg:BioMassMineral and object type xsd:double.|
| [sockg_zincConcentrationStd_mg_per_kg](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_zincConcentrationStd_mg_per_kg.md) | No slot description provided<br/>6723 occurrences with subject type sockg:BioMassMineral and object type xsd:double.|
| [sockg_zincStd_g_ha](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sockg_zincStd_g_ha.md) | No slot description provided<br/>15 occurrences with subject type sockg:WindErosionArea and object type xsd:double.|







