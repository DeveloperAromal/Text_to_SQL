import yaml
from transformers import T5ForConditionalGeneration, Trainer, TrainingArguments
import os

from src.model.preprocess import do_preprocess



def train():
    
    config_path = os.path.join("src/config/model.conf.yaml")
    
    with open(config_path) as f:
        config = yaml.safe_load(f)
        
    
    
    model_name = config["model"]["name"]
    model_save_path = config["paths"]["model_dir"]
    
    model = T5ForConditionalGeneration.from_pretrained(model_name)


    train_dataset, eval_dataset, tokenizer = do_preprocess(config["paths"]["train_data"], model_name)
    
    training_args = TrainingArguments(
                                        output_dir=config["paths"]["output_dir"],
                                        num_train_epochs=config["training"]["num_train_epochs"],
                                        per_device_train_batch_size=config["training"]["per_device_train_batch_size"],
                                        per_device_eval_batch_size=config["training"]["per_device_train_batch_size"],
                                        eval_strategy=config["training"]["eval_strategy"],
                                        save_strategy=config["training"]["save_strategy"],
                                        logging_strategy="steps",
                                        logging_steps=config["training"]["logging_steps"],
                                        learning_rate=config["training"]["learning_rate"],
                                     )
    
    trainer = Trainer(
                        model=model,
                        args=training_args,
                        train_dataset=train_dataset,
                        eval_dataset=eval_dataset,
                     )
    
    trainer.train()
    trainer.save_model(model_save_path)
    tokenizer.save_pretrained(model_save_path)