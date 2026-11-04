def summarize(scores):
    return {"count": len(scores), "mean": sum(scores)/len(scores) if scores else None}
