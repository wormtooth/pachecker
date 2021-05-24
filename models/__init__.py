import os
import pickle

import utils
from sklearn.base import clone
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

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
                'filename': 'pa_clf_rf.pkl',
                'group': 'pa'
    }
}


def load_model(model_id='pa_clf_rf'):
    config = MODELS[model_id]
    path = os.path.join(MODEL_FOLDER, config['filename'])
    if os.path.exists(path):
        with open(path, 'rb') as f:
            model = pickle.load(f)
        return model

    X, y = _load_data(config)
    model = clone(config['model']).fit(X, y)
    with open(path, 'wb') as f:
        pickle.dump(model, f)
    return model


def _load_data(config):
    folder = utils.DATA_FOLDER
    if config['group'] == 'pa':
        df = utils.load_tables(folder)['filed_pa']
        y = df.pa_approved.to_numpy()
        return df, y
