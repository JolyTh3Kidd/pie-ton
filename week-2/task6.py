def all_eq(lst):
    max_len = 0
    for s in lst:
        if len(s) > max_len:
            max_len = len(s)
    result = []
    for s in lst:
        if len(s) < max_len:
            s = s + "_" * (max_len - len(s))
        result.append(s)
    return result
