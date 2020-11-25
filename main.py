from manager.secant_method import secant_method, count


if __name__ == '__main__':
    result = secant_method()

    # Results
    print(result)

    # Check
    print(count(result[0], result[1]))
