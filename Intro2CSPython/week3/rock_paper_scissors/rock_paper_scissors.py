from rock_paper_scissors_helper import *


def play_game():
    """
    Main game function
    :return: keep_playing
    """
    players = 1
    p1_score = 0
    p2_score = 0
    msg = f'{cBold}Rock! Paper! Scissors!{cEnd}'
    intro(msg)
    msg = ''
    players = player_select()
    display_state(msg, p1_score, p2_score)

    while p1_score < 3 and p2_score < 3:
        player_1 = get_input('player_1')
        if players == 1:
            player_2 = computer_choice()
        else:
            player_2 = get_input('player_2')
        winner = check_winner(player_1, player_2)
        if winner == '1':
            p1_score += 1
            msg = f'{cWin}{obj[player_1]} beats {obj[player_2]}! Player 1 Wins!{cEnd}'
        elif winner == '2':
            p2_score += 1
            msg = f'{cWin}{obj[player_2]} beats {obj[player_1]}! Player 2 Wins!{cEnd}'
        else:
            msg = f"{cBold}Both players chose {obj[player_1]}! It's a tie!{cEnd}"
        display_state(msg, p1_score, p2_score)
    msg = f'{cBold}Player {winner} Wins!{cEnd}\nPlay again?'
    keep_playing = 1 if play_again(msg) else 0
    return keep_playing

def main():
    """
    Main function to load play_game function as long as user
    wants to keep playing
    """
    keep_playing = 1
    while keep_playing:
        keep_playing = play_game()


if __name__ == "__main__":
    main()
