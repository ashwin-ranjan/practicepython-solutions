def fib_generator(counter):

    fib = []
    a, b = 0, 1

    for x in range(counter):
        fib.append(a)
        a, b = b, a + b

    return fib


def main():

    counter = int(input("How many?: "))
    fib = fib_generator(counter)
    print(fib)


if __name__ == "__main__":
    main()
