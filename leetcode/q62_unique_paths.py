class Solution(object):
    @staticmethod
    def print_mem(tbl):
        for row in tbl:
            print('\t'.join(str(i) for i in row))

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return min(m, n)
        # m rows
        # n columns
        mem = [[float('-inf')] * n for i in range(m)]

        def traverse(y, x):
            # y rows
            # x columns
            if y > m - 1 or x > n - 1:
                return 0

            if y == m - 1 and x == n - 1:
                return 1

            if mem[y][x] > float('-inf'):
                return mem[y][x]

            down  = traverse(y + 1, x)  # down
            right = traverse(y, x + 1)  # right

            mem[y][x] = down + right
            return down + right

        traverse(0, 0)
        self.print_mem(mem)
        print("unique paths: %d" % mem[0][0])
        print("")
        return mem[0][0]


if __name__ == '__main__':
    s = Solution()

    s.uniquePaths(3, 2)
    s.uniquePaths(7, 3)

