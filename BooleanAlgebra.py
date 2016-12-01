PERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")


def boolean(x, y, operation):
    if operation == "conjunction":
        if x == 1 and y == 1:
            return 1
        else:
            return 0
    if operation == "disjunction":
        if x == 0 and y == 0:
            return 0
        else:
            return 1
    if operation == "implication":
        if x == 1 and y == 0:
            return 0
        else:
            return 1
    if operation == "exclusive":
        if (x == 1 and y == 1) or (x == 0 and y == 0):
            return 0
        else: return 1
    if operation == "equivalence":
        if (x == 1 and y == 1) or (x == 0 and y == 0):
            return 1
        else:
            return 0
