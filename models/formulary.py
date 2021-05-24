import json
import os

import utils
from .tools import flatten_dict, recover_dict


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
        return recover_dict(formulary)

    formulary = {}
    folder = utils.DATA_FOLDER
    df = utils.load_tables(folder)['dim_claims']
    for payer, drug, code in df.groupby(['bin', 'drug', 'reject_code']).size().index:
        if code == 0:
            continue
        formulary[payer, drug] = int(code)

    with open(cache_path, 'w') as f:
        json.dump(flatten_dict(formulary), f)
    return formulary
