"""
Example of submitting web form data using Flask.
"""

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    """home page"""
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    """results page"""
    vehicle = request.form.get('vehicle')
    year = request.form.get('year')
    return render_template('result.html', vehicle=vehicle, year=year)

