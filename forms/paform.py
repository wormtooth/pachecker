from flask_wtf import FlaskForm
from wtforms import BooleanField, SelectField, SubmitField
from wtforms.validators import Required

PAYERS = ['417380', '999001', '417740', '417614']
DRUGS = ['A', 'B', 'C']


class PriorAuthForm(FlaskForm):
    payer = SelectField(
        'Payer',
        description="select the patient's insurance company",
        choices=PAYERS, validators=[Required()]
    )
    drug = SelectField(
        'Drug',
        description="select the drug for the patient",
        choices=DRUGS,
        validators=[Required()]
    )

    correct_diagnosis = BooleanField(
        'correct diagnosis',
        description="check if the patient has the correct diagnosis for the associated drug"
    )
    tried_and_failed = BooleanField(
        'tried and failed',
        description="check if the patient has tried and failed the relevant generic alternatives"
    )
    contraindication = BooleanField(
        'contraindication',
        description="check if the patient has an associated contraindication for the medication requested"
    )

    submit = SubmitField('Check!')
