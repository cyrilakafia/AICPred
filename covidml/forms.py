from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField 
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    molecule_id = StringField(label='Molecule ID', validators=[DataRequired(message="Please enter a molecule ID.")])
    smiles = StringField(label='SMILES', validators=[DataRequired(message="Please enter a SMILES string.")])
    model_type = SelectField(label='Algorithm', choices=[('XGBoost', 'XGBoost'), ('AdaBoost', 'AdaBoost'), ('Random Forest', 'Random Forest')], validators=[DataRequired()])
    submit = SubmitField(label='Predict')
    