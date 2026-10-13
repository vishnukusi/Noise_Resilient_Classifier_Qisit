# Technical Approach

## Purpose
NoisePassport-Q makes classifier performance under controlled noise and resource costs auditable. The original plan defines an evaluation layer around a team-designed QML classifier, not a claim of quantum advantage.

## Workflow in this repository
1. Read the supplied model-performance and resource-usage CSVs.
2. Validate required columns and synthetic provenance.
3. Generate model summaries and derived ideal-to-noisy accuracy differences.
4. Produce separate charts for accuracy, Macro-F1, balanced accuracy, retention/flip rate, runtime, circuit evaluations, shots, depth, two-qubit gates and memory.
5. Include a qualitative architecture trade-off figure and system-flow diagram.
6. Save generated tables under `results/` and charts under `figures/`.
7. Preserve the original uploaded reports and processor/environment pack.

## Experiment design from the source reports
The Prototype Evaluation Report and Implementation Guide recommend: a fixed binary dataset split; train-only preprocessing; ideal, gate-only low/medium/high, and readout-only low/medium/high conditions; combined noise as an extension; a classical RBF-SVM baseline on the same split; repeated seeds when feasible; and logging metrics, resource metadata, environment and run failures.

## Metrics
- Accuracy = correct predictions / all predictions.
- Balanced accuracy = mean recall across classes.
- Macro-F1 = unweighted mean of class-specific F1.
- Performance drop = ideal score − noisy score, in percentage points.
- Accuracy retention = noisy accuracy / ideal accuracy if ideal accuracy > 0.
- Prediction flip rate = fraction of paired test examples whose noisy prediction differs from the ideal prediction.
- Coverage = accepted predictions / all test examples.
- Selective risk = errors among accepted predictions / accepted predictions.
- Run variability = mean and standard deviation across independent repeats.

## Architecture impact
More qubits/wider encoding may increase representational capacity but also simulation and encoding costs. Deeper circuits/more entanglers may increase expressive capacity but add gate-error opportunities and runtime. More shots/repeats may stabilize estimates but increase total execution cost. Abstention may reduce accepted-prediction risk at the cost of coverage. These are hypotheses to test, not measured conclusions.

## Evidence boundary
The plots in this repository are generated from the supplied synthetic example CSVs. They show reporting mechanics, not actual measured performance. The underlying quantum circuit/model must be independently implemented and run by the team if required by the competition.
