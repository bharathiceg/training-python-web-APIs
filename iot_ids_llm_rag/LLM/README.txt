# IoT Intrusion Detection System using LLM and RAG

This project implements an **Intrusion Detection System (IDS)** for IoT environments using:
- Anomaly detection with **Autoencoders**
- Attack classification via **fine-tuned LLM**
- **RAG (Retrieval-Augmented Generation)** to retrieve similar attack patterns

Dataset: [CICIoT2023](https://www.unb.ca/cic/datasets/iot2023.html)

---

## 📁 Project Structure

---

## 🧪 Features

- ✅ **Preprocessing & Balancing**
  - Clean NaNs, scale features
  - SMOTE oversampling

- 📊 **Visualizations**
  - Feature correlation heatmap
  - Class distribution (before and after balancing)
  - Confusion matrices for anomaly and multi-attack classification

- 🧠 **Anomaly Detection**
  - Autoencoder trained on embeddings
  - Reconstruction error thresholding

- 📚 **Fine-Tuning LLM**
  - Small BERT-based model trained on anomalous samples
  - Simulated attack classification

- 🔍 **RAG Retrieval**
  - FAISS + SentenceTransformer to find similar past attacks

---

## 🚀 How to Run

### 1. Clone and install dependencies

```bash
pip install -r requirements.txt

### 2. Add Dataset

Download and place CICIoT2023_combined.csv inside the data/ folder.

### 3.Run the pipeline

python main.py

Evaluation Outputs

Feature Correlation Heatmap – shows how features relate

Class Distributions – before and after SMOTE balancing

Anomaly Detection Report – classification + confusion matrix

Attack Classification Report – for fine-tuned LLM

RAG Output – Top-k retrieved similar attacks

Dependencies
All key packages are listed in requirements.txt, including:

pandas, numpy, scikit-learn

tensorflow, matplotlib, seaborn

transformers, datasets, sentence-transformers

faiss-cpu, accelerate, imblearn

Notes
The LLM classification is simulated (you can replace with real inference from Trainer.predict()).

RAG demonstrates a retrieval-based similarity approach, not full generation.

You can plug in any other LLM or anomaly model to extend.

