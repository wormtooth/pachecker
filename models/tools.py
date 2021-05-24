import json
import itertools

import pandas
import utils


def flatten_dict(d):
    return [
        {'key': key, 'val': val}
        for key, val in d.items()
    ]


def recover_dict(l):
    return {
        tuple(item['key']): item['val']
        for item in l
    }


def convert_model_to_json(model, path=None):
    df = utils.load_tables(utils.DATA_FOLDER)['dim_claims']
    bin = df.bin.unique().tolist()
    drug = df.drug.unique().tolist()
    data = list(itertools.product(bin, drug, [0, 1], [0, 1], [0, 1]))
    X = pandas.DataFrame(
        data=data,
        columns=['bin', 'drug', 'correct_diagnosis',
                 'tried_and_failed', 'contraindication']
    )
    y = model.predict_proba(X)[:, 1]
    model_dict = {
        feat: prob
        for feat, prob in zip(data, y)
    }

    if path:
        with open(path, 'w') as f:
            json.dump(flatten_dict(model_dict), f)

    return model_dict


def load_model_from_json(json_path):
    with open(json_path, 'r') as f:
        model = recover_dict(json.load(f))
    return model
