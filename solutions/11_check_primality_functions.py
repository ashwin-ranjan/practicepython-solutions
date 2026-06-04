from sympy import isprime


def main():

    num = input("Enter a number: ")

    while not num.isdigit():
        num = input("Enter a number: ")

    result = isprime(num)


if __name__ == "__main__":
    main()
