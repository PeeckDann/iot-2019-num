if __name__ == '__main__':
    from math import sin, pi
    from matplotlib import pyplot as plt

    Umax = 100
    f = 50
    R1, R2, R3, R4 = 5, 4, 7, 2
    L1, L2, L3 = 0.01, 0.02, 0.015
    C1, C2, C3 = 0.0003, 0.00015, 0.0002
    t_int = 0.2
    h = 0.00001
    U1 = lambda t: Umax * sin(2 * pi * f * t)

    F = [
        lambda x, t: ((x[1] + x[2] - x[0]) / R2) / C1,
        lambda x, t: ((U1(t) - x[1] - x[2]) / R1 - (x[1] + x[2] - x[0]) / R2) / C2,
        lambda x, t: ((U1(t) - x[1] - x[2]) / R1 - (x[1] + x[2] - x[0]) / R2 - x[2] / R3) / C3
    ]

    X = [0, 0, 0]
    t = 0
    U2 = []
    times = [h * i for i in range(int(t_int / h))]
    temp_x = [0, 0, 0]
    temp_x_star = [0, 0, 0]
    while t < t_int:
        U2.append(temp_x[2] * R3)
        for i in range(2):
            temp_x = []
            for i in range(len(X)):
                temp_x_star.append(X[i] + h * F[i](X, t))
                temp_x.append(X[i] + 0.5 * h * (F[i](X, t) + F[i](temp_x_star, t + h)))
            for i in range(len(X)):
                X[i] += h * F[i](temp_x, t)
        t += h
    print(X)
    plt.plot(times, U2)
    plt.ylabel('U2')
    plt.xlabel('t')
    plt.show()
