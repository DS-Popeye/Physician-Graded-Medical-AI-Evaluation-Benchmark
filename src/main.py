import json
from pathlib import Path
try:
    from .core import rank_candidates, reviewer_agreement, score_criteria, extract_clues
except ImportError:
    from core import rank_candidates, reviewer_agreement, score_criteria, extract_clues
def main():
    base=Path(__file__).resolve().parents[1]
    case=json.loads((base/'data/synthetic/case_001.json').read_text(encoding='utf-8'))
    note=case['note']
    result={'project':'physician_graded_test_set','case_id':case['case_id'], 'toy_candidate_ranking':rank_candidates(note),
             'clues':sorted(extract_clues(note)), 'disclaimer':'Not medical diagnosis; toy labels only'}
    print(json.dumps(result,indent=2))
if __name__=='__main__': main()
