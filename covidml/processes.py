import pickle
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from rdkit import Chem
from Mold2_pywrapper import Mold2
from rdkit.Chem import Draw
from base64 import b64encode
from io import BytesIO

matplotlib.use('Agg')

plt.style.use('covidml\static\stylesheet\ssass.mplstyle')

def load_model(model_type):
    with open(f'covidml/models/{model_type}/mask1', 'rb') as file:
        mask = pickle.load(file)
            
    with open(f'covidml/models/{model_type}/classifier1', 'rb') as file:
        classifier = pickle.load(file)
        
    return mask, classifier

def predict_activity(smiles, mask, classifier):
    mols = [Chem.MolFromSmiles(smiles) for smiles in smiles]

    mold2 = Mold2()
    df = mold2.calculate(mols, show_banner=False)
    
    df = df.astype(float)
    df = df.round(3)
    
    df_original = df.copy()
        
    df = df.loc[:, mask]
        
    pred = classifier.predict(df)
    pred_prob = classifier.predict_proba(df)
        
    if pred == 0:
        confidence = pred_prob[0][0]
        activity = "Inactive"
            
    if pred == 1:
        confidence = pred_prob[0][1]
        activity = "Active"
        
    return activity, confidence, df_original

def calculate_molecular_weight(smiles):
    compound = Chem.MolFromSmiles(smiles)
    molecular_weight = Chem.rdMolDescriptors.CalcExactMolWt(compound)
    return molecular_weight

def smiles_to_image(smiles):
    compound = Chem.MolFromSmiles(smiles)
    image = Draw.MolToImage(compound)
    
    byte_stream = BytesIO()
    image.save(byte_stream, format='PNG')
    byte_stream.seek(0)
    return b64encode(byte_stream.getvalue()).decode('utf-8')

def applicability_domain(id, df):
    means = np.load('covidml/models/AD/means.npy')
    stds = np.load('covidml/models/AD/stds.npy')
    
    with open('covidml/models/AD/variance_filter_mask', 'rb') as file:
        mask = pickle.load(file)
        
        
    df['ID'] = id
    
    cols = df.columns.tolist()
    df = df.reindex(columns=[cols[-1]] + cols[:-1])

    
    try:
        df = df.loc[:, mask]
    except Exception as e:
        print("An error occurred: ")
        print(e)
        
    
    df.drop(['ID'], inplace=True, axis=1)
    
    for i, column in enumerate(df.columns, 0):
        df[column] = (df[column] - means[i])/stds[i]
        

    max_value = df.iloc[0].max()

    min_value = df.iloc[0].min()

    values = [id, min_value]
    

    if max_value > 3:
        if min_value > 3:
            output = 'Not in Domain'
            values[1] = min_value
        else: 
            mean_des = df.iloc[0].mean()
            std_des = df.iloc[0].std()
            s_new = mean_des + (1.28 * std_des)
            if s_new > 3:
                output = 'Not in Domain'
                values[1] = s_new
            else:
                output = 'Within Domain'
                values[1] = s_new
    else:
        output = 'Within Domain'
        values[1] = max_value
    
    cid1 = np.load('covidml/models/AD/in_domain_cids_train.npy')
    cid2 = np.load('covidml/models/AD/out_domain_cids_train.npy')

    stan1 = np.load('covidml/models/AD/in_domain_train.npy')
    stan2 = np.load('covidml/models/AD/out_domain_train.npy')
    

    plt.scatter(np.log(cid1), stan1, color = 'b',  s=20, alpha=0.5, label="Train", marker="h", edgecolors='black')
    plt.scatter(np.log(cid2), stan2, color = 'b',  s=20, alpha=0.5, marker="h", edgecolors='black')
    
    plt.scatter(np.log(int(id)), values[1], color = 'r',  s=90, alpha=0.9, label="Test", marker="h", edgecolors='black')
    
    plt.axhline(3, color = 'black', ls= '--')
    plt.ylim(bottom=0.2, top=7)
    plt.xlabel("Log(Compound CID)")
    plt.ylabel("Standardized Descriptor Values")
    plt.title('Applicability Domain Analysis')
    plt.legend()
    try:
        byte_stream = BytesIO()
        plt.savefig(byte_stream, format='PNG', dpi=80, bbox_inches='tight')
        byte_stream.seek(0)
    
        plot_data = b64encode(byte_stream.getvalue()).decode('utf-8')
    
        plt.clf()
        plt.close()
    except Exception as e:
        print("An error occurred: ")
        print(e)
    print("DONEEEEEEEE")
    
    return plot_data, output
    