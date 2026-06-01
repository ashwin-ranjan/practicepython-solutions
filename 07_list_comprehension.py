import random


def even_only(a):
    return [b for b in sorted(a) if b % 2 == 0]


def main():
    a = random.sample(range(100), random.randint(0, 101))
    print(even_only(a))


if __name__ == "__main__":
    main()
