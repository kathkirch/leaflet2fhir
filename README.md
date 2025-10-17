# FHIR Integration and Evaluation Artifacts for Medication Leaflet Information Extraction

Research Artifacts
A curated artifact set for mapping Austrian medicinal leaflets to FHIR R5.

Overview
This repository accompanies "INTEGRATING MEDICATION LEAFLETS UTILIZING FHIR AND AN LLM-BASED QUESTION-ANSWER PIPELINE IN A MOBILE APPLICATION" (2025) and distributes the research-facing assets that underpin the leaflet-to-FHIR pipeline while intentionally withholding the production ingestion stack, orchestration services, and mobile application used in deployment. You will find FSH definitions, IG configuration, prompt question sets, sample extractions, and evaluation notebooks. Proprietary backend code, security-hardened infrastructure, and commercialization components remain private to protect IP and mitigate supply-chain risk.

Repo Map
```text
.
|-- ig/                      # FHIR Implementation Guide configuration & FSH sources
|   |-- ig.ini               # IG Publisher entrypoint
|   `-- sushi-config.yaml    # Canonical metadata for SUSHI
|
|-- prompts/                 # Question sets and a TXT subset of leaflets
|   |-- leaflet_as_txt/      # Leaflets as plain text used for extraction
|   `-- sets.py              # Question sets (LLM prompts)
|
|-- samples/                 # Illustrative bundles and model outputs
|   |-- fhir_resources/      # JSON resources conforming to IG profiles
|   |-- llm_outputs/         # Sample model answers
|   `-- README.md            # Directory index
|
|-- eval/                    # Evaluation assets
|   |-- notebooks/           # Notebooks, metrics, and exports
|   |-- eval_meds_list.csv   # List of medicinal products used in evaluation
|   `-- README.md            # Usage notes
|
|-- pyproject.toml           # Poetry project definition (Python 3.10+)
|-- poetry.lock              # Locked Python dependency graph
|-- LEGAL_NOTICE.md          # Redistribution and use statement
`-- .gitignore               # Ignored file patterns
```

# Quickstart

## Prerequisites:

Node.js (tested with 18+) with global fsh-sushi
Java 17+ for the HL7 IG Publisher
Python 3.10+ with Poetry matching pyproject.toml
Docker Desktop (optional) for a local HAPI-FHIR server
Java 17+ is required and JAVA_HOME may need to be set manually before running the publisher.

---
# Implementation Guide Creation

### Install SUSHI
```bash
npm install -g fsh-sushi
```
### Download/run IG Publisher (example helper script; adapt if you keep a local _tools helper)
(Place the downloaded jar in ./ig/input-cache or use your preferred setup)

Example publisher invocation via ig.ini:
```bash
java -jar ./_publisher/publisher.jar -ig ig/ig.ini -watch -tx n/a
```

## Build profiles -> FHIR artifacts (SUSHI)
```bash
cd ig/fsh 
sushi -s .
``` 

## Build IG
```bash
java -jar validator_cli.jar samples/fhir_bundles/example.json -ig output/package.tgz -version 5.0.0
```
NOTE: The IG Publisher writes the rendered site and QA reports to ig/build/output. 

---
## Reproducing the Samples
- Question sets live in prompts/questionsets/ 
- Sample LLM outputs are in samples/llm_outputs/ and demonstrate the answer schema.
- Sample FHIR resources as JSON reside in samples/fhir_resources/ and align with the IG profiles.
---
## Sampling & exclusions 
eval/eval_meds_list.csv enumerates medicinal products by their admission number evaluated in the study.
Sampling logic, randomization, and exclusion filters (narcotics, homeopathic remedies, veterinary products, administration route constraints) are documented in eval/notebooks/randomizer_meds.ipynb.
---
# Code Availability
Included: FSH source files, IG configuration, question sets and evaluation notebooks. Withdrawn: the production ingestion services, LLM orchestration workflows, mobile applications, and deployment automation that power the commercial product, in order to safeguard IP and maintain security boundaries.
---
# Data Availability
Included: a TXT subset of public medicinal leaflets in prompts/leaflet_as_txt/, LLM outputs in samples/llm-outputs, human-evaluation results in eval/notebooks/evaluation.xlsx, and sample FHIR resources in samples/fhir_resources. 