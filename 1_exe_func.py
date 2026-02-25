import random
import time

def get_user_choice() -> str:
    """
    get choice from user until got a valid choice
    :return:  str - 'rock', 'paper', 'scissors'
    """
    while True:
        get_user_choice: int = int(input('choose (1) = rock (2) paper (3) scissors: '))
        while get_user_choice >= 1 and get_user_choice <= 3:
            if get_user_choice == 1:
                return 'rock 🪨'
            if get_user_choice == 2:
                return 'paper 📄'
            if get_user_choice == 3:
                return 'scissors ✂️'


def get_random_computer_choice() -> str:
    """
    random 1 options from 'rock', 'paper', 'scissors'
    :return:  str - 'rock', 'paper', 'scissors'
    """
    random_computer_number = random.randint(1, 3)
    if random_computer_number == 1:
            return 'rock 🪨'
    if random_computer_number == 2:
        return 'paper 📄'
    if random_computer_number == 3:
        return 'scissors ✂️'


def print_user_choice_icon_and_delay(choice, how_long_sleep) -> None:
    """
    print the user choice + icon and sleep 2-3
    :param choice:  str - 'rock', 'paper', 'scissors'
    :param how_long_sleep:  how long sleep in seconds
    :return: None
    """
    print(user_choice)
    time.sleep(how_long_sleep)


def print_computer_choice_icon(choice) -> None:
    """
    print computer choice + icon
    :param choice:  str - 'rock', 'paper', 'scissors'
    :return:
    """
    print(computer_choice)


def get_game_result(user_choice, computer_choice) -> str:
    """

    :param user_choice:  str - 'rock', 'paper', 'scissors'
    :param computer_choice: str - 'rock', 'paper', 'scissors'
    :return: str winner - 'user', 'draw', 'computer'
    """

    if user_choice == computer_choice:
        return 'draw 🤝'
    if user_choice == 'paper 📄' and computer_choice == 'rock 🪨':
        return 'user wins 💥'
    if user_choice == 'rock 🪨' and computer_choice == 'scissors ✂️':
        return 'user wins 💥'
    if user_choice == 'scissors ✂️' and computer_choice == 'paper 📄':
        return 'user wins 💥'
    else:
        return 'computr wins 💥'

def print_result_and_icon(get_result) -> None:
    """
    👋 💥🤝✅
    Print result with icon
    :param get_result: str winner - 'user', 'draw', 'computer'
    :return: None
    """
    print(get_result)

#
# Icons for each choice
# ICONS = {
#     "rock": "🪨",
#     "paper": "📄",
#     "scissors": "✂️",
# }

print("🎮 Rock–Paper–Scissors")

user_choice = get_user_choice()
print_user_choice_icon_and_delay(user_choice, 3)
computer_choice = get_random_computer_choice()
print_computer_choice_icon(computer_choice)
get_result = get_game_result(user_choice, computer_choice)
print_result_and_icon(get_result)