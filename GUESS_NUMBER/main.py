import random

def guess(x):
    random_number =  random.randint(1, x)

    guess = 0

    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print ("Sorry, guess again. Too high")
    
    print(f'Yay, congrats. you\'ve guesses the number {random_number} correctly')

def computer_guess(x):
    low = 1
    high = x
    feed_back= ''
    guess_attempts = 0
    while feed_back != 'c':
        if low != high:
            guess_attempts += 1
            guess = random.randint(low, high)
        else:
            guess = low
        feed_back = input(f'is {guess} too high (H), too low (L), correct (C) '.lower())
        if feed_back == 'h':
            high = guess - 1
        elif feed_back == 'l':
            low = guess + 1
    print(f'Yay! The computer guessed your number {guess} correctly in {guess_attempts} attemts' )

# guess(10)
computer_guess(1000)
    