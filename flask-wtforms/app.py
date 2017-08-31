"""
Example of a Flask app that uses WTForms via the Flask-WTF extension.

Run this app with the following commands
export FLASK_APP=app.py; export FLASK_DEBUG=1; flask run
"""

from flask import Flask, render_template, request
from forms import MyForm

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/')
def home():
    """ Show home page """
    form = MyForm()
    return render_template('home.html', form=form)

@app.route('/results', methods=['POST'])
def results():
    """ Show results page or the error page """
    myform = MyForm(request.form)
    if request.method == 'POST' and myform.validate():
        dub = myform.doubler.data * 2
        return render_template('results.html', form=myform, doubler=dub)
    return render_template('errors.html', form=myform)

