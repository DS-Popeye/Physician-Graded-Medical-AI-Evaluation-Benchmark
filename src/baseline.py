from .core import rank_candidates

def predict(note):
    return rank_candidates(note)[0]["diagnosis"]
