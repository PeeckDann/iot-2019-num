from methods.seidel_method import seidel_method


if __name__ == '__main__':

    a = [[24.53, 2.42, 3.85],
         [2.31, 31.49, 1.52],
         [3.49, 4.84, 29.04]]
    b = [30.24, 40.53, 42.81]

    print("\nResultaty:")
    n = 1
    x = seidel_method(a, b)
    for element in x:
        print(f'x{n} = {element}')
        n += 1

    print("\nPerevirka:\nOchikuvani resultaty - 30.24; 40.53; 42.81")
    r1 = round(24.53 * x[0] + 2.42 * x[1] + 3.85 * x[2], 2)
    r2 = round(2.31 * x[0] + 31.49 * x[1] + 1.52 * x[2], 2)
    r3 = round(3.49 * x[0] + 4.84 * x[1] + 29.04 * x[2], 2)
    print(f'Otrymani resultaty - {r1}; {r2}; {r3}')
