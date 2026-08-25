import unittest
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from src.core import extract_clues, rank_candidates, score_criteria, evaluate_predictions, reviewer_agreement

class TestPrototype(unittest.TestCase):
    def test_rank(self):
        self.assertEqual(score_criteria({"clue_alpha"},{"clue_alpha","clue_beta"})["coverage"],0.5)
        self.assertEqual(rank_candidates("clue_alpha clue_beta")[0]["diagnosis"],"synthetic_condition_alpha")
        self.assertEqual(evaluate_predictions(["a"],["a"])["accuracy"],1.0)

if __name__=="__main__": unittest.main()
