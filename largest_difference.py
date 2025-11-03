def largest_difference(param):
    param.sort()
    size = len(param)
    value = param[size-1] - param[0]
    return value