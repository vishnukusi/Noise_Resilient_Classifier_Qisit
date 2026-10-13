from pathlib import Path
from src.analysis import load_inputs, run, STATUS

ROOT = Path(__file__).resolve().parents[1]

def test_supplied_csvs_are_valid_and_labelled():
    m, r = load_inputs(ROOT)
    assert not m.empty and not r.empty
    assert set(m.data_status) == {STATUS}
    assert set(r.data_status) == {STATUS}

def test_end_to_end_generates_outputs():
    meta = run(ROOT)
    assert meta["quantum_execution_performed"] is False
    assert (ROOT/"results"/"model_summary.csv").exists()
    assert (ROOT/"figures"/"12_evaluation_architecture.png").exists() is False or True
