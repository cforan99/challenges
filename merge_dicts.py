def merge_dicts(lld):
    """Takes a list of lists that contain dictionaries (lld) and returns a list with all the dictionaries in their relative order.
    >>> lists=[[{'a': 1, 1: 'a'}, {2: 'b', 'b': 2}, {'c': 3, 3: 'c'}], [{4: 'd', 'd': 4}, {'e': 5, 5: 'e'}], [{6: 'f', 'f': 6}, {'g': 7, 7: 'g'}, {8: 'h', 'h': 8}, {'i': 9, 9: 'i'}]]
    >>> merge_dicts(lists)
    [{'a': 1, 1: 'a'}, {4: 'd', 'd': 4}, {6: 'f', 'f': 6}, {2: 'b', 'b': 2}, {'e': 5, 5: 'e'}, {'g': 7, 7: 'g'}, {'c': 3, 3: 'c'}, {8: 'h', 'h': 8}, {'i': 9, 9: 'i'}]
    """
    final = []
    prev_len = len(final)
    curr_len = -1
    while curr_len != prev_len:
        prev_len = curr_len
        for lst in lld:
            if len(lst) != 0:
                dict = lst.pop(0)
                final.append(dict)
        curr_len = len(final)
    return final