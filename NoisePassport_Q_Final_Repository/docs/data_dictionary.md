# Data Dictionary

## `data/illustrative_model_data.csv`
- `data_status`: provenance; current value is `ILLUSTRATIVE_SYNTHETIC_NOT_MEASURED`.
- `model`: quantum classifier, classical RBF SVM, or optional quantum + abstention.
- `noise_level`: named illustrative condition.
- `noise_severity`: ordinal plotting index, not a physical probability.
- `accuracy`, `balanced_accuracy`, `macro_f1`: example scores from 0 to 1.
- `accuracy_retention`: example fraction of ideal accuracy retained.
- `prediction_flip_rate`: example fraction of predictions that differ from ideal.

## `data/illustrative_resource_data.csv`
- `data_status`: synthetic provenance label.
- `model`: model/configuration name.
- `qubits`: example qubit count.
- `circuit_depth`: example depth.
- `two_qubit_gates`: example two-qubit gate count.
- `shots_per_evaluation`: example shot budget.
- `circuit_evaluations`: example total evaluations.
- `runtime_seconds`: example elapsed time.
- `peak_memory_mb`: example memory.

These are synthetic illustrative data, not measured values. Keep the provenance labels. For measured data, also log dataset/source/license, split seed, run seed, backend/simulator, noise parameters, package versions, sample counts, repetitions, and timestamps.
