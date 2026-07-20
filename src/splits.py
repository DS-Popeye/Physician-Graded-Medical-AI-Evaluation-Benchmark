def split_ids(ids):
    ids=sorted(ids)
    a=int(len(ids)*0.7); b=int(len(ids)*0.85)
    return {"train":ids[:a], "validation":ids[a:b], "test":ids[b:]}
