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
        
        self.column_spaces = [5, 5, 5, 5, 5, 5, 5]
        self.board = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ]
        ]
        self.winning_pattern = []

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
        # check self.column_spaces to see if column is > 0
        column -= 1
        self.column_spaces[column] -= 1
        row_num = self.column_spaces[column]
        self.board[row_num + 1][column] = symbol

    def clear_game(self):
        self.column_spaces = [5] * 7
        self.winning_pattern = []
        for i in range(6):
            for j in range(7):
                self.board[i][j] = ' '

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
            if self.column_spaces[column - 1] < 0:
                print("Column %d is full" % column)
                continue
            else:
                return column

    def check_horizontal(self, symbol, count, y, x, pattern):
        # y is row, x is column
        if x > 6 or y > 5:  # if outside board boundaries
            return False
        if self.board[y][x] != symbol:
            return False
        if count == 3 and self.board[y][x] == symbol:
            self.set_winning_pattern(pattern + [[y, x]])
            return True
        return self.check_horizontal(symbol, count + 1, y, x + 1, pattern + [[y, x]])

    def check_vertical(self, symbol, count, y, x, pattern):
        # y is row, x is column
        if x > 6 or y > 5:  # if outside board boundaries
            return False
        if self.board[y][x] != symbol:
            return False
        if count == 3 and self.board[y][x] == symbol:
            self.set_winning_pattern(pattern + [[y, x]])
            return True
        return self.check_vertical(symbol, count + 1, y - 1, x, pattern + [[y, x]])


    def check_diagonal(self, symbol, count, y, x, direction, pattern):
        if x > 6 or y > 5:  # if outside board boundaries
            return False
        if self.board[y][x] != symbol:
            return False
        if count == 3 and self.board[y][x] == symbol:
            self.set_winning_pattern(pattern + [[y, x]])
            return True
        if direction == 1:
            # diagonal going down
            return self.check_diagonal(symbol, count + 1, y + 1, x + 1, direction, pattern + [[y, x]])
        # diagonal going up
        return self.check_diagonal(symbol, count + 1, y - 1, x + 1, direction, pattern + [[y, x]])

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
                    winner = self.check_horizontal(player.symbol, 0, i, j, []) or \
                             self.check_vertical(player.symbol, 0, i, j, []) or \
                             self.check_diagonal(player.symbol, 0, i, j, 1, []) or \
                             self.check_diagonal(player.symbol, 0, i, j, -1, [])
                if winner is True:
                    break
            if winner is True:
                break
        return winner

    def set_winning_pattern(self, pattern):
        print(pattern)
        for sq in pattern:
            y = sq[0]
            x = sq[1]
            self.board[y][x] = "█"

    def check_stalemate(self):
        for row in self.board:
            for col in row:
                if col == ' ':
                    return False
        return True

    def display_score(self, player1, player2):
        print("\n")
        print(" " * 3 + "Player 1 (%s) score: %d" % (player1.symbol, player1.get_total_wins()))
        print(" " * 3 + "Player 2 (%s) score: %d" % (player2.symbol, player2.get_total_wins()))
        print("\n")


class Player:
    def __init__(self, symbol):
        self.symbol = symbol
        self._win_count = 0  # maybe implement this later

    def increment_win(self):
        self._win_count += 1

    def get_total_wins(self):
        return self._win_count



def game_handler(game, player1, player2):
    turn = -1

    while True:
        current_player = player1 if turn == -1 else player2
        symbol = player1.symbol if turn == -1 else player2.symbol
        
        game.display()
        column_input = game.input_handler(current_player)

        game.add(column_input, symbol)
        winner = game.detect_winner(current_player)
        clear_screen()
        
        if winner is True:
            print("*" * 50)
            print("WINNER %s!" % current_player.symbol)
            print("*" * 50)
            current_player.increment_win()
            game.display_score(player1, player2)
            break
        if game.check_stalemate() is True:
            print("NO WINNER, STALEMATE")
            break
        turn *= -1
    game.display()


if __name__ == '__main__':
    PLAYER_1_SYMBOL = 'X'
    PLAYER_2_SYMBOL = 'O'
    player1 = Player(PLAYER_1_SYMBOL)
    player2 = Player(PLAYER_2_SYMBOL)

    connect_four = ConnectFour()

    while True:
        game_handler(connect_four, player1, player2)

        replay = input("\nReplay round? y/N: ")
        replay = replay.strip()

        if replay.lower() == 'y':
            connect_four.clear_game()
            clear_screen()
            continue
        else:
            break
