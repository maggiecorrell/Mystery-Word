import random

def stripped_list():
    with open('/usr/share/dict/words', 'r') as f:
        for line in f:
            stripped_words.append(line.strip('\n'))
    return stripped_words

def easy_words(stripped_words):
    easy_list = []
    for line in stripped_words:
        if len(line) >= 4 and len(line)<= 6:
            easy_list.append(line)
    return easy_list

def medium_words(stripped_words):
    medium_list = []
    for line in stripped_words:
        if len(line) >= 6 and len(line)<= 8:
            medium_list.append(line)
    return medium_list

def hard_words(stripped_words):
    hard_list = []
    for line in stripped_words:
        if len(line) >= 8:
            hard_list.append(line)
    return hard_list

def choose_level():
    stripped_words = []
    level_choice = input("Pick a level to play at [E]asy, [M]edium, [H]ard: ").lower()
    if level_choice == 'e':
        return easy_words(stripped_words)
    elif level_choice == 'm':
        return medium_words(stripped_words)
    elif level_choice == 'h':
        return hard_words(stripped_words)
    else:
        print("Please enter a vaild level.")

def random_word(choose_level):
    word_to_guess = random.choice(choose_level)
    print("The word you have to guess is {} letters long".format(len(word_to_guess)))
    return word_to_guess

def display_word(word_to_guess, guesses):
    cover_list = []
    for guess in word_to_guess:
        cover_list.append('_')
    for value, guess in enumerate(list(word_to_guess)):
        if guess in guesses:
            cover_list[value] = guess.upper()
    return' '.join(cover_list)


def wrong_guess(word_to_guess, wrong_guesses):
    for guess in word_to_guess:
        if guess not in word_to_guess:
            wrong_guesses.append(letter)
    return wrong_guesses

def is_word_complete(word_to_guess, guesses):
    for letter in word_to_guess:
        if letter not in guesses:
            return False
    return True


def main():
    counter = 8
    wrong_guesses = []
    choose_level()
    while counter >= 0:
        random_word(choose_level)
        guess = input("guess a letter: ").upper()
        print("You have {} number of guesses left".format(counter))
        print("incorrect guesses: {}".format(wrong_guesses))
        if wrong_guess:
            counter -= 1
            print("Guess again")
        elif display_word:
            print(cover_list)
        elif counter == 0:
            print("Out of guesses. You lose")





if __name__ == '__main__':
    main()
