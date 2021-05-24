from flask_wtf import FlaskForm
from wtforms import BooleanField, SelectField, SubmitField
from wtforms.validators import Required

PAYERS = ['417380', '999001', '417740', '417614']
DRUGS = ['A', 'B', 'C']


class PriorAuthForm(FlaskForm):
    payer = SelectField('Payer', choices=PAYERS, validators=[Required()])
    drug = SelectField('Drug', choices=DRUGS, validators=[Required()])

    correct_diagnosis = BooleanField('correct diagnosis')
    tried_and_failed = BooleanField('tried and failed')
    contraindication = BooleanField('contraindication')

    submit = SubmitField('Check!')
