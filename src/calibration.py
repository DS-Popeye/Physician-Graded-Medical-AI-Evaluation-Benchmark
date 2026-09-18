def brier_score(probs, labels):
    if len(probs)!=len(labels): raise ValueError("Length mismatch")
    return sum((p-y)**2 for p,y in zip(probs,labels))/len(probs) if probs else None
