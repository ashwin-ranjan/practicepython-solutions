numbers = [42, 7, 89, 13, 56, 42, 91, 3, 77, 24, 65, 18, 99, 50, 12, 73, 8, 36, 56, 1]


def less_checker(numbers, num):

    less_than_5 = [number for number in numbers if number < 5]
    print(f"Less than 5: {sorted(less_than_5)}")

    less_than_num = [number for number in numbers if number < num]
    print(f"Less than {num}: {sorted(less_than_num)}")


def main():

    num = input("Enter a number: ")

    while not num.isdigit():
        num = input("Enter a number: ")

    num = float(num)

    less_checker(numbers, num)


if __name__ == "__main__":
    main()
