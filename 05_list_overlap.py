import random


def find_overlap(a, b):

    overlaps = [num for num in a if num in b]
    return overlaps


def main():

    a = random.sample(range(50), random.randint(0, 101))
    b = random.sample(range(50), random.randint(0, 101))
    print(find_overlap(a, b))


if __name__ == "__main__":
    main()
