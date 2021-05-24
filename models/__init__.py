import json
import os

MODEL_FOLDER = os.path.dirname(os.path.realpath(__file__))


def recover_dict(l):
    return {
        tuple(item['key']): item['val']
        for item in l
    }


def load_model(model_id='pa_clf_rf'):
    path = os.path.join(MODEL_FOLDER, f'{model_id}.json')
    with open(path, 'r') as f:
        model = recover_dict(json.load(f))
    return model


def get_formulary():
    path = os.path.join(MODEL_FOLDER, 'formulary.json')
    with open(path, 'r') as f:
        formulary = json.load(f)
    return recover_dict(formulary)
