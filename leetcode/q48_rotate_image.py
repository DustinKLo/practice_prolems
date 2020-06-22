class Solution(object):
    @staticmethod
    def print_matrix(matrix):
        for row in matrix:
            print('\t'.join(str(r) for r in row))
        print("")

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        self.print_matrix(matrix)

        left = 0
        right = len(matrix[0]) - 1
        depth = 0

        while left < right:
            for i in range(left, right):
                tmp1 = matrix[depth][i]
                tmp2 = matrix[i][right]
                tmp3 = matrix[right][right - i + depth]
                tmp4 = matrix[right - i + depth][depth]

                print(i, left, right, depth)
                # print(tmp1, tmp2, tmp3, tmp4)

                matrix[i][right] = tmp1
                matrix[right][right - i + depth] = tmp2
                matrix[right - i + depth][depth] = tmp3
                matrix[depth][i] = tmp4
            print("")
            left += 1
            right -= 1
            depth += 1

        self.print_matrix(matrix)
        return matrix


if __name__ == '__main__':
    s = Solution()

    matrix = [
        [ 0, 1, 2, 3, 4],
        [ 5, 6, 7, 8, 9],
        [10,11,12,13,14],
        [15,16,17,18,19],
        [20,21,22,23,24],
    ]
    s.rotate(matrix)