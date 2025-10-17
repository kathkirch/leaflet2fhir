ValueSet: OrderableDrugForm
Id: orderableDrugForm
Title: "Orderable drugform ValueSet"
Description: "A value set for orderable drugfrom of medicinal products"
* ^experimental = true
* include codes from system http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm

ValueSet: DoseForm
Id: dose-form
Title: "Doseform ValueSet"
Description: "A value set for dose forms"
* ^experimental = true
* include codes from system http://snomed.info/sct where concept is-a #736542009

ValueSet: BlackTriangleMonitoring
Id: blacktrianglemonitoring
Title: "Black Triangle ValueSet"
Description: "Code System for black triangle monitoring information"
* ^experimental = true
* include codes from system http://hl7.org/fhir/medicinal-product-additional-monitoring


// Own ValueSet
ValueSet: DosingInstructionCodes
Id: dosinginstructioncodes
Title: "Instruction Codes for Medication Intake"
Description: "A set of SNOMED CT codes describing various scenarios related to the administration of medication."
* ^experimental = true
* http://snomed.info/sct#223422006 "Recommendation regarding what to do if drug omitted"
* http://snomed.info/sct#260378005 "Excessive"
* http://snomed.info/sct#410546004 "Discontinued"
* http://snomed.info/sct#422096002 "Dosing instruction fragment"
* http://snomed.info/sct#261773006 "Duration of therapy"

