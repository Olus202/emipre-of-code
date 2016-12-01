def count_units(number):
    bin_number = bin(number)
    units = bin_number.count("1")
    return units
