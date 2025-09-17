from transformers import T5Tokenizer
from datasets import Dataset

import pandas as pd
import os

def do_preprocess(batch):
    
    ds_path = os.path.abspath("src/processed/train")
    
    df = pd.read_csv(ds_path)
    ds = Dataset.from_pandas(df)
    
    tokenizer = T5Tokenizer.from_pretrained("t5_small")

    def preprocess():    
        inputs = tokenizer(batch["natural_language_query"], max_length=128, truncation = True, padding = "max_length")
        labels = tokenizer(batch["sql_query"], max_length=128, truncation = True, padding = "max_length")
        inputs["labels"] = labels["input_ids"]
        
        return inputs
    
    
    dataset = ds.map(preprocess, batched = True)
    train_test = dataset.train_test_split(test_size = 0.1)
    
    
    return train_test["train"], train_test["test"], tokenizer





    
    
    