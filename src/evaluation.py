from .core import evaluate_predictions

def accuracy(gold, predictions):
    return evaluate_predictions(gold, predictions)["accuracy"]
