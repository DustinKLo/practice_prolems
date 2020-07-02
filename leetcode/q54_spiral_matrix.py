class Solution(object):
    @staticmethod
    def print_matrix(matrix):
        for row in matrix:
            print(row)

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []

        direction_mapper = {
            'right': 'down',
            'down': 'left',
            'left': 'up',
            'up': 'right'
        }

        print("matrix")
        self.print_matrix(matrix)
        
        ans = []
        l = 0  # left
        r = len(matrix[0])
        u = 0  # up
        d = len(matrix)

        ans = []
        direction = 'right'  # starting direction
        while l < r and u < d:
            if direction == 'right':
                # read right, will read down after
                for i in range(l, r):
                    ans.append(matrix[u][i])
                u += 1
                direction = direction_mapper['right']

            elif direction == 'down':
                # read down, will read left after
                for i in range(u, d):
                    ans.append(matrix[i][r-1])
                r -= 1
                direction = direction_mapper['down']

            elif direction == 'left':
                # read left, will read up
                # need to read backwards from right bound to left bound
                for i in range(r - 1, l - 1, -1):
                    ans.append(matrix[d-1][i])
                d -= 1
                direction = direction_mapper['left']

            else:
                # read up, will read right after
                # need to read backwards from bottom bound to top
                for i in range(d - 1, u - 1, -1):
                    ans.append(matrix[i][l])
                direction = direction_mapper['up']
                l += 1
        print("spiral order:")
        print(ans)
        print("")
        return ans


if __name__ == '__main__':
    s = Solution()
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12]
    ]
    s.spiralOrder(matrix)

    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [10,11,12]
    ]
    s.spiralOrder(matrix)

    matrix = [
        [1],
        [2],
        [3],
        [4]
    ]
    s.spiralOrder(matrix)

    matrix = [[1,2,3,4,5]]
    s.spiralOrder(matrix)
