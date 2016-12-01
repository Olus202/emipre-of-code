def sure_not(line):
    if "not " not in line[:4]:
        line = "not " + line
    return line
