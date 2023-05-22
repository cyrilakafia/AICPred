import pickle 
import numpy as np
import pandas as pd

def load_model():
    with open('classifier1', 'rb') as file:
        model = pickle.load(file)
    return model


df = pd.read_csv("../../final_dataset.csv")

# chose first row of the dataset
df = df.iloc[0]
print(df.shape)

# model = load_model()

# result = model.predict(df[0])