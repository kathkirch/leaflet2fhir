Profile: MLLOrganization
Parent: Organization
Id: medicinal-organization
Title: "MLL Organization"
Description: "A custom profile for Organization-Resources that is used to display information in the package insert for either the drug manufacturer or the marketing authorization holder"

* name ^short = "Name of organisation, the whole name of organization is required"
* name 1..1 MS

* contact.telecom ^slicing.discriminator.type = #value
* contact.telecom ^slicing.discriminator.path = "system"
* contact.telecom ^slicing.rules = #open

* contact.telecom contains fax 0..1 
* contact.telecom[fax].value 0..1
* contact.telecom[fax].system = #fax

* contact.telecom contains website 0..1
* contact.telecom[website].value 0..1
* contact.telecom[website].system = #url

* contact ^short = "The address of organization"
* contact.address 1..1 MS 
* contact.address.text 1..1
* contact.address.line 0..1 
* contact.address.city 1..1 
* contact.address.postalCode 1..1 
* contact.address.country 1..1 