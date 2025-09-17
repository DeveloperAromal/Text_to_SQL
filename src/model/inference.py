from transformers import T5Tokenizer, T5ForConditionalGeneration


def text_to_sql(query, model_path):
    
    tokenizer = T5Tokenizer.from_pretrained(model_path)
    
    model = T5ForConditionalGeneration.from_pretrained(model_path)
    
    
    inputs = tokenizer(query, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=128)
    
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
