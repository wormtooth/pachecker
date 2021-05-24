import json
import os

import utils


def _flatten(formulary):
    return [
        {'key': key, 'val': val}
        for key, val in formulary.items()
    ]


def _recover(formulary):
    return {
        tuple(item['key']): item['val']
        for item in formulary
    }


def get_formulary():

    cache_path = os.path.join(utils.APP_FOLDER, 'models', 'formulary.json')
    formulary = None
    if os.path.exists(cache_path):
        try:
            with open(cache_path, 'r') as f:
                formulary = json.load(f)
        except Exception:
            pass

    if formulary:
        return _recover(formulary)

    formulary = {}
    folder = utils.DATA_FOLDER
    df = utils.load_tables(folder)['dim_claims']
    for payer, drug, code in df.groupby(['bin', 'drug', 'reject_code']).size().index:
        if code == 0:
            continue
        formulary[payer, drug] = int(code)

    with open(cache_path, 'w') as f:
        json.dump(_flatten(formulary), f)
    return formulary
