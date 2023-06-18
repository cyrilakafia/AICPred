from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, SelectField, FileField
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    molecule_id = IntegerField(label='Molecule ID', validators=[DataRequired(message="Please enter a valid integer for the molecule ID.")])
    smiles = StringField(label='SMILES', validators=[DataRequired(message="Please enter a SMILES string.")])
    model_type = SelectField(label='Algorithm', choices=[('XGBoost', 'XGBoost'), ('Decision Tree', 'Decision Tree')], validators=[DataRequired()])
    submit = SubmitField(label='Predict')


class UploadFile(FlaskForm):
    file = FileField(label='Upload File', validators=[DataRequired()])
    model_type = SelectField(label='Algorithm', choices=[('XGBoost', 'XGBoost'), ('Decision Tree', 'Decision Tree')], validators=[DataRequired()])
    submit = SubmitField(label='Predict')