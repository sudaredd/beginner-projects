import random
import string

from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set (string.ascii_letters)
    used_letters = set() # what the user has guessed
    
    lives = 6
    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'gh']) -> 'a b gh'
        print('You have', lives, ' lives left  and you have used these letters', ' '.join(used_letters))
        # What current word is (ie W- R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('letter is not found')
        elif user_letter in used_letters:
            print(f'You have already used this letter {user_letter} , please try again')
        else:
            print(f'invalid letter {user_letter}, please try again')
    
    if lives > 0:
        print(f'Yay! Congrats, you have guessed word {word} correctly')
    else:
        print(f'You died, sorry, the word was {word} ')

hangman()