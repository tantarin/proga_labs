


def convert_precision(precision=0.01):
    if isinstance(precision, float):
        l = len(str(precision))
        for i in range(1, l+1):
            if precision * 10 ** i >= 1:
                return i