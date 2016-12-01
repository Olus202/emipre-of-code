import string


def count_ingots(report):
    alpha = string.ascii_uppercase
    ingots = []
    for letter in alpha:
        for dig in range(1, 10):
            ingots.append(letter + str(dig))
    report_parts = report.split(",")
    result = 0
    for r in report_parts:
        result += (ingots.index(r) + 1)
    return result

