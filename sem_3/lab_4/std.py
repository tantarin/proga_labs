from math import *


def std(*args):
    xV = 0
    n = 0
    Sigma = 0.0
    for x in args:
        xV += x
        n += 1
    xV = xV / n
    for x in args:
        Sigma += (x - xV) ** 2
    res = sqrt(Sigma / n)
    return res