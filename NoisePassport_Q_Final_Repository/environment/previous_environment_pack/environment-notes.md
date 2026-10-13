# Environment notes — fill in after setup

- Python version:
- Operating system:
- CPU / RAM:
- Virtual environment name:
- Install command:
- Successful smoke-test date:
- Qiskit version:
- Qiskit Aer version:
- Qiskit Machine Learning version:
- Qiskit Algorithms version:
- Dataset and split seed:
- Git commit:
- Known install/runtime issues:

## Setup (recommended)
Windows PowerShell:
```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -c "import qiskit, qiskit_aer; print(qiskit.__version__, qiskit_aer.__version__)"
python -m pip freeze > environment-lock.txt
```

macOS / Linux:
```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python -c "import qiskit, qiskit_aer; print(qiskit.__version__, qiskit_aer.__version__)"
python -m pip freeze > environment-lock.txt
```

The pins are inherited from the supplied prototype plan and must be validated in your environment. If installation fails, resolve compatibility and record the exact working versions rather than claiming the template was tested.
