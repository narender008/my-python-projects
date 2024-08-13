import random


def main(user_r, computer_r):
    result = {
        (1, 1): "It's a tie!",
        (1, 2): "Computer wins!",
        (1, 3): "User wins!",
        (2, 1): "User wins!",
        (2, 2): "It's a tie!",
        (2, 3): "Computer wins!",
        (3, 1): "Computer wins!",
        (3, 2): "User wins!",
        (3, 3): "It's a tie!",
    }
    value = result.get((user_r, computer_r), "Invalid input")
    print(value)


if __name__ == "__main__":
    while True:
        user_response = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: "))
        computer_response = random.randint(1, 3)
        main(user_response, computer_response)
        print("You want to play again? (y/n)")
        if input().lower() != "y":
            break
