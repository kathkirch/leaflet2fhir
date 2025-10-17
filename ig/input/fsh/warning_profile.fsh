Profile: Warning
Parent: ClinicalUseDefinition
Id: warning
Title: "Warning"
Description: "A custom profile for the ClinicalUseDefinition-Resource that is used to display a warning regarding a medication contained in the medication leaflet"

* type = #warning
* warning 1..1 MS
* warning.description ^short = "The long description, the long text of the warning"
* warning.description 1..1 MS

* subject 1..1 MS
* subject ^short = "The medication for which this warning applies"
* subject only Reference (MedicinalProductDefinition)