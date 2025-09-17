from transformers import T5Tokenizer
from datasets import Dataset

import pandas as pd
import os

def do_preprocess(dataset_path, model_name):
    
    df = pd.read_csv(dataset_path)
    ds = Dataset.from_pandas(df)

    tokenizer = T5Tokenizer.from_pretrained(model_name)

    def preprocess(batch):
        
        inputs = tokenizer(
                            batch["natural_language_query"],
                            max_length=128,
                            truncation=True,
                            padding="max_length"
                         )
        
        labels = tokenizer(
                            batch["sql_query"],
                            max_length=128,
                            truncation=True,
                            padding="max_length"
                          )
        
        inputs["labels"] = labels["input_ids"]
        return inputs

    dataset = ds.map(preprocess, batched=True)
    train_test = dataset.train_test_split(test_size=0.1)

    return train_test["train"], train_test["test"], tokenizer

    
    