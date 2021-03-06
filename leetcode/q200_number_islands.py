class Solution(object):
    @staticmethod
    def print_map(grid):
        for row in grid:
            # print(row)
            formatted_row = '\t'.join(row).expandtabs(5)
            print(formatted_row)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = [[0] * len(row) for row in grid]

        def traverse(y, x):
            # y rows, x columns
            if y > len(grid) - 1 or y < 0:  # if outside map
                return
            if x > len(grid[y]) - 1 or x < 0:
                return

            if grid[y][x] == '0':  # will not traverse if water
                return

            if visited[y][x] == 1:  # if we already visited coordinate
                return

            visited[y][x] = 1
            self.coordinates.add((y, x))

            traverse(y - 1, x)  # up
            traverse(y + 1, x)  # down
            traverse(y, x - 1)  # left
            traverse(y, x + 1)  # right

        island_num = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if visited[i][j] == 1:
                    continue
                if grid[i][j] == '1':
                    island_num += 1
                self.coordinates = set()
                traverse(i, j)

                for _y, _x in self.coordinates:
                    grid[_y][_x] = str(island_num)

        self.print_map(grid)
        print("final island count:", island_num)
        print("###########################\n")
        return island_num


if __name__ == '__main__':
    s = Solution()

    ex_map = [
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
    ]
    s.numIslands(ex_map)

    ex_map = [
         ['1', '1', '0', '0', '0'],
         ['1', '1', '0', '0', '0'],
         ['0', '0', '1', '0', '0'],
         ['0', '0', '0', '1', '1'],
    ]
    s.numIslands(ex_map)

    ex_map = [
         ['1', '1', '0', '0', '1'],
    ]
    s.numIslands(ex_map)

    ex_map = [
         ['1'],
         ['0'],
         ['1'],
         ['0'],
         ['1'],
    ]
    s.numIslands(ex_map)

    ex_map = []
    s.numIslands(ex_map)

    ex_map = [
         ['1', '1', '1', '1', '0', '1', '1', '1', '1', '0', '1', '1', '1', '1', '0', '1', '1', '1', '1', '0'],
         ['1', '1', '0', '1', '0', '1', '1', '0', '1', '0', '1', '1', '0', '1', '0', '1', '1', '0', '1', '0'],
         ['1', '1', '0', '0', '0', '1', '1', '0', '0', '0', '1', '1', '0', '0', '0', '1', '1', '0', '0', '0'],
         ['0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
         ['1', '1', '0', '1', '0', '1', '1', '1', '1', '0', '1', '1', '0', '1', '0', '1', '1', '1', '1', '0'],
         ['1', '1', '0', '1', '0', '1', '1', '0', '0', '0', '1', '1', '0', '1', '0', '1', '1', '0', '0', '0'],
         ['1', '1', '0', '0', '0', '1', '1', '0', '0', '0', '1', '1', '0', '0', '0', '1', '1', '0', '0', '0'],
         ['0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0'],
         ['1', '1', '1', '1', '0', '1', '1', '1', '1', '0', '1', '1', '1', '1', '0', '1', '1', '1', '1', '0'],
         ['1', '1', '0', '1', '0', '1', '1', '0', '1', '0', '1', '1', '0', '1', '0', '1', '1', '0', '1', '0'],
         ['1', '1', '0', '0', '0', '1', '1', '0', '0', '0', '1', '1', '0', '0', '0', '1', '1', '0', '0', '0'],
         ['0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
         ['1', '1', '0', '1', '0', '1', '1', '1', '1', '0', '1', '1', '0', '1', '0', '1', '1', '1', '1', '0'],
         ['1', '1', '0', '1', '0', '1', '1', '0', '0', '0', '1', '1', '0', '1', '0', '1', '1', '0', '0', '0'],
         ['1', '1', '0', '0', '0', '1', '1', '0', '0', '0', '1', '1', '0', '0', '0', '1', '1', '0', '0', '0'],
         ['0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0'],
    ]
    s.numIslands(ex_map)
