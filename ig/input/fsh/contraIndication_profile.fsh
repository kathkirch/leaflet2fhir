Profile: Contraindication
Parent: ClinicalUseDefinition
Id: contraindication
Title: "Contraindication"
Description: "Custom Profile used in IG to display leaflet information in fhir"

* type = #contraindication
* contraindication 1..1 MS
* contraindication.diseaseSymptomProcedure 1..1
* contraindication.diseaseSymptomProcedure only CodeableReference
* contraindication.diseaseSymptomProcedure.concept.text ^short = "Description of Contraindication"
* contraindication.diseaseSymptomProcedure.concept.text 1..1

* subject 1..1 MS
* subject ^short = "The medication for which this is an contraindication"
* subject only Reference (MedicinalProductDefinition)