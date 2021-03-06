import time
from player import HumanPlayer, RandomComputerPlayer
class TicTacToe():
    def __init__(self):
        self.board = [' ' for _ in range(9)] # We will use single list to represent 3x3 board
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3: (i+1)*3] for i in range(3)]:
            print('| ' + '|'.join(row) + ' |')
    
    @staticmethod
    def print_board_nums():
        # 0 | 1| 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range (j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + '|'.join(row) + ' |')
    
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     if spot == ' ':
        #         moves.append(i)
        # return moves

    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = True
            return True
        return False

    def winner (self, square, letter):
        # winner if 3 in a row anywhere. we have to check all of these!
        # first lets check the row
        row_ind = square // 3
        row = self.board[row_ind * 3 : (row_ind+1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # Check column
        col_ind = square % 3
        column = [self.board[col_ind + i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # Check diagnols
        # but only if the square is even number (0, 2, 4, 6, 8)
        # these are the only possible moves to win a diagonal
        if square % 2 == 0:

            diagnoal1 = [self.board[i] for i in [0, 4, 8]] # left to right diagonal
            if all([spot == letter for spot in diagnoal1]):
                return True

            diagnoal2 = [self.board[i] for i in [2, 4, 6]] # right to left diagonal
            if all([spot == letter for spot in diagnoal2]):
                return True

        return False



def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_board_nums()
    
    letter = 'X'
    
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        if game.make_move(square, letter):
            if print_game:
                print (letter + f' makes a move to square {square}')
                game.print_board()
            
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            # after we made our move, we need to alternate letters
            letter = 'O' if letter =='X' else 'X'
        
        # tiny break to make things little easier to read
        time.sleep(0.8)
    
    if print_game:
        print('It\'s a tie!')

if __name__ == '__main__':
    print('play')
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)

