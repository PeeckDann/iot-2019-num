from methods.newton_method import newton_method, f

if __name__ == '__main__':
    x = newton_method()

    print('\n-------------------------------------------')
    print(f'x = {x}')
    print('-------------------------------------------')
    print(f'f(x) should be 0\nf(x) is {round(f(x))}')
    print('-------------------------------------------')
