# NoisePassport-Q — Final Documentation & Analysis Repository

**Project:** Project Q / Qiskit Fall Fest 2026 — Q3 Noise-Resilient Classifier  
**Entry point:** `main.py`  
**Scope:** reproducible analysis of the previously supplied CSV data, report assets, experiment protocol, and environment/noise-profile documentation.

> **Evidence warning:** Both included CSVs are marked `ILLUSTRATIVE_SYNTHETIC_NOT_MEASURED`. All numerical plots generated from them are examples of presentation and analysis only. They are not measured results, do not establish quantum-classifier performance, and must not be presented as experimental findings. The original reports' blank/template figures are preserved in the source reports under `docs/`.

## Included deliverables

1. **End-to-end entry point:** `main.py` reads the supplied CSVs, validates their provenance/schema, writes summary/derived tables, regenerates the figures and records run metadata.
2. **Setup/execution guide:** this README.
3. **Processor and environment definitions:** `configs/processor_definitions.json`, `requirements.txt`, `environment.txt`, and the original environment pack preserved in `environment/`.
4. **Detailed reports:** `reports/technical_report.md`, plus the original uploaded Word reports preserved under `docs/`.
5. **All generated charts:** `figures/01...12...png`.
6. **Supplied CSVs:** both original CSVs copied unchanged into `data/`.
7. **Technical documentation:** architecture, experiment protocol, metric definitions, data dictionary and interpretation guidance.
8. **Tests:** basic automated checks for CSV validation and output generation.

## Repository map

```text
NoisePassport_Q_Final_Repository/
├── README.md
├── main.py
├── requirements.txt
├── environment.txt
├── PROJECT_MANIFEST.json
├── data/
│   ├── illustrative_model_data.csv
│   └── illustrative_resource_data.csv
├── configs/
│   └── processor_definitions.json
├── docs/
│   ├── technical_approach.md
│   ├── data_dictionary.md
│   ├── experiment_protocol.md
│   ├── prototype_evaluation_report_source.docx
│   └── hackathon_implementation_guide_source.docx
├── environment/
│   └── previous_environment_pack/
├── figures/
│   ├── 01_accuracy_vs_noise_synthetic.png
│   ├── 02_macro_f1_vs_noise_synthetic.png
│   ├── 03_balanced_accuracy_synthetic.png
│   ├── 04_retention_and_flip_rate_synthetic.png
│   ├── 05_runtime_synthetic.png
│   ├── 06_circuit_evaluations_synthetic.png
│   ├── 07_shots_per_evaluation_synthetic.png
│   ├── 08_circuit_depth_synthetic.png
│   ├── 09_two_qubit_gates_synthetic.png
│   ├── 10_peak_memory_synthetic.png
│   ├── 11_architecture_tradeoffs_conceptual.png
│   └── 12_evaluation_architecture.png
├── results/
│   ├── model_summary.csv
│   ├── resource_summary.csv
│   ├── quantum_derived_comparisons.csv
│   └── data_provenance.txt
├── reports/
│   └── technical_report.md
├── src/
│   └── analysis.py
└── tests/
    └── test_analysis.py
```

## Setup

Python 3.10+ recommended; Python 3.11 is a reasonable target.

### Windows PowerShell

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### macOS/Linux

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run the analysis

From the repository root:

```bash
python main.py
```

This validates the CSVs, calculates summary/derived tables, regenerates the graphs, and writes `results/run_metadata.json`. It intentionally rejects CSVs that do not retain the synthetic provenance label, so that the example values are not silently presented as measured data.

## Run tests

```bash
pytest -q
```

## What the supplied CSVs say (illustrative only)

The example model CSV shows the quantum-classifier accuracy values 0.90 (Ideal), 0.86 (Low), 0.78 (Medium), and 0.67 (High); the classical RBF-SVM example is 0.88 for each condition row. The resource CSV uses illustrative values of 4 qubits, depth 18, 12 two-qubit gates, 2,048 shots/evaluation, 320 evaluations, 14.2 seconds and 128 MB for the quantum classifier; the quantum-plus-abstention example uses 6,144 shots, 960 evaluations, 39.8 seconds and 140 MB; the classical example has 0 qubits, 0.08 seconds and 42 MB. **These values are copied from the supplied synthetic examples, not measured outcomes.**

## Scientific boundaries and what is still required

The source Prototype Evaluation Report (8 pages) explicitly states that the original plan contained no measured scores, runtime logs, or circuit metadata. The Implementation Guide (10 pages) says its illustrative charts and values must not be submitted as experimental findings. Those two source documents are preserved in `docs/`.

This repository is complete as a **documentation, data-analysis, graph-generation and report package** around the provided CSVs. It does not implement or execute the team's core quantum classifier. If the Q3 judges require an actual end-to-end quantum experiment, the team must independently implement and run the circuit/classifier, export actual outputs and replace the example data through a deliberate, documented workflow. Do not claim hardware validation or quantum advantage without evidence.
