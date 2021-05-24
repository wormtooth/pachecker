import os
import pickle

import utils
from sklearn.base import clone
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

from .tools import load_model_from_json, convert_model_to_json

MODEL_FOLDER = os.path.dirname(os.path.realpath(__file__))

PA_RFC = Pipeline([
    ('preprocess', utils.DataFrameFeatures(
        num_cols=['correct_diagnosis', 'tried_and_failed', 'contraindication'],
        cat_cols=['bin', 'drug']
    )),
    ('rfc', RandomForestClassifier(
        max_depth=8, min_samples_split=9
    ))
])

MODELS = {
    'pa_clf_rf': {
        'name': 'Random Forest',
        'model': PA_RFC,
        'group': 'pa'
    }
}


def load_model(model_id='pa_clf_rf'):
    config = MODELS[model_id]
    path = os.path.join(MODEL_FOLDER, f'{model_id}.json')
    if os.path.exists(path):
        return load_model_from_json(path)

    X, y = _load_data(config)
    model = clone(config['model']).fit(X, y)
    model = convert_model_to_json(model, path)

    return model


def _load_data(config):
    folder = utils.DATA_FOLDER
    if config['group'] == 'pa':
        df = utils.load_tables(folder)['filed_pa']
        y = df.pa_approved.to_numpy()
        return df, y
