def most_difference(*args):
    elements = []
    for arg in args:
        elements.append(arg)
    
    if len(elements) == 0:
        return 0
    else:
        minimum = min(elements)
        maximum = max(elements)
        difference = maximum - minimum
        return difference
