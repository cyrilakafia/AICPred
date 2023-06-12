from covidml import app
from flask import render_template, redirect, url_for, request, flash
from covidml.forms import UploadForm
from covidml.faq_contacts import faqs, contacts
from covidml.processes import load_model, predict_activity, calculate_molecular_weight, smiles_to_image
from covidml.processes import applicability_domain


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
            results['model_type'] = model_type
            results['mw'] = molecular_weight
            results['activity'] = activity
            results['confidence'] = confidence
            results['molecule_id'] = molecule_id
            results['adAnalysis'] = ad_analysis
            results['smiles'] = smiles[0]
            results['image'] = structure_img
            results['adImage'] = ad_img
            
        except Exception as e:
            flash("Invalid SMILES", "danger")
            return render_template('upload.html', title='Error', form = form)

            # return results
        return render_template('upload.html', title='Results', form=form, results=results)
            
    return render_template('upload.html', title='Upload', form=form)

@app.route('/tutorials')
def tutorials_page():
    return render_template('tutorials.html', title='Tutorials')