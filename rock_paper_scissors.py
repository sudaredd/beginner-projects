import random

def play():
    user = input("what's your choice? 'r' for rock, 'p' for paper, 's' for scissors:")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return 'It\'s tie'
    elif is_win(user, computer):
        return 'You won!'
    else:
        return 'You lost!'

# r>s, s>p, p>r
def is_win(player, opponent):
    #return true if player wins
    return (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r')

print(play())