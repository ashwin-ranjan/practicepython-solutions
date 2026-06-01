def palindrome(s):
    return s == s[::-1]


def main():
    s = input("Enter a string to check: ")

    while not s.isalpha():
        s = input("Enter a string to check: ")

    p = palindrome(s)

    if p:
        print(f"{s} is a palindrome")
    else:
        print(f"{s} is not a palindrome")


if __name__ == "__main__":
    main()
