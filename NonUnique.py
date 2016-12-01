def non_unique(data):
    non_unique_elem = []
    for i in data:
        m = data.count(i)
        if type(i) == str:
            if i.upper() in data and i.lower() in data:
                m = 2
        if m != 1:
            non_unique_elem.append(i)
    return non_unique_elem
