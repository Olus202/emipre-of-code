def golf(number):
    result = 1
    for n in str(number):
        if n != "0":
            result *= int(number)
    return result
