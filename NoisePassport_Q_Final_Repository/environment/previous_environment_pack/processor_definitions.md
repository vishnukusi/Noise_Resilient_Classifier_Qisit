# Processor definitions — NoisePassport-Q

## Purpose
These are **simulator profiles** for controlled experiments, not real quantum processors and not calibration data. They operationalize the project plan's ideal, gate-noise-only and readout-noise-only conditions.

## Profiles
- `ideal`: no injected noise; reference condition.
- `gate_noise_low`, `gate_noise_medium`, `gate_noise_high`: illustrative depolarizing-noise stress levels.
- `readout_noise_low`, `readout_noise_medium`, `readout_noise_high`: illustrative asymmetric-capable readout bit-flip profiles (the template uses equal transition probabilities).

The exact values live in `processor_definitions.json`. They are placeholders for a reproducible stress-test grid. Do not describe them as properties of an IBM Quantum device. If the official Q3 specification gives required noise parameters, replace these values with the official values and document the change.

## What to record per run
- profile name and JSON parameters
- simulator/backend name and package versions
- transpiler optimization level and transpiled circuit depth
- shot count and random seeds
- qubit count and two-qubit gate count where available
- training, inference and total wall-clock time (define timing boundaries)
- dataset name, split seed and sample count
- metrics from the held-out test set

## Real-hardware note
If the team later uses a real backend, record its exact name, execution date, relevant calibration snapshot/source, transpilation settings, shots, and job identifier if permitted. Do not label a simulator profile as a real processor.
