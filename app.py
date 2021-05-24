import os

import numpy as np
import pandas as pd
from flask import Flask, redirect, render_template, url_for

from forms.paform import PriorAuthForm
from models import load_model
from models.formulary import get_formulary

rfc = load_model()
formulary = get_formulary()

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def index():
    return redirect(url_for('pa_form'))


@app.route('/pa_form')
def pa_form():
    return render_template(
        'pa_form.html',
        form=PriorAuthForm(),
        title='Prior Authorization Checker'
    )


@app.route('/pa_result', methods=['POST'])
def pa_result():
    form = PriorAuthForm()

    bin = form.payer.data
    drug = form.drug.data
    correct_diagnosis = int(form.correct_diagnosis.data)
    tried_and_failed = int(form.tried_and_failed.data)
    contraindication = int(form.contraindication.data)
    
    result = rfc[(bin, drug, correct_diagnosis, tried_and_failed, contraindication)]
    result = np.round(result * 100, 2)
    code = formulary.get((form.payer.data, form.drug.data), 0)
    return render_template(
        'pa_result.html',
        title='Prior Authorization Result',
        form=form,
        code=code,
        result=result
    )
