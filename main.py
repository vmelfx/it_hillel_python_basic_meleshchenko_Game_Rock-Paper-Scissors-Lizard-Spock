import random

user_choice = None
random_program_choice = None
user_win_message = "You win!"
computer_win_message = "Computer wins!"
draw_message = "It's a draw!"


def rules():
    print("HERE ARE THE RULES OF THE GAME: \n"
          "Scissors cuts paper, paper covers rock, rock crushes lizard,\n"
          "lizard poisons Spock, Spock smashes scissors,"
          "scissors decapitates lizard,\nlizard eats paper,"
          "paper disproves Spock, Spock vaporizes rock,\n"
          "and as it always has, rock crushes scissors.\n\n")


def user_input():
    while True:
        print("Please, make your choice: rock, paper, scissors, lizard or Spock? To interrupt the game enter ")
        global user_choice
        user_choice = input("Your choice: ").lower()
        if user_choice in ["rock", "paper", "scissors", "lizard", "spock"]:
            return user_choice
        else:
            print("Please make correct input.")


def program_choice():
    choices_list = ["rock", "paper", "scissors", "lizard", "spock"]
    global random_program_choice
    random_program_choice = random.choice(choices_list)
    print(f"Computer: {random_program_choice}")


def winner_detector():
    rock_list = ["paper", "spock", "rock", "scissors", "lizard"]
    paper_list = ["scissors", "lizard", "paper", "spock", "rock"]
    scissors_list = ["rock", "spock", "scissors", "paper", "lizard"]
    lizard_list = ["rock", "scissors", "lizard", "paper", "spock"]
    spock_list = ["paper", "lizard", "spock", "rock", "scissors"]

    def sorter(element_list):
        index = 0
        for element in element_list:
            if element == random_program_choice:
                if index == 0 or index == 1:
                    return computer_win_message
                elif index == 2:
                    return draw_message
                else:
                    return user_win_message
            index += 1

    if user_choice == "rock":
        print(sorter(rock_list))
    elif user_choice == "paper":
        print(sorter(paper_list))
    elif user_choice == "scissors":
        print(sorter(scissors_list))
    elif user_choice == "lizard":
        print(sorter(lizard_list))
    elif user_choice == "spock":
        print(sorter(spock_list))


def main():
    while True:
        rules()
        user_input()
        program_choice()
        winner_detector()
        play_again = input("Play again? (Y/N)").lower()
        if play_again == "y":
            continue
        else:
            break


if __name__ == '__main__':
    main()