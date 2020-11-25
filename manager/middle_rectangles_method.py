import math

f = lambda x: math.exp(2 * x) * math.sin(3 * x)
F = lambda x: (math.exp(2 * x) * (2 * math.sin(3 * x) - 3 * math.cos(3 * x))) / 13


def middle_rectangles_method(f, a, b):
    n = 30

    Integral = 0
    h = (b - a) / n
    x = a

    for i in range(n):
        Integral += f(x + h / 2)
        x += h
    Integral *= h

    return Integral



