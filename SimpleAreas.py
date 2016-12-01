import math


def simple_areas(*args):
    args_num = len(args)
    if args_num == 1:
        area = math.pi * args[0]/2 * args[0]/2
        return round(area, 2)
    elif args_num == 2:
        area = args[0] * args[1]
        return round(area, 2)
    elif args_num == 3:
        p = (args[0] + args[1] + args[2]) / 2
        area = math.sqrt(p * (p - args[0]) * (p - args[1]) * (p - args[2]))
        return round(area, 2)
    return 0
