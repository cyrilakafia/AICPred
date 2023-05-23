# import packages
import pickle 
import numpy as np
import pandas as pd

# check xgboost version
# import xgboost as xgb

# print(xgb.__version__)


def load_model():
    '''Function to load the model'''
    with open('classifier1', 'rb') as file:
        model = pickle.load(file)
    return model

def load_mask():
    '''Function to load the variance threshold mask'''
    with open('mask1', 'rb') as file:
        mask = pickle.load(file)
    return mask

def test_model():
    '''Function to test loaded model and mask'''
    model = load_model()
    mask = load_mask()
    df = pd.read_csv("test.csv")
    df = df.loc[:, mask]
    result = model.predict(df)
    return result

# load model and mask
model = load_model()
mask = load_mask()

#
df = pd.read_csv("test.csv")
df = df.loc[:, mask]

print(df.shape)

df.to_csv('test.csv', index=False)

result = model.predict(df)
print(result)