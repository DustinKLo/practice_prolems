class Solution(object):
    @staticmethod
    def print_board(board):
        for row in board:
            print(row)
        print("")

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        print("original board")
        self.print_board(board)

        board_height = len(board)
        board_width = 0 if board_height == 0 else len(board[0])

        def traverse(y, x):  # return boolean
            # y row, x column
            if y < 0 or y > board_height - 1:
                return True
            if x < 0 or x > board_width - 1:
                return True

            if (y, x) in visited:
                return True

            if board[y][x] == 'X':
                return True
            visited.add((y, x))  # so we don't revisit coordinate

            if y == 0 or y == board_height - 1:
                return False
            if x == 0 or x == board_width - 1:
                return False

            # traverse left, right, up, down
            return traverse(y, x - 1) and traverse(y, x + 1) and traverse(y + 1, x) and traverse(y - 1, x)

        for i in range(board_width):  # column
            for j in range(board_height):  # row
                if board[j][i] == 'X':
                    continue
                visited = set()
                is_valid = traverse(j, i)
                if is_valid is True:  # take all sets and change to 'X'
                    for _y, _x in visited:
                        board[_y][_x] = 'X'
        
        print("new board")
        self.print_board(board)
        print("#########################################################\n")
        return board


if __name__ == '__main__':
    s = Solution()

    example_board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X'],
    ]
    s.solve(example_board)

    example_board = [
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'X'],
        ['O', 'O', 'O', 'X', 'X', 'O', 'O', 'X', 'X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'X'],
        ['O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O'],
        ['O', 'X', 'O', 'X', 'X', 'O', 'O', 'X', 'X', 'O', 'O', 'O'],
        ['X', 'O', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'O', 'O'],
        ['X', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'O'],
    ]
    s.solve(example_board)

    example_board = [
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'X'],
        ['O', 'O', 'O', 'X', 'X', 'O', 'O', 'X', 'X', 'O', 'O', 'X', 'O', 'O', 'O', 'X', 'X', 'O', 'O', 'X', 'X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'X'],
        ['O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O'],
        ['O', 'X', 'O', 'X', 'X', 'O', 'O', 'X', 'X', 'O', 'O', 'O', 'O', 'X', 'O', 'X', 'X', 'O', 'O', 'X', 'X', 'O', 'O', 'O'],
        ['X', 'O', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'O', 'O', 'X', 'O', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'O', 'O'],
        ['X', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'O'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'X'],
        ['O', 'O', 'O', 'X', 'X', 'O', 'O', 'X', 'X', 'O', 'O', 'X', 'O', 'O', 'O', 'X', 'X', 'O', 'O', 'X', 'X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'X'],
        ['O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O'],
        ['O', 'X', 'O', 'X', 'X', 'O', 'O', 'X', 'X', 'O', 'O', 'O', 'O', 'X', 'O', 'X', 'X', 'O', 'O', 'X', 'X', 'O', 'O', 'O'],
        ['X', 'O', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'O', 'O', 'X', 'O', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'O', 'O'],
        ['X', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'O'],
    ]
    s.solve(example_board)

    example_board = []
    s.solve(example_board)

    example_board = [
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ]
    s.solve(example_board)
