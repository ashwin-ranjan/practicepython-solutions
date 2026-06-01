import random


def main():

    num_list = random.sample(range(1, 30), 12)
    print(num_list)

    first = num_list[0]
    last = num_list[-1]

    print(f"First: {first} and Last: {last}")


if __name__ == "__main__":
    main()
