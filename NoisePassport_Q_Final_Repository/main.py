from pathlib import Path
from src.analysis import run

if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    metadata = run(root)
    print("NoisePassport-Q analysis complete.")
    print(f"Run type: {metadata['run_type']}")
    print(f"Data status: {metadata['data_status']}")
    print(f"Tables: {root / 'results'}")
    print(f"Figures: {root / 'figures'}")
    print("Important: supplied CSVs are synthetic examples, not measured quantum results.")
