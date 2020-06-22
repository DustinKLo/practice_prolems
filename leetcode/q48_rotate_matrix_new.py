class Solution(object):
    @staticmethod
    def print_matrix(matrix):
        for row in matrix:
            print('\t'.join(str(r) for r in row))
            print("")
        print("")

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        print("old: ")
        self.print_matrix(matrix)

        # transpose matrix
        for i in range(0, len(matrix) - 1):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                # tmp = matrix[i][j]
                # matrix[i][j] = matrix[j][i]
                # matrix[j][i] = tmp

        # flip vertically
        for row in matrix:
            i = 0
            j = len(row) - 1
            while i < j:
                row[i], row[j] = row[j], row[i]
                # tmp = row[i]
                # row[i] = row[j]
                # row[j] = tmp
                i += 1
                j -= 1

        print("rotated: ")
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
    matrix = [
        [0,1,2,3],
        [4,5,6,7],
        [8,9,10,11],
        [12,13,14,15]
    ]
    s.rotate(matrix)
