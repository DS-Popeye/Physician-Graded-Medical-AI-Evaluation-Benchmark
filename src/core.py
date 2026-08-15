import re
from collections import Counter

# Illustrative toy criteria only; NOT formal medical diagnostic criteria.
TOY_RULES = {
    'synthetic_condition_alpha': {'clue_alpha', 'clue_beta'},
    'synthetic_condition_beta': {'clue_gamma', 'clue_delta'},
    'synthetic_condition_gamma': {'clue_epsilon', 'clue_zeta'},
}
def extract_clues(text):
    return set(re.findall(r'\bclue_(?:alpha|beta|gamma|delta|epsilon|zeta)\b', text.lower()))
def score_criteria(clues, required):
    required = set(required)
    if not required: return {'coverage': 0.0, 'matched': [], 'missing': []}
    return {'coverage': len(clues & required) / len(required),
            'matched': sorted(clues & required), 'missing': sorted(required - clues)}
def rank_candidates(note):
    clues = extract_clues(note)
    return sorted([{'diagnosis': d, **score_criteria(clues, req)} for d,req in TOY_RULES.items()],
                  key=lambda x: (-x['coverage'], x['diagnosis']))
def evaluate_predictions(gold, predicted):
    if len(gold) != len(predicted): raise ValueError('Length mismatch')
    n=len(gold)
    return {'n': n, 'accuracy': sum(a==b for a,b in zip(gold,predicted))/n if n else 0.0}
def reviewer_agreement(ratings):
    # Simple exact agreement, not Cohen's kappa.
    pairs=[r for r in ratings if len(r)>=2]
    return {'n':len(pairs), 'exact_agreement':sum(len(set(r))==1 for r in pairs)/len(pairs) if pairs else 0.0}
