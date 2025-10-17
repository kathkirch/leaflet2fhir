# Samples

Overview
This directory provides illustrative outputs aligned with the Implementation Guide and evaluation workflow.

fhir_resources/ — FHIR R5 JSON bundles and resources created from the llm output.
llm_outputs/ — Redacted LLM responses.

## FHIR Resource Samples
Each JSON file aligns with the profiles defined in the IG:

cud_1-19251.json → ClinicalUseDefinition/undesirable-effect;warning;contraindication;interaction
mpd_1-19251.json → MedicinalProductDefinition/mpdProfile | Ingredient/active-ingredient;excipient-ingredient
org_1-19251.json → Organization/medicinal-organization
mk_1-19251.json → MedicationKnowledge/medicationKnowledge-leaflet

Local validation
Validate each resource or bundle against a local HAPI-FHIR server with $validate after uploading the relevant StructureDefinition resources.

## LLM Output Samples
- Files follow the pattern `<admission_nr>_<domain>.json`, where `domain` reflects the resource type aligned fields -  `mpd` (MedicinalProductDefinition), `mk` (MedicationKnowledge), `org` (organization), `undes` (undesirable effects as ClinicalUseDefinition), or `icw` (interactions, contraindications, warnings as ClinicalUseDefinition).
- Each file contains a flat JSON object whose keys match the evaluation rubric used in the notebooks. Values are free-text strings lifted from the leaflet excerpts; when multiple bullet points are needed they are pipe-separated (`|`) rather than stored as arrays.
- Missing leaflet content is captured with `null` so that automated scoring can distinguish “not mentioned” from “not parsed”.
