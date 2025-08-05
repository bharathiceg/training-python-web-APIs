import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import classification_report, confusion_matrix

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

from imblearn.over_sampling import SMOTE

# ===============================
# 📥 1. Load and Preprocess Data
# ===============================

df = pd.read_csv("CICIoT2023_combined.csv")

# Drop unnecessary columns
df = df.drop(columns=["Flow ID", "Timestamp"], errors='ignore')

# Drop missing values
df = df.dropna()

# Encode class labels
label_encoder = LabelEncoder()
df['Label'] = label_encoder.fit_transform(df['Attack_Type'])

# Split features and labels
X = df.drop(columns=["Attack_Type", "Label"])
y = df["Label"]

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ===============================
# 📊 2. Plot Before Balancing
# ===============================

def plot_class_distribution(labels, title):
    label_counts = pd.Series(labels).value_counts().sort_index()
    class_names = label_encoder.inverse_transform(label_counts.index)
    sns.barplot(x=class_names, y=label_counts.values)
    plt.xticks(rotation=90)
    plt.title(title)
    plt.xlabel("Class")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

plot_class_distribution(y, "Class Distribution Before Balancing")

# ===============================
# ⚖️ 3. Balance Dataset using SMOTE
# ===============================

smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_scaled, y)

plot_class_distribution(y_resampled, "Class Distribution After SMOTE Balancing")

# ===============================
# ✂️ 4. Train-Test Split (on Resampled Data)
# ===============================

X_train, X_test, y_train, y_test = train_test_split(
    X_resampled, y_resampled, test_size=0.2, random_state=42, stratify=y_resampled
)

# ===============================
# 🧠 5. Build & Train Neural Network
# ===============================

model = Sequential([
    Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.3),
    Dense(64, activation='relu'),
    Dropout(0.3),
    Dense(len(np.unique(y)), activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

history = model.fit(X_train, y_train, epochs=20, batch_size=64, validation_split=0.2)

# ===============================
# 📈 6. Evaluate Model
# ===============================

y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)

print(classification_report(y_test, y_pred_classes, target_names=label_encoder.classes_))

conf_matrix = confusion_matrix(y_test, y_pred_classes)
plt.figure(figsize=(12, 8))
sns.heatmap(conf_matrix, annot=True, fmt='d',
            xticklabels=label_encoder.classes_,
            yticklabels=label_encoder.classes_,
            cmap='Blues')
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.tight_layout()
plt.show()
# Create a correlation heatmap using raw features (not scaled)
plt.figure(figsize=(18, 12))
corr_matrix = df.drop(columns=["Attack_Type", "Label"]).corr()

# Plot heatmap
sns.heatmap(corr_matrix, cmap='coolwarm', linewidths=0.5)
plt.title("Feature Correlation Heatmap", fontsize=16)
plt.tight_layout()
plt.show()
