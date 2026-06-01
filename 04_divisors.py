def main():

    number = input("Enter a number: ")

    while not number.isdigit():
        number = input("Enter a number: ")

    number = int(number)

    find_factors(number)


def find_factors(number):

    divisors = list(range(1, number + 1))

    for x in divisors:
        if number % x == 0:
            print(x, end="  ")


if __name__ == "__main__":
    main()
