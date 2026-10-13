from pathlib import Path
import json
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

STATUS = "ILLUSTRATIVE_SYNTHETIC_NOT_MEASURED"
MODEL_COLS = {"data_status","model","noise_level","noise_severity","accuracy","balanced_accuracy","macro_f1","accuracy_retention","prediction_flip_rate"}
RESOURCE_COLS = {"data_status","model","qubits","circuit_depth","two_qubit_gates","shots_per_evaluation","circuit_evaluations","runtime_seconds","peak_memory_mb"}

def load_inputs(root: Path):
    model = pd.read_csv(root/"data"/"illustrative_model_data.csv")
    resource = pd.read_csv(root/"data"/"illustrative_resource_data.csv")
    for label, frame, required in [("model",model,MODEL_COLS),("resource",resource,RESOURCE_COLS)]:
        missing = required - set(frame.columns)
        if missing:
            raise ValueError(f"{label} CSV missing columns: {sorted(missing)}")
        if frame.empty:
            raise ValueError(f"{label} CSV is empty")
        if set(frame["data_status"].astype(str)) != {STATUS}:
            raise ValueError(f"{label} CSV provenance must remain {STATUS}; inspect changes deliberately.")
    for c in ["accuracy","balanced_accuracy","macro_f1","accuracy_retention","prediction_flip_rate"]:
        if not model[c].between(0,1).all():
            raise ValueError(f"{c} must be in [0,1]")
    return model, resource

def plot_line(df, metric, title, filename, root, ylabel):
    fig, ax = plt.subplots(figsize=(9,5.5))
    for name, group in df.groupby("model"):
        group = group.sort_values("noise_severity")
        ax.plot(group["noise_level"], group[metric], marker="o", linewidth=2, label=name)
    ax.set_ylim(0.5,1.0); ax.set_xlabel("Noise condition (ordinal; illustrative)")
    ax.set_ylabel(ylabel); ax.set_title(title + " — synthetic values, not measured")
    ax.grid(True, alpha=.25); ax.legend()
    fig.tight_layout(); fig.savefig(root/"figures"/filename,dpi=190,bbox_inches="tight"); plt.close(fig)

def plot_bar(df, metric, title, filename, root, ylabel):
    fig, ax = plt.subplots(figsize=(9,5.5))
    ax.bar(df["model"], df[metric])
    ax.set_ylabel(ylabel); ax.set_title(title + " — synthetic values, not measured")
    ax.tick_params(axis="x",rotation=15)
    fig.tight_layout(); fig.savefig(root/"figures"/filename,dpi=190,bbox_inches="tight"); plt.close(fig)

def run(root: Path):
    (root/"figures").mkdir(exist_ok=True); (root/"results").mkdir(exist_ok=True)
    m,r = load_inputs(root)
    m.groupby(["model","noise_level","noise_severity"],as_index=False).agg(
        accuracy=("accuracy","mean"),balanced_accuracy=("balanced_accuracy","mean"),
        macro_f1=("macro_f1","mean"),accuracy_retention=("accuracy_retention","mean"),
        prediction_flip_rate=("prediction_flip_rate","mean")
    ).to_csv(root/"results"/"model_summary.csv",index=False)
    r.to_csv(root/"results"/"resource_summary.csv",index=False)
    q=m[m.model=="Quantum classifier"].sort_values("noise_severity")
    ideal=float(q[q.noise_level.str.lower()=="ideal"].iloc[0].accuracy)
    derived=q.copy()
    derived["ideal_accuracy_reference"]=ideal
    derived["accuracy_drop_percentage_points"]=(ideal-derived.accuracy)*100
    derived["retention_recomputed_from_accuracy"]=derived.accuracy/ideal if ideal else None
    derived.to_csv(root/"results"/"quantum_derived_comparisons.csv",index=False)
    plot_line(m,"accuracy","Accuracy vs noise","01_accuracy_vs_noise_synthetic.png",root,"Accuracy (fraction)")
    plot_line(m,"macro_f1","Macro-F1 comparison","02_macro_f1_vs_noise_synthetic.png",root,"Macro-F1 (fraction)")
    plot_line(m,"balanced_accuracy","Balanced accuracy","03_balanced_accuracy_synthetic.png",root,"Balanced accuracy (fraction)")
    fig,ax=plt.subplots(figsize=(9,5.5))
    ax.plot(q.noise_level,q.accuracy_retention,marker="o",label="Accuracy retention")
    ax.plot(q.noise_level,q.prediction_flip_rate,marker="s",label="Prediction flip rate")
    ax.set_ylim(0,1);ax.set_xlabel("Noise condition (ordinal; illustrative)");ax.set_ylabel("Ratio / rate")
    ax.set_title("Retention and prediction flips — synthetic values, not measured")
    ax.grid(True,alpha=.25);ax.legend();fig.tight_layout()
    fig.savefig(root/"figures"/"04_retention_and_flip_rate_synthetic.png",dpi=190,bbox_inches="tight");plt.close(fig)
    plot_bar(r,"runtime_seconds","Runtime comparison","05_runtime_synthetic.png",root,"Runtime (seconds; illustrative)")
    plot_bar(r,"circuit_evaluations","Circuit workload","06_circuit_evaluations_synthetic.png",root,"Circuit evaluations (illustrative)")
    plot_bar(r,"shots_per_evaluation","Shot budget","07_shots_per_evaluation_synthetic.png",root,"Shots/evaluation (illustrative)")
    plot_bar(r,"circuit_depth","Circuit depth","08_circuit_depth_synthetic.png",root,"Depth (illustrative)")
    plot_bar(r,"two_qubit_gates","Two-qubit gate count","09_two_qubit_gates_synthetic.png",root,"Two-qubit gates (illustrative)")
    plot_bar(r,"peak_memory_mb","Peak memory","10_peak_memory_synthetic.png",root,"Memory MB (illustrative)")
    meta={"project":"NoisePassport-Q","run_type":"SUPPLIED_CSV_ANALYSIS_ONLY","data_status":STATUS,
          "quantum_execution_performed":False,"note":"Figures and tables are derived from synthetic illustrative CSVs."}
    (root/"results"/"run_metadata.json").write_text(json.dumps(meta,indent=2),encoding="utf-8")
    return meta
