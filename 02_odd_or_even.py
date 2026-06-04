def calculations(num):

    if num % 4 == 0:
        print("The number is even and can be evenly divided by 4")
    elif num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")


def factor_or_not(num, check):

    if num % check == 0:
        print(f"{num} can be evenly divided by {check}")
    else:
        print(f"{num} cannot be evenly divided by {check}")


def main():

    num = input("What number would you like to check?: ")

    while not num.isdigit():
        num = input("What number would you like to check?: ")

    num = float(num)

    check = input("What number would you like to divide by?: ")

    while not check.isdigit():
        check = input("What number would you like to divide by?")

    check = float(check)

    calculations(num)
    factor_or_not(num, check)


if __name__ == "__main__":
    main()
