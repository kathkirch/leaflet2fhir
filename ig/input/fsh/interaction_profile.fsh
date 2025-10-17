Profile: Interaction
Parent: ClinicalUseDefinition
Id: interaction
Title: "Interaction"
Description: "Custom  ClinicalUseDefinition profile to describe interactions in medication leaflet."

* type = #interaction
* interaction 1..1 MS
* interaction.type 1..1
* interaction.type.text ^short = "Description for the type of interaction, e.g. drug to drug, alcohol, etc."
* interaction.type.text 1..1
* interaction.effect 1..1
* interaction.effect.concept only CodeableConcept
* interaction.effect.concept.text 1..1
* interaction.effect.concept.text ^short = "Description of the interaction inclusive instructions when to talk to physician"

* subject 1..1 MS
* subject ^short = "The medication for which this is interaction applies"
* subject only Reference (MedicinalProductDefinition)