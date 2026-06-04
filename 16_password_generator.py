import random
import string


def generator(security, words):

    # fmt: off

    if security == "weak":
        pw = "".join(random.sample(words, 2))
        
    elif security == "medium":
        chars = random.choices(string.ascii_letters, k=4) + random.choices(string.digits, k=4)
        random.shuffle(chars)
        pw = "".join(chars)
        
    elif security == "strong":
        chars = random.choices(string.ascii_letters, k=4) + random.choices(string.digits, k=4) + random.choices(string.punctuation, k=4)
        random.shuffle(chars)
        pw = "".join(chars)

    return pw

    # fmt: on


def main():

    words = [
        "apple",
        "banana",
        "sunshine",
        "mountain",
        "river",
        "tiger",
        "eagle",
        "ocean",
        "forest",
        "thunder",
        "coffee",
        "guitar",
        "dragon",
        "castle",
        "rocket",
        "penguin",
        "monkey",
        "planet",
        "diamond",
        "shadow",
        "winter",
        "summer",
        "autumn",
        "spring",
        "cloud",
        "storm",
        "lightning",
        "breeze",
        "meadow",
        "valley",
        "panda",
        "dolphin",
        "falcon",
        "rabbit",
        "turtle",
        "saturn",
        "comet",
        "galaxy",
        "meteor",
        "nebula",
    ]

    while True:
        security = input(
            "Weak/Medium/Strong level of password? ('quit' to quit): "
        ).lower()
        while security not in ["weak", "medium", "strong", "quit"]:
            security = input(
                "Weak/Medium/Strong level of password? ('quit' to quit): "
            ).lower()

        if security == "quit":
            print("Thanks for using my program!")
            break

        password = generator(security, words)
        print()
        print("*************************************")
        print(f"Your password is: {password}")
        print("*************************************")
        print()


if __name__ == "__main__":
    main()
