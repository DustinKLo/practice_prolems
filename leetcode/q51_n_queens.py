import copy

class Solution(object):
    @staticmethod
    def print_brd(brd):
        for row in brd:
            print(row)

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        print("n: %d" % n)
        self.ans = []
        def traverse(y, target, brd):
            """
            y rows
            target = n
            """
            if y >= n:
                ans_board = copy.deepcopy(brd)
                for i in range(target):
                    ans_board[i] = ''.join(ans_board[i])
                self.ans.append(ans_board)
                return

            for i in range(target):  # i column
                brd[y][i] = 'Q'

                pass_checks = True

                # check vertical
                q_count = 0
                for j in range(target):  # j row
                    if brd[j][i] == 'Q':
                        q_count += 1
                        if q_count > 1:
                            pass_checks = False
                            break

                if pass_checks == True:
                    # check diag down, slope down right from point
                    k = y + 1 # vertical
                    j = i + 1 # horizontal
                    while j < target and k < target:
                        if brd[k][j] == 'Q':
                            pass_checks = False
                            break
                        k += 1
                        j += 1
                
                if pass_checks == True:
                    # check diag down, slope up left from point
                    k = y - 1 # vertical
                    j = i - 1 # horizontal
                    while j > -1 and k > -1:
                        if brd[k][j] == 'Q':
                            pass_checks = False
                            break
                        k -= 1
                        j -= 1

                if pass_checks == True:
                    # check diag up slope up right from point
                    k = y - 1  # vertical
                    j = i + 1  # horizontal
                    while j < target and k > -1:
                        if brd[k][j] == 'Q':
                            pass_checks = False
                            break
                        k -= 1
                        j += 1
                
                if pass_checks == True:
                    # check diag up slope down left from point
                    k = y + 1  # vertical
                    j = i - 1  # horizontal
                    while j > -1 and k < target:
                        if brd[k][j] == 'Q':
                            pass_checks = False
                            break
                        k += 1
                        j -= 1

                if pass_checks is False:  # empty out space
                    brd[y][i] = '.'
                else:  # traverse further
                    traverse(y + 1, target, brd)

                brd[y][i] = '.'  # resetting spot as we traverse back up

        board = [['.'] * n for i in range(n)]
        traverse(0, n, board)
        for brd in self.ans:
            self.print_brd(brd)
            print("")
        print("############################")
        return self.ans


if __name__ == '__main__':
    s = Solution()

    s.solveNQueens(4)
    s.solveNQueens(5)
    s.solveNQueens(6)
