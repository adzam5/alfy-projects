from hangman_helper import *
import sys

if sys.stdout.isatty():
    cWarn = '\033[93m'
    cWin = '\033[92m'
    cBold = '\033[1m'
    cEnd = '\033[0m'
else:
    cWarn, cWin, cBold, cEnd = '', '', '', ''

games_count = 1

def update_word_pattern(word, pattern, letter):
    for i in range(len(word)):
        if word[i] == letter:
            pattern = pattern[:i] + letter + pattern[i+1:]
    return pattern


def filter_words_list(words, pattern, wrong_guess_lst):
    matches = []
    for word in words:
        if len(word) == len(pattern):
            if wrong_check(word, wrong_guess_lst) and pattern_check(pattern, word):
                matches.append(word)
    matched = len(matches)
    if matched > HINT_LENGTH:
        sub = [0, matched//HINT_LENGTH, 2*matched//HINT_LENGTH, (HINT_LENGTH - 1)*matched//HINT_LENGTH]
        sub_matches = []
        for i in sub:
            sub_matches.append(matches[i])
        return sub_matches
    else:
        return matches


def wrong_check(word, wrong_guess_lst):
    for letter in word:
        if letter in wrong_guess_lst:
            return False
    return True


def pattern_check(pattern, word):
    matches = 0
    for pos, letter in enumerate(word):
        if letter == pattern[pos]:
            matches += 1
            if word.count(letter) != pattern.count(letter):
                return False
    return True if matches == len(word) - pattern.count('_') else False


def run_single_game(list_words, score):
    global games_count
    msg = f'{cBold}Welcome to Hangman!{cEnd}'
    wrong_guess_lst = []
    word = get_random_word(list_words)
    pattern = '_' * len(word)

    # print(f'word: {word}')  # Debugging
    while word != pattern and score > 0:
        display_state(pattern, wrong_guess_lst, score, msg)
        msg = ''
        user_input = get_input()
        guess = user_input[1]
        n = 0
        if user_input[0] == LETTER:
            if len(guess) > 1 or guess.isupper() or guess.isdigit() or not guess.isalpha():
                msg = f'{cWarn}Input incorrect.  Please enter a lowercase letter.{cEnd}'
            elif guess in word and guess not in pattern:
                score -= 1
                n = word.count(guess)
            elif guess in wrong_guess_lst or guess in pattern:
                msg = f"{cWarn}'{guess}' already guessed.  Please try again.{cEnd}"
            elif guess not in wrong_guess_lst:
                score -=1
                wrong_guess_lst.append(guess)
        elif user_input[0] == WORD:
            if len(guess) != len(word) or guess.isupper() or guess.isdigit() or not guess.isalpha():
                msg = f'{cWarn}Input incorrect.  Please try again.{cEnd}'
            elif guess == word:
                score -= 1
                n = pattern.count('_')
                pattern = guess
            elif guess != word:
                score -=1
        elif user_input[0] == HINT:
            score -= 1
            words = list_words
            show_suggestions(filter_words_list(words, pattern, wrong_guess_lst))
        score = score + (n*(n+1)//2)
        pattern = update_word_pattern(word, pattern, guess)
    if pattern == word:
        s = 's' if games_count > 1 else ''
        msg = f'{cWin}YOU WIN!{cEnd}'
        pa_msg = f'You have played {games_count} game{s} and have {score} points. Play again?'
    else:
        msg = f'The word was: {word}'
        pa_msg = f'{cBold}You lose!  You won {games_count -1} out of {games_count} games.  Play again?{cEnd}'
    display_state(pattern, wrong_guess_lst, score, msg)
    games_count += 1
    return score, pa_msg


def main():
    global games_count
    list_words = load_words()
    score = POINTS_INITIAL
    score, msg = run_single_game(list_words, score)

    while play_again(msg):
        if score <= 0:
            score = POINTS_INITIAL
            games_count = 1
        score, msg = run_single_game(list_words, score)


if __name__ == "__main__":
    main()
