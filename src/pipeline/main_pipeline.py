from src.pipeline.download_dataset import download_ds
from src.pipeline.inspect import inspect
from src.model.train import train
from src.model.inference import text_to_sql

def pipeline():
    inspect()
    download_ds()
    train()
    text_to_sql()
    