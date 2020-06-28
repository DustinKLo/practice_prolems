class Solution(object):
    def __init__(self):
        self.visited = set()

    def traverse(self, y, x, island_num):
        # y rows, x columns
        if y > self.map_height - 1 or y < 0:  # if outside map
            return 
        if x > self.map_width - 1 or x < 0:
            return

        print(y, x, island_num)
        if (y, x,) not in self.visited:
            self.visited.add((y, x,))
        else:  # if we already visited coordinate
            return

        if self.map[y][x] == '0':  # will not traverse if water
            return
        
        self.traverse(y - 1, x, island_num)  # up 
        self.traverse(y + 1, x, island_num)  # down
        self.traverse(y, x - 1, island_num)  # left
        self.traverse(y, x + 1, island_num)  # right
        

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            print("final island count:", 0)
            print("###########################\n")
            return 0

        self.visited = set()
        self.map = grid
        self.map_width = len(grid[0])
        self.map_height = len(grid)

        island_num = 0
        for i in range(self.map_height):
            for j in range(self.map_width):
                if (i, j,) in self.visited:
                    continue
                if grid[i][j] == '1':
                    island_num += 1
                self.traverse(i, j, island_num)
        
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
