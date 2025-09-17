import subprocess
import sys
import os


def dep_install():
    
    subprocess.run([sys.executable, "-m", "venv", "venv"])

    if os.name == "nt":
        pip_path = os.path.join("venv", "Scripts", "pip.exe")
    else: 
        pip_path = os.path.join("venv", "bin", "pip")

    dependencies = [
        "torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu",
        "transformers",
        "datasets",
        "pandas",
        "pyyaml",
        "tqdm",
        "accelerate"
    ]

    for dep in dependencies:
        subprocess.run(f"{pip_path} install {dep}", shell=True, check=True)

    print("✅ Virtual environment created and dependencies installed successfully!")
