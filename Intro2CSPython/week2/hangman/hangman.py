from hangman_helper import *
import sys

if sys.stdout.isatty():
	cWarn = '\033[93m'
	cWin = '\033[92m'
	cBold = '\033[1m'
	cEnd = '\033[0m'
else:
	cWarn, cWin, cBold, cEnd = '', '', '', ''

games_count = 0
points = 0
play = 1


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
	sub = 0, matched//HINT_LENGTH, 2*matched//HINT_LENGTH
	if matched > HINT_LENGTH:
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
	for letter in pattern:
		if letter != '_':
			if letter not in word:
				return False
	pairs = list(zip(pattern, word))
	same = 0
	for i in pairs:
		if i[0] != '_' and i[0] == i[1]:
			same += 1
	us = pattern.count('_')
	return same == (len(pattern) - us)


def run_single_game(list_words, score):
	global games_count
	global points
	global play
	msg = f'{cBold}Welcome to Hangman!{cEnd}'
	points = score
	wrong_guess_lst = []
	word = get_random_word(list_words)
	pattern = '_' * len(word)
	games_count += 1

	print(f'word: {word}')  # Debugging
	while word != pattern and points > 0:
		display_state(pattern, wrong_guess_lst, points, msg)
		msg = ''
		user_input = get_input()
		guess = user_input[1]
		n = 0
		if user_input[0] == LETTER:
			if len(guess) > 1 or guess.isupper() or guess.isdigit() or not guess.isalpha():
				msg = f'{cWarn}Input incorrect.  Please enter a lowercase letter.{cEnd}'
			elif guess in word and guess not in pattern:
				points -= 1
				n = word.count(guess)
			elif guess in wrong_guess_lst or guess in pattern:
				msg = f"{cWarn}'{guess}' already guessed.  Please try again.{cEnd}"
			elif guess not in wrong_guess_lst:
				points -=1
				wrong_guess_lst.append(guess)
		elif user_input[0] == WORD:
			if len(guess) != len(word) or guess.isupper() or guess.isdigit() or not guess.isalpha():
				msg = f'{cWarn}Input incorrect.  Please try again.{cEnd}'
			elif guess == word:
				points -= 1
				n = pattern.count('_')
				pattern = guess
			elif guess != word:
				points -=1
		elif user_input[0] == HINT:
			points -= 1
			words = list_words
			show_suggestions(filter_words_list(words, pattern, wrong_guess_lst))
		points = points + (n*(n+1)//2)
		pattern = update_word_pattern(word, pattern, guess)
	if pattern == word:
		msg = f'{cWin}YOU WIN!{cEnd}'
		display_state(pattern, wrong_guess_lst, points, msg)
		msg = f'You have played {games_count} games and have {points} points'
	if points <= 0:
		games_count = 0
		msg = f'{cBold}You lose!  Your winning streak has ended after {games_count} wins.{cEnd}\nThe word was {word}.'
	play = play_again(msg)


def main():
	list_words = load_words()
	while play:
		score = POINTS_INITIAL if games_count == 0 else points
		run_single_game(list_words, score)


if __name__ == "__main__":
	main()
