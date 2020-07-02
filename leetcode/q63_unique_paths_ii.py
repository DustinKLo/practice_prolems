class Solution(object):
    @staticmethod
    def print_tbl(tbl):
        for row in tbl:
            print('\t'.join(str(i) for i in row))

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        print("grid")
        self.print_tbl(obstacleGrid)

        mem = []
        for i in range(len(obstacleGrid)):
            mem.append([float('-inf')] * len(obstacleGrid[i]))

        def traverse(y, x):
            # y rows
            # x columns
            if y > len(obstacleGrid) - 1 or x > len(obstacleGrid[y]) - 1:
                # outside grid
                return 0

            if obstacleGrid[y][x] == 1:
                mem[y][x] = 0
                return 0

            if mem[y][x] > float('-inf'):
                return mem[y][x]

            # reached end
            if y == len(obstacleGrid) - 1 and x == len(obstacleGrid[y]) - 1:
                if obstacleGrid[y][x] == 1:
                    mem[y][x] = 0
                    return 0
                mem[y][x] = 1
                return 1

            right = traverse(y, x + 1)
            down = traverse(y + 1, x)
            
            mem[y][x] = right + down
            return right + down

        traverse(0, 0)
        print("memoization tbl")
        self.print_tbl(mem)
        print("unique paths: %d" % mem[0][0])
        print("##############################\n")
        return mem[0][0]


if __name__ == '__main__':
    s = Solution()

    grid = [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]
    paths = s.uniquePathsWithObstacles(grid)

    grid = [
        [0,0,0,0,0,0],
        [0,1,0,0,1,0],
        [0,0,0,0,0,0]
    ]
    paths = s.uniquePathsWithObstacles(grid)

    grid = [[0,0,0,0]]
    paths = s.uniquePathsWithObstacles(grid)

    grid = [[0,0,1,0]]
    paths = s.uniquePathsWithObstacles(grid)

    grid = [
        [0],
        [0],
        [0],
        [0],
    ]
    paths = s.uniquePathsWithObstacles(grid)

    grid = [
        [0],
        [0],
        [1],
        [0],
    ]
    paths = s.uniquePathsWithObstacles(grid)

    grid = [
        [0,0],
        [1,1],
        [0,0]
    ]
    paths = s.uniquePathsWithObstacles(grid)

    grid = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1],
    ]
    paths = s.uniquePathsWithObstacles(grid)

    grid = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1],
        [0,0,0,0,0,0,0,1,0],
    ]
    paths = s.uniquePathsWithObstacles(grid)

    grid = [
        [0,0,0,0,0,0,0,1],
        [0,0,0,0,0,0,1,0],
        [0,0,0,0,0,1,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0,0],
        [0,0,1,0,0,0,0,0],
        [0,1,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0],
    ]
    paths = s.uniquePathsWithObstacles(grid)
