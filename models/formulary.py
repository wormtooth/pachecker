import utils

FORMULARY = None


def get_formulary():
    global FORMULARY
    if FORMULARY:
        return FORMULARY
    FORMULARY = {}
    folder = utils.DATA_FOLDER
    df = utils.load_tables(folder)['dim_claims']
    for payer, drug, code in df.groupby(['bin', 'drug', 'reject_code']).size().index:
        if code == 0:
            continue
        FORMULARY[payer, drug] = int(code)
    return FORMULARY
