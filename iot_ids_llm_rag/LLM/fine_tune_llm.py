from transformers import AutoModelForSequenceClassification, Trainer, TrainingArguments, AutoTokenizer
from datasets import Dataset

def fine_tune_llm(texts, labels, model_name='distilbert-base-uncased'):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=len(set(labels)))
    
    dataset = Dataset.from_dict({"text": texts, "label": labels})
    dataset = dataset.map(lambda x: tokenizer(x["text"], truncation=True, padding=True), batched=True)

    training_args = TrainingArguments(output_dir="./llm_out", per_device_train_batch_size=4, num_train_epochs=1)
    trainer = Trainer(model=model, args=training_args, train_dataset=dataset)
    trainer.train()
    return model, tokenizer
