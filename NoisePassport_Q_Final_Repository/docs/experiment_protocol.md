# Experiment Protocol — For a Real Run

1. Verify the official Q3 rubric and approved dataset requirements.
2. Select and cite a dataset; document labels, preprocessing, and license.
3. Freeze train/validation/test split and seed. Fit all transformations on training data only. Use patient/group-aware splits if records are correlated.
4. Team independently implements and understands the quantum classifier, feature encoding, circuit, training method, measurement and class mapping.
5. Run ideal, gate-only low/medium/high, and readout-only low/medium/high. Add combined noise if time and specification allow.
6. Compare with a classical baseline on the same held-out split.
7. Repeat selected conditions across independent seeds if feasible.
8. Log accuracy, balanced accuracy, Macro-F1, performance drop, retention, prediction flip rate, coverage/selective risk if used, qubits, transpiled depth, two-qubit gates, shots, circuit evaluations, runtime, memory if measured, backend, parameters and package versions.
9. Generate plots from raw measured CSVs. Do not infer runtime or resources from accuracy.
10. Report means and standard deviations for repeated runs; do not claim significance from a single run.
11. Never relabel the provided synthetic CSVs as measured. The current analysis deliberately guards against this.
