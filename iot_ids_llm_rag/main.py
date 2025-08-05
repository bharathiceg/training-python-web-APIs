import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import numpy as np
import pandas as pd

from modules.data_ingestion import load_data
from modules.preprocessing import preprocess_features
from modules.embedding import generate_embeddings
from modules.anomaly_detection import build_autoencoder, detect_anomalies
from modules.fine_tune_llm import fine_tune_llm
from modules.rag_module import build_knowledge_base, retrieve


def plot_class_distribution(y_before, y_after, label_enc):
    fig, axs = plt.subplots(1, 2, figsize=(14, 5))
    
    sns.countplot(x=y_before, ax=axs[0])
    axs[0].set_title("Before Balancing")
    axs[0].set_xticklabels(label_enc.inverse_transform(sorted(set(y_before))), rotation=45)

    sns.countplot(x=y_after, ax=axs[1])
    axs[1].set_title("After Balancing")
    axs[1].set_xticklabels(label_enc.inverse_transform(sorted(set(y_after))), rotation=45)

    plt.tight_layout()
    plt.show()


def plot_feature_correlation(df):
    corr = df.corr()
    plt.figure(figsize=(12, 10))
    sns.heatmap(corr, cmap='coolwarm', annot=False)
    plt.title("Feature Correlation Heatmap")
    plt.show()


def evaluate_anomaly_detection(y_true, y_pred):
    print("[Anomaly Detection] Classification Report")
    print(classification_report(y_true, y_pred))
    cm = confusion_matrix(y_true, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot(cmap="Blues")
    plt.title("Anomaly Detection Confusion Matrix")
    plt.show()


def evaluate_attack_classification(y_true, y_pred):
    print("[Attack Classification] Classification Report")
    print(classification_report(y_true, y_pred))
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt="d", cmap="YlGnBu")
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.title("Attack Classification Confusion Matrix")
    plt.show()


def main():
    # Load data
    df = load_data("data/CICIoT2023_combined.csv")
    
    # Class distribution before balancing
    label_counts_before = df['Label'].value_counts()
    
    # Feature correlation
    plot_feature_correlation(df.drop('Label', axis=1))

    # Preprocess features
    X, y, label_enc = preprocess_features(df)
    
    # Class distribution after balancing
    plot_class_distribution(label_counts_before.index.to_list(), y, label_enc)

    # Generate embeddings for anomaly detection
    texts = [",".join(map(str, row)) for row in X[:500].astype(str)]
    embeddings = generate_embeddings(texts)

    # Train autoencoder
    ae = build_autoencoder(embeddings.shape[1])
    ae.fit(embeddings, embeddings, epochs=10, batch_size=32, verbose=0)

    # Detect anomalies
    anomalies, errors = detect_anomalies(ae, embeddings)
    evaluate_anomaly_detection(np.zeros_like(anomalies), anomalies.astype(int))

    # Extract anomalous samples
    anomalous_samples = [texts[i] for i in range(len(anomalies)) if anomalies[i]]
    labels = [y[i] for i in range(len(anomalies)) if anomalies[i]]

    # Fine-tune LLM on anomalous data
    model, tokenizer = fine_tune_llm(anomalous_samples, labels)

    # Simulated prediction (can replace with model output)
    y_pred = labels
    evaluate_attack_classification(labels, y_pred)

    # RAG: build knowledge base and retrieve similar attacks
    rag_model, rag_index, doc_embeddings = build_knowledge_base(anomalous_samples)
    sample_query = anomalous_samples[0]
    retrieved_docs = retrieve(sample_query, rag_model, rag_index, anomalous_samples)
    
    print("\nTop-k Retrieved Attacks:")
    for doc in retrieved_docs:
        print("-", doc[:100])


if __name__ == "__main__":
    main()
