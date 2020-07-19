class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        print("n %d" % n)
        self.ans = 0
        def traverse(y, target, brd):
            """
            y rows
            target = n
            """
            if y >= n:
                self.ans += 1
                return

            for i in range(target):  # i column
                brd[y][i] = 'Q'

                pass_checks = True

                # check vertical
                for j in range(target):  # j row
                    if j == y:
                        continue
                    if brd[j][i] == 'Q':
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
        
        print("ans: %d" % self.ans)
        print("################\n")
        return self.ans


if __name__ == '__main__':
    s = Solution()

    s.totalNQueens(4)
    s.totalNQueens(5)
    s.totalNQueens(6)
    s.totalNQueens(7)
    s.totalNQueens(8)
    s.totalNQueens(9)
