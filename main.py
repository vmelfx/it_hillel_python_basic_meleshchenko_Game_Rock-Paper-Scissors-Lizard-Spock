import random

user_choice = None
random_program_choice = None
user_win_message: str = "You win!"
computer_win_message: str = "Computer wins!"
draw_message: str = "It's a draw!"


def rules():
    """
    This function is responsible for printing rules of the game
    """
    print("HERE ARE THE RULES OF THE GAME: \n"
          "Scissors cuts paper, paper covers rock, rock crushes lizard,\n"
          "lizard poisons Spock, Spock smashes scissors,"
          "scissors decapitates lizard,\nlizard eats paper,"
          "paper disproves Spock, Spock vaporizes rock,\n"
          "and as it always has, rock crushes scissors.\n\n")


def user_input():
    """
    This function is responsible for user input.
    Input is not case-sensitive.
    While loop is used to keep the program
    from executing until the user makes the correct input. Also, it is used to give user
    an opportunity to exit from the game
    """
    while True:
        global user_choice
        print("Please, make your choice: rock, paper, scissors, lizard or Spock? To interrupt the game enter 'exit'")
        user_choice: str = input("Your choice: ").lower()
        if user_choice in ["rock", "paper", "scissors", "lizard", "spock"]:
            return user_choice
        elif user_choice == "exit":
            raise SystemExit
        else:
            print(f'Invalid input "{user_choice}"')


def program_choice():
    """
    This function is responsible for computer choices in the game
    """
    global random_program_choice
    choices_list: list = ["rock", "paper", "scissors", "lizard", "Spock"]
    random_program_choice: str = random.choice(choices_list)
    print(f"Computer: {random_program_choice}")


def winner_detector():
    """
    This function detects who has won.
    Here we have five lists with all possible choices.
    In each list, the first two values are losing for the selected element,
    the third element leads to a draw, and the last two elements are winning
    for the selected element.
    Example: in rock_list first two elements are losing for rock("paper" and "spock"),
    third element leads to a draw("rock") and the last two elements are winning for rock
    ("scissors" and "lizard")
    Depending on user_choice value we run choice_analyzer with the same name as user choice.
    Example: If user_choice is "rock" we run choice_analyzer with rock_list.
    """
    rock_list: list = ["paper", "Spock", "rock", "scissors", "lizard"]
    paper_list: list = ["scissors", "lizard", "paper", "Spock", "rock"]
    scissors_list: list = ["rock", "Spock", "scissors", "paper", "lizard"]
    lizard_list: list = ["rock", "scissors", "lizard", "paper", "Spock"]
    spock_list: list = ["paper", "lizard", "Spock", "rock", "scissors"]

    def choice_analyzer(element_list):
        """
        This function returns the winner.
        It is a simple loop with a counter.
        In for loop, we iterate over the passed list until the element in the list is equal
        to random_program_choice.
        Then, function looks at index value and depending on it returns winner
        Example: user_choice = "spock" and random_program_choice = "scissors",
        so from winner_detector function we've got spock_list. As mentioned before,
        the first two values are losing for "spock",
        the third element leads to a draw, and the last two elements are winning
        for "spock".
        Loop will continue until it encounters "scissors" in the list and because it is the
        last element in the list its index is 4, so user wins.
        """
        index: int = 0
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
        print(choice_analyzer(rock_list))
    elif user_choice == "paper":
        print(choice_analyzer(paper_list))
    elif user_choice == "scissors":
        print(choice_analyzer(scissors_list))
    elif user_choice == "lizard":
        print(choice_analyzer(lizard_list))
    elif user_choice == "spock":
        print(choice_analyzer(spock_list))


def menu():
    """
    This function asks user if he wants to play again.
    Input is not case-sensitive.
    Depending on user input it runs the game again or exits from the program
    If user enters something else instead of "y" or "n" function prints Invalid input and
    restarts itself.
    """
    play_again: str = input("Play again? (Y/N)").lower()
    if play_again == "y":
        return True
    elif play_again == "n":
        raise SystemExit
    else:
        print(f'Invalid input "{play_again}"')
        menu()


def main():
    while True:
        rules()
        user_input()
        program_choice()
        winner_detector()
        menu()


if __name__ == '__main__':
    main()
