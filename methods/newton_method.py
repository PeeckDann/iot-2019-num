def f(x):
    return x ** 3 + 3 * (x ** 2) + 1


def df(x):
    return 3 * x ** 2 + 6 * x


def ddf(x):
    return 6*x + 6


def find_first_step():
    x = -4
    while x < -2.25:
        if ddf(x) * f(x) > 0:
            return x
        else:
            x += 0.01


def newton_method():
    x = find_first_step()
    e = 0.000000000001

    while True:
        x_old = x
        x = x - (f(x) / df(x))
        check = ((x - x_old)/x)
        if -e < check * 100 < e:
            return x
