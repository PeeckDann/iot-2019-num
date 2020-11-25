import math


def count(x1, x2):
    # Calculation of functions from system of equations
    f = [0, 0]
    f[0] = x1 ** 2 - x2 ** 2 - 0.1 - x1
    f[1] = 2 * x1 * x2 - 0.1 - x2
    return f


def secant_method():
    # Secant method variables
    E = [[0, 0],
         [0, 0]]
    h = [0, 0]
    x = [0.1, 0.1]
    x_old = [0.1, 0.1]
    x_older = [0.5, 0.5]
    J = [[0, 0],
         [0, 0]]
    x_tilda = [0, 0]

    # Gauss method variables
    V = [[0, 0],
         [0, 0]]
    P = [0, 0]
    in_x = [0, 0]
    C = [[0, 0],
         [0, 0]]
    Y = [0, 0]
    X = [0, 0]
    INVERS = [[0, 0],
              [0, 0]]

    # Accuracy variable
    e = 0.00001

    # Initialization of unit matrix
    for i in range(0, 2):
        for j in range(0, 2):
            if i == j:
                E[i][j] = 1
            else:
                E[i][j] = 0

    # Main iteration
    while True:

        # Step vector calculation
        for i in range(0, 2):
            h[i] = x_older[i] - x_old[i]

        # Function vector calculation
        f = count(x[0], x[1])

        # Jacobi matrix calculation
        for i in range(0, 2):
            for j in range(0, 2):
                for k in range(0, 2):
                    x_tilda[k] = x[k]
                x_tilda[j] = x[j] + h[j]
                f_tilda = count(x_tilda[0], x_tilda[1])
                J[i][j] = (f_tilda[i] - f[i]) / h[j]

        # Gauss method (by main elements of all matrix)
        for b in range(0, 2):

            # Direct course
            for i in range(0, 2):
                in_x[i] = i
            for i in range(0, 2):
                for j in range(0, 2):
                    V[i][j] = J[i][j]
                    P[i] = E[i][b]
            for k in range(0, 2):

                # Matrix sorting
                max = math.fabs(V[k][k])
                h_requiem = k
                w = k
                for l in range(0, 2):
                    for f_requiem in range(0, 2):
                        if max < math.fabs(V[l][f_requiem]):
                            max = math.fabs(V[l][f_requiem])
                            h_requiem = l
                            w = f_requiem
                value = P[k]
                P[k] = P[h_requiem]
                P[h_requiem] = value
                for d in range(0, 2):
                    value = V[k][d]
                    V[k][d] = V[h_requiem][d]
                    V[h_requiem][d] = value
                z = in_x[k]
                in_x[k] = in_x[w]
                in_x[w] = z
                for d in range(0, 2):
                    if d < k:
                        value = C[d][k]
                        C[d][k] = C[d][w]
                        C[d][w] = value
                    else:
                        value = V[d][k]
                        V[d][k] = V[d][w]
                        V[d][w] = value

                # Direct course (continuation)
                Y[k] = P[k] / V[k][k]
                for i in range(k + 1, 2):
                    P[i] = P[i] - V[i][k] * Y[k]
                    for j in range(k + 1, 2):
                        C[k][j] = V[k][j] / V[k][k]
                        V[i][j] = V[i][j] - V[i][k] * C[k][j]

            # Reverse course
            for n in range(0, 2):
                X[n] = Y[n]
            for i in range(1, -1, -1):
                s = 0
                for j in range(i + 1, 2):
                    s += C[i][j] * X[j]
                X[i] = Y[i] - s

            # Ordering x(i)
            for i in range(0, 2):
                if in_x[i] != i:
                    z = in_x[i]
                    value = X[i]
                    X[i] = X[z]
                    X[z] = value
                    in_x[i] = in_x[z]
                    in_x[z] = z
            for i in range(0, 2):
                INVERS[i][b] = X[i]

        # Calculation of the next approximation of x
        for i in range(0, 2):
            s2 = 0
            for j in range(0, 2):
                s2 += INVERS[i][j] * f[j]
            x[i] = x_old[i] - s2

        # Convergence condition
        for i in range(0, 2):
            check = math.fabs((x[i] - x_old[i]) / x[i]) * 100
            x_older[i] = x_old[i]
            x_old[i] = x[i]
            if check < e:
                return x
