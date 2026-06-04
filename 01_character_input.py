name = ""
age = ""


def age_calculation(age):

    when_age_hundred = (2026 - age) + 100
    return when_age_hundred


def how_many_times(number, when_age_hundred):

    for _ in range(number):
        print(f"You will be hundred years old in {when_age_hundred}")


def main():

    name = input("What is your first name?: ")

    while not name.isalpha():
        name = input("What is your first name?: ")

    age = input("What is your age?: ")

    while not age.isdigit() or int(age) <= 0:
        age = input("What is your age?: ")

    age = int(age)

    number = int(input("How many times should I print the message?: "))

    when_age_hundred = age_calculation(age)

    how_many_times(number, when_age_hundred)


if __name__ == "__main__":
    main()
