def seidel_method(a, b):
    p = [0, 0, 0]
    y = [0, 0, 0]
    x = [0, 0, 0]
    v = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

    for i in range(0, 3):
        p[i] = b[i]/a[i][i]
        x[i] = y[i] = b[i]
        for j in range(0, 3):
            if i != j:
                v[i][j] = -(a[i][j]/a[i][i])
            else:
                v[i][j] = 0

    while True:
        for i in range(0, 3):
            s = 0
            for j in range(0, 3):
                s += v[i][j] * x[j]
            x[i] = p[i] + s
        for k in range(0, 3):
            e = (((x[k] - y[k]) / x[k]) * 100)
            if -0.1 < e < 0.1:
                return x
        y[k] = x[k]

