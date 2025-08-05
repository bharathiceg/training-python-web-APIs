from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
import numpy as np

def build_autoencoder(input_dim):
    input_layer = Input(shape=(input_dim,))
    encoded = Dense(64, activation="relu")(input_layer)
    decoded = Dense(input_dim, activation="linear")(encoded)
    autoencoder = Model(inputs=input_layer, outputs=decoded)
    autoencoder.compile(optimizer='adam', loss='mse')
    return autoencoder

def detect_anomalies(autoencoder, data, threshold=0.01):
    recon = autoencoder.predict(data)
    errors = np.mean(np.square(data - recon), axis=1)
    anomalies = errors > threshold
    return anomalies, errors
