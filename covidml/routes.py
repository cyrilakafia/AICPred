from covidml import app
from flask import render_template, redirect, url_for, request, flash
from covidml.forms import UploadForm
import pickle
from Mold2_pywrapper import Mold2
from rdkit import Chem


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html', title='Home')

@app.route('/upload', methods = ['GET', 'POST'])
def upload_page():
    form = UploadForm()
    if form.validate_on_submit():
        molecule_id = form.molecule_id.data
        smiles = [str((form.smiles.data))]
        print(smiles)
        
        with open('pregame/pkl/mask1', 'rb') as file:
            mask = pickle.load(file)
            
        with open('pregame/pkl/classifier1', 'rb') as file:
            classifier = pickle.load(file)
        
        try:
            mols = [Chem.MolFromSmiles(smiles) for smiles in smiles]

            mold2 = Mold2()
            df = mold2.calculate(mols, show_banner=False)
        
            df = df.astype(float)
            df = df.round(3)
                
            df = df.loc[:, mask]
                
            pred = classifier.predict(df)
            pred_prob = classifier.predict_proba(df)
                
            if pred == 0:
                confidence = pred_prob[0][0]
                activity = "Inactive"
                    
            if pred == 1:
                confidence = pred_prob[0][1]
                activity = "Active"
                    
            results = {}
            results['molecule_id'] = molecule_id
            results['activity'] = activity
            results['confidence'] = confidence
            
        except Exception as e:
                flash("Invalid SMILES", "danger")
                return render_template('upload.html', title='Error', form = form)

            # return results
        print(results)
        return render_template('upload.html', title='Results', form = form, results=results)
            
    return render_template('upload.html', title='Upload', form=form)

@app.route('/tutorials')
def tutorials_page():
    return render_template('tutorials.html', title='Tutorials')

@app.route('/about')
def faq_page():
    return render_template('faq.html', title='About')

@app.route('/contact')
def contact_page():
    return render_template('contact.html', title='Contact')