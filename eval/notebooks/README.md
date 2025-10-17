# Evaluation Notebooks

Assets
- compute_evaluation.ipynb — Computes per-field and per-question-set metrics on the shared LLM outputs using binary scoring and aggregate means.
- evaluation.xlsx — Human evaluation sheet; columns include leaflet_id, question_id, field, label (A/M/I/F), human_score, and reviewer comments following the coding rules below.
- medlist.csv — Reference list of evaluated medicinal products with metadata columns (leaflet_id, product_name, atc_code, language, status) governing inclusion.
- randomizer_meds.ipynb — Documents sampling, exclusion (narcotics, homeopathic, veterinary, route filters), and tie-breaking logic for the evaluated set.
- error_code_heatmap.jpg / error_code_heatmap.svg — Visualization outputs summarizing error frequencies across fields.

## Scoring scheme
- Binary decisions per field (1 = correct, 0 = incorrect/missing).
- Aggregation at two levels: mean per question set and mean per field across leaflets.
- Error categories: Assignment (A), Missing (M), Interpretation (I), False/Hallucination (F) 

# How to run:
## Set up Python env with Poetry
poetry install

## Span virt. env 
poetry shell

## Launch notebooks
poetry lab




