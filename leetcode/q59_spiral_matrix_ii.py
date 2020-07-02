class Solution(object):
    @staticmethod
    def print_matrix(matrix):
        for row in matrix:
            row = '\t'.join(str(n) for n in row).expandtabs(5)
            print(row)

    def generateMatrix(self, n):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if n == 0:
            return []

        direction_mapper = {
            'right': 'down',
            'down': 'left',
            'left': 'up',
            'up': 'right'
        }

        matrix = [[0] * n for i in range(n)]
        
        ans = []
        l = 0  # left
        r = len(matrix[0])
        u = 0  # up
        d = len(matrix)

        num = 1
        direction = 'right'  # starting direction
        while l < r and u < d:
            if direction == 'right':
                # read right, will read down after
                for i in range(l, r):
                    matrix[u][i] = num
                    num += 1
                u += 1
                direction = direction_mapper['right']

            elif direction == 'down':
                # read down, will read left after
                for i in range(u, d):
                    matrix[i][r-1] = num
                    num += 1
                r -= 1
                direction = direction_mapper['down']

            elif direction == 'left':
                # read left, will read up
                # need to read backwards from right bound to left bound
                for i in range(r - 1, l - 1, -1):
                    matrix[d-1][i] = num
                    num += 1
                d -= 1
                direction = direction_mapper['left']

            else:
                # read up, will read right after
                # need to read backwards from bottom bound to top
                for i in range(d - 1, u - 1, -1):
                    matrix[i][l] = num
                    num += 1
                direction = direction_mapper['up']
                l += 1

        print("n: %d" % n)
        self.print_matrix(matrix)
        print("")
        return matrix


if __name__ == '__main__':
    s = Solution()
    s.generateMatrix(1)
    s.generateMatrix(2)
    s.generateMatrix(3)
    s.generateMatrix(4)
    s.generateMatrix(5)
    s.generateMatrix(6)
    s.generateMatrix(10)
    s.generateMatrix(20)
