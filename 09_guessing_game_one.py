import random


def checking(guess, ans, guesses):

    if guess < ans:
        print("Too low...")
        guesses += 1
        return False, guesses

    elif guess > ans:
        print("Too high...")
        guesses += 1
        return False, guesses

    else:
        guesses += 1
        print(f"YOU WON in {guesses} guesses!")
        return True, guesses


def main():

    ans = random.randint(1, 9)
    guesses = 0

    while True:

        guess = input("Your guess (1-9 or 'exit'): ")

        if guess.lower() == "exit":
            print("Goodbye!")
            break

        if not guess.isdigit():
            print("Please enter a number.")
            continue

        guess = int(guess)

        if guess < 1 or guess > 9:
            print(f"{guess} is invalid")
            continue

        won, guesses = checking(guess, ans, guesses)

        if won:
            break


if __name__ == "__main__":
    main()
