def convert(str_number, radix):
    try:
        cunverted_num = int(str_number, radix)
        return cunverted_num
    except:
        return -1
