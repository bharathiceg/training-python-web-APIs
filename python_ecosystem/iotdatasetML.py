import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from imblearn.over_sampling import SMOTE
from collections import Counter

# Load combined dataset
df = pd.read_csv("C:\\Users\\DELL\\Desktop\\MTD IDS\\MetaMTD\\python coding\\CICIoT2023_combined.csv")
print("The dataset is loaded")


# Drop columns that are not useful
if "Flow ID" in df.columns:
    df = df.drop(columns=["Flow ID", "Timestamp"], errors='ignore')

# Handle missing values
df = df.dropna()

# Encode labels
label_encoder = LabelEncoder()
df['label'] = label_encoder.fit_transform(df['Attack_Type'])

# Split features and labels
X = df.drop(columns=["Attack_Type", "label"])
y = df["label"]

# Print original class distribution
print("Original class distribution:", Counter(y))

# Apply SMOTE to oversample minority classes
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_scaled, y)

# Print new class distribution
print("Resampled class distribution:", Counter(y_resampled))

# Train-test split on resampled data
X_train, X_test, y_train, y_test = train_test_split(
    X_resampled, y_resampled, test_size=0.2, random_state=42, stratify=y_resampled
)