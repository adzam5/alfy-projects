import random
import time
import sys

# variables to add some color when playing on tty
if sys.stdout.isatty():
    cWarn = '\033[93m'
    cWin = '\033[92m'
    cScor = '\033[95m'
    cBold = '\033[1m'
    cEnd = '\033[0m'
else:
    cWarn, cWin, cBold, cEnd = '', '', '', ''

# dictionary to translate user input abbriviations to words for messages
obj = {
    'r': 'Rock',
    'p': 'Paper',
    's': 'Scissors'
}


def intro(msg):
    """
    Displays inital message with time delay between words
    :param msg: message to be displayed
    """
    msg = msg.split()
    for i in msg:
        print(i, end=' ', flush=True)
        time.sleep(0.5)
    print('')


def player_select():
    """
    Allows users to select number of players
    and checks for incorrect input
    :return: selcted number of players
    """
    user_input = ''
    valid_input = ['1', '2']
    while True:
        user_input = input('Enter number of players (1 or 2): ')
        if user_input in valid_input:
            break
        else:
            print(f'{cWarn}Invalid option!{cEnd}')
    return int(user_input)


def get_input(player):
    """
    Receives user input during game play and checks
    for incorrect input
    :param player: which player input is from
    :return: user_input
    """
    valid_input = ['r', 'p', 's']
    player = 'Player 1: ' if player == 'player_1' else 'Player 2: '
    while True:
        user_input = input(f"{cBold}{player}{cEnd}Please enter 'r' for Rock, 'p' for Paper, or 's' for Scissors:\n")
        if user_input == '!':
            msg = f'Are you sure you want to quit?'
            quit = play_again(msg)
            if quit:
                exit()
        elif user_input in valid_input:
            return user_input
        else:
            print(f'{cWarn}Invalid option!{cEnd}')


def computer_choice():
    """
    Selects a random choice from predefined list if player 2 is computer
    :return: random choice
    """
    choices = ['r', 'p', 's']
    return random.choice(choices)


def check_winner(player_1, player_2):
    """
    compares player 1 user input to player 2 user input
    against list of possible winning scenarios to
    see who won the round
    :param player_1: player 1 user input
    :param player_2: player 2 user input
    :return: 1 or 2 if player 1 or player 2 won, tie if both users had same input
    """
    check = player_1, player_2
    wins = [('r', 's'), ('p', 'r'), ('s', 'p')]

    if check in wins:
        return '1'
    elif check[::-1] in wins:
        return '2'
    else:
        return 'tie'


def display_state(msg, p1_score, p2_score):
    """
    Displays custom message and current score
    :param msg: custom message for current round
    :param p1_score: player 1 score
    :param p2_score: player 2 score
    """
    print(msg)
    print(f'{cScor}Player 1: {p1_score} | Player 2: {p2_score}{cEnd}')


def play_again(msg):
    """
    Accepts user input to continue playing
    :param msg: custom message
    :return: True if user wants to keep playing, otherwise False
    """
    print(msg)
    while True:
        choice = input("Enter 'y' for Yes, 'n' for No: ")
        if choice and choice == 'y':
            return True
        if choice and choice == 'n':
            return False

