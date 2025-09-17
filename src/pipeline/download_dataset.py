import kagglehub
import os
import shutil


def download_ds():
    # Ensure target folder exists
    target_path = "src/processed/dataset"
    os.makedirs(target_path, exist_ok=True)

    # Download from KaggleHub (goes to cache by default)
    dataset_path = kagglehub.dataset_download("godaromal/text-to-sql")

    # Copy dataset into your project folder
    if os.path.isdir(dataset_path):
        for file in os.listdir(dataset_path):
            src_file = os.path.join(dataset_path, file)
            dst_file = os.path.join(target_path, file)
            if os.path.isfile(src_file):
                shutil.copy(src_file, dst_file)
    else:
        shutil.copy(dataset_path, target_path)

    print(f"✅ Dataset downloaded and saved to {target_path}")


if __name__ == "__main__":
    download_ds()
import kagglehub
import os
import shutil


def download_ds():
    target_path = "src/processed/dataset"
    os.makedirs(target_path, exist_ok=True)

    dataset_path = kagglehub.dataset_download("godaromal/text-to-sql")

    if os.path.isdir(dataset_path):
        for file in os.listdir(dataset_path):
            src_file = os.path.join(dataset_path, file)
            dst_file = os.path.join(target_path, file)
            if os.path.isfile(src_file):
                shutil.copy(src_file, dst_file)
    else:
        shutil.copy(dataset_path, target_path)

    print(f"Dataset downloaded and saved to {target_path}")

