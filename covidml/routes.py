from covidml import app
from flask import render_template, redirect, url_for, request, flash, send_file
from covidml.forms import UploadForm, UploadFile
from covidml.faq_contacts import faqs, contacts
from covidml.processes import load_model, predict_activity, calculate_molecular_weight, smiles_to_image
from covidml.processes import applicability_domain
from werkzeug.utils import secure_filename

import pandas as pd
import os

@app.route('/')
@app.route('/home')
def home_page():

    faq_list = faqs()
    contact_list = contacts()
    
    return render_template('home.html', faqs=faq_list, contacts=contact_list)

@app.route('/upload', methods = ['GET', 'POST'])
def upload_page():
    form = UploadForm()
    if form.validate_on_submit():
        molecule_id = form.molecule_id.data
        smiles = [str((form.smiles.data))]
        model_type = str((form.model_type.data))
        
        mask, classifier = load_model(model_type)    
         
        try:
            
            activity, confidence, df_original = predict_activity(smiles, mask, classifier)
            

            molecular_weight = calculate_molecular_weight(smiles[0])
            
            structure_img = smiles_to_image(smiles[0])
            
            ad_img, ad_analysis = applicability_domain(molecule_id, df_original)
            
            
            results = {}
            results['molecule_id'] = molecule_id
            if len(smiles[0]) > 80:
                results['smiles'] = smiles[0][:80] + '...'
            else:
                results['smiles'] = smiles[0]
            results['mw'] = molecular_weight
            results['activity'] = activity
            results['confidence'] = confidence
            results['ad'] = ad_analysis
            
            os.remove('covidml/static/temp/results.csv')
            df = pd.DataFrame(results, index=[0])
            df.to_csv('covidml/static/temp/results.csv', index=False)
            
            
            results['model_type'] = model_type
            results['image'] = structure_img
            results['adImage'] = ad_img
            
            
        except Exception as e:
            flash("Invalid SMILES", "danger")
            return render_template('upload.html', title='Error', form = form)

            # return results
        return render_template('upload.html', title='Results', form=form, results=results)
            
    return render_template('upload.html', title='Upload', form=form)


@app.route('/upload_file', methods = ['GET', 'POST'])
def upload_file_page():
    file_form= UploadFile()
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
    
        with open(f.filename, 'r') as file:
            content = file.readlines()
            
        content = content[0].strip().split(' ')
        molecule_id = content[0]
        smiles = [str(content[1])]
        model_type = str((file_form.model_type.data))
        
        mask, classifier = load_model(model_type)
        
        try:
            
            activity, confidence, df_original = predict_activity(smiles, mask, classifier)
            

            molecular_weight = calculate_molecular_weight(smiles[0])
            
            structure_img = smiles_to_image(smiles[0])
            
            ad_img, ad_analysis = applicability_domain(molecule_id, df_original)
            
            
            results = {}
            results['molecule_id'] = molecule_id
            if len(smiles[0]) > 80:
                results['smiles'] = smiles[0][:80] + '...'
            else:
                results['smiles'] = smiles[0]
            results['mw'] = molecular_weight
            results['activity'] = activity
            results['confidence'] = confidence
            results['ad'] = ad_analysis
            
            os.remove('covidml/static/temp/results.csv')
            df = pd.DataFrame(results, index=[0])
            df.to_csv('covidml/static/temp/results.csv', index=False)
            
            
            results['model_type'] = model_type
            results['image'] = structure_img
            results['adImage'] = ad_img
            
            
        except Exception as e:
            flash("Invalid SMILES", "danger")
            return render_template('upload_file.html', title='Error', file_form = file_form)
        
        
        return render_template('upload_file.html', title='Results', file_form=file_form, results=results)
    return render_template('upload_file.html', title='Upload File', file_form=file_form)


@app.route('/tutorials')
def tutorials_page():
    return render_template('tutorials.html', title='Tutorials')

@app.route('/download_csv')
def download_csv():
    return send_file('static/temp/results.csv', as_attachment=True)