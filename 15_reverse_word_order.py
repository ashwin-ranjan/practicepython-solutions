def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])


def main():
    sentence = input("Enter a sentence: ")
    reversed_sentence = reverse_words(sentence)
    print(f"Reversed sentence: {reversed_sentence}")


if __name__ == "__main__":
    main()
