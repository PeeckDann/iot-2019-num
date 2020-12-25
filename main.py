if __name__ == '__main__':
    from matplotlib import pyplot as plt

    def S3(i):
        x1 = Lmin
        x2 = Lmax
        h = x2 - x1
        b1 = (2 * (i - x1) + h) * (x2 - i) ** 2
        b2 = (2 * (x2 - i) + h) * (i - x1) ** 2

        return (b1 * Lmin + b2 * Lmax) / (h ** 3)

    def find_U1(t):
        while t > T:
            t -= T
        if t <= b:
            U1 = t * 10 / b
        elif t <= 3 * a:
            U1 = - (t - b) * 10 / b + 10
        elif t <= 4 * a:
            U1 = - (t - 3 * a) * 10 / a
        elif t <= 5 * a:
            U1 = - 10
        elif t <= 6 * a:
            U1 = (t - 5 * a) * 10 / a - 10

        return U1

    t_int = 1
    a = 0.006
    b = 1.5 * a
    T = 6 * a
    imin, imax = 1, 2
    R1, R2, R3, R4 = 4, 2.3, 570, 110
    C1 = 0.0002
    C2 = 0.004
    Lmin, Lmax = 0.03, 0.3
    L2 = lambda i: Lmax if (abs(i) <= imin) else S3(i) if (imin < abs(i) < imax) else Lmin

    F = [
        lambda x, u: ((u - x[0] + R3 * x[1]) / (R1 + R3)) / C1,
        lambda x, u: (u - R1 * ((u - x[0] + R3 * x[1]) / (R1 + R3)) - x[0] - R2 * x[1] - x[2] - R4 * x[1]) / L2(x[1]),
        lambda x, u: x[1] / C2
    ]

    X = [0, 0, 0]
    t = 0
    h = 0.001
    U2 = []
    UC1 = []
    I2 = []
    UC2 = []
    U = []
    times = [h * i for i in range(int(t_int / h))]
    temp = [0, 0, 0]
    while t <= t_int:
        U2.append(X[1] * R4)
        U.append(find_U1(t))
        UC1.append(X[0])
        I2.append(X[1])
        UC2.append(X[2])
        for i in range(len(X)):
            K1 = h * F[i](X, U[-1])
            K2 = h * F[i]([x + 0.5 * h for x in X], U[-1] + 0.5 * K1)
            K3 = h * F[i]([x + h for x in X], U[-1] + 2 * K2 - K1)
            X[i] = X[i] + (K1 + 4 * K2 + K3) / 6
        t += h
    print(X)
    plt.figure(1)
    plt.plot(times, U2)
    plt.figure(2)
    plt.plot(times, U)
    plt.figure(3)
    plt.plot(times, UC1)
    plt.figure(4)
    plt.plot(times, I2)
    plt.figure(5)
    plt.plot(times, UC2)

    plt.show()
