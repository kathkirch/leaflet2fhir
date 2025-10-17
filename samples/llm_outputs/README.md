# LLM Output Samples

## Layout
- Files follow the pattern `<admission_nr>_<domain>.json`, where `domain` is one of `mpd` (MedicinalProductDefinition-aligned fields), `mk` (MedicationKnowledge-style dosing instructions), `org` (manufacturer/contact data), `undes` (undesirable effects), or `icw` (interactions, contraindications, warnings).
- Each file contains a flat JSON object whose keys match the evaluation rubric used in the notebooks. Values are free-text strings lifted from the leaflet excerpts; when multiple bullet points are needed they are pipe-separated (`|`) rather than stored as arrays.
- Missing leaflet content is captured with `null` so that automated scoring can distinguish “not mentioned” from “not parsed”.

## Field conventions
- Textual fields preserve leaflet wording, including German sentences and typographic characters from the source PDFs.
- Numeric strings such as `dose_and_rate`, `max_dose_per_intake`, or `max_dose_per_period` encode simple scalars that downstream scripts cast to numbers during evaluation.
- Composite description fields (e.g., `modeOfAction`, `interaction_medications`) are intentionally verbose because they are scored via exact/partial string matching and manual review.

## Example (`1-19251_mpd.json`)
```json
{
  "nameDoseFormPart": "Filmtabletten",
  "nameStrengthPart": "10 mg/500 mg",
  "fullName": "Buscopan® plus Paracetamol 10 mg/ 500 mg Filmtabletten",
  "admission_nr": "1-19251",
  "modeOfAction": "Buscopan plus Paracetamol enthält zwei Wirkstoffe: Hyoscin-N-butylbromid und Paracetamol. ...",
  "indication": "Krampfartige Schmerzen im Bereich des Magen-Darm-Traktes; ..."
}
```
The `icw` files expose pipe-delimited interaction statements, while `undes` files summarize adverse reactions and safety signals keyed to the ClinicalUseDefinition profile.

## Usage notes
- Notebooks under [`../../eval/notebooks/`](../../eval/notebooks/) load these JSON objects directly; keep keys stable if you extend the dataset.
- When converting to FHIR Instances, map each domain file to the corresponding resource type referenced in the IG.
- These samples are illustrative and omit sensitive orchestration metadata. All content originates from public medicinal product leaflets; no patient-level information is included.
