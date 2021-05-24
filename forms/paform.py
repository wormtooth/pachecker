import utils
from flask_wtf import FlaskForm
from wtforms import BooleanField, SelectField, SubmitField
from wtforms.validators import Required

df = utils.load_tables(utils.DATA_FOLDER)['full']
PAYERS = df.bin.unique().tolist()
DRUGS = df.drug.unique().tolist()


class PriorAuthForm(FlaskForm):
    payer = SelectField('Payer', choices=PAYERS, validators=[Required()])
    drug = SelectField('Drug', choices=DRUGS, validators=[Required()])

    correct_diagnosis = BooleanField('correct diagnosis')
    tried_and_failed = BooleanField('tried and failed')
    contraindication = BooleanField('contraindication')

    submit = SubmitField('Check!')
