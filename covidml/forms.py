from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField 
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    molecule_id = StringField(label='Molecule ID', validators=[DataRequired(message="Please enter a molecule ID.")])
    smiles = StringField(label='SMILES', validators=[DataRequired(message="Please enter a SMILES string.")])
    submit = SubmitField(label='Predict')
    