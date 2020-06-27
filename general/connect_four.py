import sys
import os


IS_WINDOWS = sys.platform.startswith('win')

def clear_screen():
    if IS_WINDOWS:
        os.system('cls')
    else:
        os.system('clear')


class ConnectFour:
    def __init__(self):
        # will decrement whenever player puts piece down
        # if index is 0, cannot add to that column anymore
        self.buffer = 3
        self.buffer_space = ' ' * self.buffer
        
        self.index_tracker = [5, 5, 5, 5, 5, 5, 5]
        self.board = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ]
        ]

    def display(self):
        print("\n")
        numbers_display =  self.buffer_space + '  1   2   3   4   5   6   7'
        print(numbers_display)
        print(self.buffer_space + '-' * 29)
        for row in self.board:
            displayed_row = ' | '.join(col for col in row)
            print(self.buffer_space + '| ' + displayed_row + ' | ')
            print(self.buffer_space + '-' * 29)
        print("\n")

    def add(self, column, symbol):
        # check self.index_tracker to see if column is > 0
        column -= 1
        self.index_tracker[column] -= 1
        row_num = self.index_tracker[column]
        self.board[row_num + 1][column] = symbol

    def input_handler(self, player):
        """
        Handles the player input for their turn
        """
        while True:
            column = input("\nEnter column number Player %s: " % player.symbol)
            try:
                column = int(column)
            except (ValueError, Exception) as e:
                print("Input numbers please")
                continue

            if column < 1 or column  > 7:
                print("choose between column 1 and 7")
                continue
            if self.index_tracker[column - 1] < 0:
                print("Column %d is full" % column)
                continue
            else:
                return column

    def check_horizontal(self, symbol, count, y, x):
        # y is row, x is column
        if x > 6 or y > 5:  # if outside board boundaries
            return False
        if self.board[y][x] != symbol:
            return False
        if count == 3 and self.board[y][x] == symbol:
            return True
        return self.check_horizontal(symbol, count + 1, y, x + 1)

    def check_vertical(self, symbol, count, y, x):
        # y is row, x is column
        if x > 6 or y > 5:  # if outside board boundaries
            return False
        if self.board[y][x] != symbol:
            return False
        if count == 3 and self.board[y][x] == symbol:
            return True
        return self.check_vertical(symbol, count + 1, y - 1, x)


    def check_diagonal(self, symbol, count, y, x, direction):
        if x > 6 or y > 5:  # if outside board boundaries
            return False
        if self.board[y][x] != symbol:
            return False
        if count == 3 and self.board[y][x] == symbol:
            return True
        if direction == 1:
            # diagonal going down
            return self.check_diagonal(symbol, count + 1, y + 1, x + 1, direction)
        # diagonal going up
        return self.check_diagonal(symbol, count + 1, y - 1, x + 1, direction)

    def detect_winner(self, player):
        """
        detect winner
        use DFS and detect vertical, horizontal and diaganol
        """
        winner = False
        for i in range(5, 0, -1):  # rows, starting from bottom up
            for j in range(7):  # columns
                if self.board[i][j] == ' ':
                    continue
                else:
                    winner = self.check_horizontal(player.symbol, 0, i, j) or \
                             self.check_vertical(player.symbol, 0, i, j) or \
                             self.check_diagonal(player.symbol, 0, i, j, 1) or \
                             self.check_diagonal(player.symbol, 0, i, j, -1)
                if winner is True:
                    break
            if winner is True:
                break
        return winner

    def check_stalemate(self):
        for row in self.board:
            for col in row:
                if col == ' ':
                    return False
        return True


class Player:
    def __init__(self, symbol):
        self.symbol = symbol
        self._win_count = 0  # maybe implement this later

    def increment_win(self):
        self._win_count += 1

    def get_total_wins(self):
        return self._win_count


if __name__ == '__main__':
    PLAYER_1_SYMBOL = 'X'
    PLAYER_2_SYMBOL = 'O'
    
    player1 = Player(PLAYER_1_SYMBOL)
    player2 = Player(PLAYER_2_SYMBOL)
    
    game = ConnectFour()
    turn = -1

    while True:
        current_player = player1 if turn == -1 else player2
        symbol = PLAYER_1_SYMBOL if turn == -1 else PLAYER_2_SYMBOL
        
        game.display()
        column_input = game.input_handler(current_player)

        game.add(column_input, symbol)
        winner = game.detect_winner(current_player)
        clear_screen()
        
        if winner is True:
            print("*" * 50)
            print("WINNER %s!" % current_player.symbol)
            print("*" * 50)
            break
        if game.check_stalemate() is True:
            print("NO WINNER, STALEMATE")
            break
        turn *= -1
    
    game.display()
