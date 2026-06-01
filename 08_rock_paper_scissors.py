import random


def compare(computer, player, streak):

    if player == computer:
        print("It's a tie!")

    elif player == "rock" and computer == "scissors":
        print("You won!")
        streak += 1

    elif player == "paper" and computer == "rock":
        print("You won!")
        streak += 1

    elif player == "scissors" and computer == "paper":
        print("You won!")
        streak += 1

    else:
        print("You lost...")
        streak = 0

    return streak


def emoji_appender(choice):

    if choice == "rock":
        return "🪨"

    elif choice == "scissors":
        return "✂️"

    else:
        return "📃"


def main():

    options = ["rock", "paper", "scissors"]
    streak = 0

    while True:

        print()

        computer = random.choice(options)

        player = input("Rock, Paper, or Scissors? (q to quit): ").lower()

        while player not in options and player != "q":
            player = input("Rock, Paper, or Scissors? (q to quit): ").lower()

        if player == "q":
            print(f"Your streak was {streak} 🔥")
            print("Thanks for using my program!")
            break

        computer_emoji = emoji_appender(computer)
        player_emoji = emoji_appender(player)

        print(f"Computer's Choice: {computer} {computer_emoji}")
        print(f"Player's Choice: {player} {player_emoji}")

        streak = compare(computer, player, streak)

        print(f"Current streak: {streak} 🔥")


if __name__ == "__main__":
    main()
