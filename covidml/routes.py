from covidml import app
from flask import render_template, redirect, url_for, flash, send_file, request, get_flashed_messages
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

    contact_list = contacts()
    
    return render_template('home.html', contacts=contact_list)

@app.route('/upload', methods = ['GET', 'POST'])
def upload_page():
    form = UploadForm()
    file_form = UploadFile()
    results = {}
    is_file_tab = False

    if request.args.get('tab') == 'smiles':
        try: 
            if form.validate_on_submit():
                molecule_id = form.molecule_id.data
                smiles = [str((form.smiles.data))]
                model_type = str((form.model_type.data))
                
                mask, classifier = load_model(model_type)    
            
                activity, confidence, df_original = predict_activity(smiles, mask, classifier)
                
                molecular_weight = calculate_molecular_weight(smiles[0])
                    
                structure_img = smiles_to_image(smiles[0])
                    
                ad_img, ad_analysis = applicability_domain(molecule_id, df_original)
                    
                results['molecule_id'] = molecule_id
                if len(smiles[0]) > 80:
                    results['smiles'] = smiles[0][:80] + '...'
                else:
                    results['smiles'] = smiles[0]
                results['mw'] = molecular_weight
                results['activity'] = activity
                results['confidence'] = confidence
                results['ad'] = ad_analysis
                
                if not os.path.exists('covidml/static/temp/'):
                    os.mkdir('covidml/static/temp/')
                
                if os.path.exists('covidml/static/temp/results.csv'):
                    os.remove('covidml/static/temp/results.csv')
                    
                df = pd.DataFrame(results, index=[0])
                df.to_csv('covidml/static/temp/results.csv', index=False)
                    
                    
                results['model_type'] = model_type
                results['image'] = structure_img
                results['adImage'] = ad_img
                
        except Exception as e:
            print(e)
            flash("Invalid SMILES, enter a valid SMILES to make a prediction", category="danger")

    elif request.args.get('tab') == 'file':
        is_file_tab = True
        if request.method == 'POST':
            f = request.files['file']
            f.filename = secure_filename(f.filename)
            f.save(f.filename)
            
            # check if file is a text file
            if f.filename.split('.')[-1] != 'txt':
                flash("Invalid file type, please upload a text file", "danger")
            
            # check if file is empty
            if os.stat(f.filename).st_size == 0:
                flash("File is empty, please upload a text file with SMILES", "danger")
            
            # check how many non empty lines are in the txt file
            
            lines = 0
            with open(f.filename, 'r') as file:
                for l in file:
                    if l.strip():
                        lines += 1
            
            for line in range(lines):
                with open(f.filename, 'r') as file:
                    content = file.readlines()
                
                content = content[line].strip().replace('\n', '').split(' ')
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

                    if not os.path.exists('covidml/static/temp/'):
                        os.mkdir('covidml/static/temp/')
                
                    if os.path.exists('covidml/static/temp/results.csv'):
                        os.remove('covidml/static/temp/results.csv')
                    
                    df = pd.DataFrame(results, index=[0])
                    df.to_csv('covidml/static/temp/results.csv', index=False)              
                                    
                    results['model_type'] = model_type
                    results['image'] = structure_img
                    results['adImage'] = ad_img
                
                except Exception as e:
                    flash("Invalid SMILES provided in text file", "danger")
                
            # remove uploaded file
            os.remove(f.filename)

    else:
        return redirect(url_for('upload_page', tab='smiles'))

    return render_template('upload.html', title='Upload', form=form, file_form=file_form, results=results, is_file_tab=is_file_tab)


@app.route('/tutorials')
def tutorials_page():
    steps = [
        {'title': 'Step 1', 'img': 'static/images/tutorials/1_1.png', 'text': 'Description of step 1...'},
        {'title': 'Step 2', 'img': 'static/images/tutorials/2_2.png', 'text': 'Description of step 2...'},
        {'title': 'Step 3', 'img': 'static/images/tutorials/3_3.png', 'text': 'Description of step 3...'},
        {'title': 'Step 4', 'img': 'static/images/tutorials/4_4.png', 'text': 'Description of step 3...'},
        {'title': 'Step 5', 'img': 'static/images/tutorials/5_5.png', 'text': 'Description of step 3...'}
        ]
    return render_template('tutorials.html', title='Tutorials', steps=steps)

@app.route('/faqs')
def faqs_page():

    faq_list = faqs()
    
    return render_template('faqs.html', faqs=faq_list)

@app.route('/download_csv')
def download_csv():
    return send_file('static/temp/results.csv', as_attachment=True)

@app.route('/download_test_file')
def download_test_file():
    return send_file('static/test.txt', as_attachment=True)