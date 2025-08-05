import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from imblearn.over_sampling import SMOTE

def clean_data(df):
    df = df.dropna()
    df = df.drop_duplicates()
    return df

def balance_data(X, y):
    smote = SMOTE()
    return smote.fit_resample(X, y)

def preprocess_features(df):
    df = clean_data(df)
    label_enc = LabelEncoder()
    df['Label'] = label_enc.fit_transform(df['Label'])

    X = df.drop('Label', axis=1)
    y = df['Label']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_bal, y_bal = balance_data(X_scaled, y)
    return X_bal, y_bal, label_enc
