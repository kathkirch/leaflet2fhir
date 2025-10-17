Profile: ExcipientIngredient
Parent: Ingredient
Id: excipient-ingredient
Title: "Excipient Ingredient"
Description: "Custom Ingredient profile to describe excipient ingredients of a medicinal product"

* for 1..1 MS
* for only Reference(MedicinalProductDefinition)

* role 1..1
* role only CodeableConcept

* role.coding.system = "http://hl7.org/fhir/ingredient-role"
* role.coding.system 1..1
* role.coding.code = #100000072082
* role.coding.code 1..1
* role.coding.display = "excipient"
* role.coding.display 1..1

* substance 1..1
* substance.code 1..1
* substance.code only CodeableReference
* substance.code.concept.text 1..1 
* substance.code.concept.text ^short = "Name of the substance/ingredient"