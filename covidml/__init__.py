from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a43688ca7d6f595a88b0ff8f'
app.config['UPLOAD_FOLDER'] = 'covidml/static/temp'

from covidml import routes