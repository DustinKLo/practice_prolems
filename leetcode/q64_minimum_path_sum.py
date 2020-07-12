from pprint import pprint
# USING DIJKSTRA'S SHORTEST PATH ALGORITHM

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # build DIJKSTRA table (or a dictionary in this case)
        """
        (y, x) | smallest_sum | last_pt
        -------------------------------
        (0, 0) | 0            | (0, 0)
        (0, 1) | inf          | (0, 0)
        .
        .
        .
        """
        if len(grid) == 0:
            return 0

        mem = {}
        for j in range(len(grid)):  # row
            for i in range(len(grid[j])):  # column
                mem[j, i] = {
                    'smallest_sum': float('inf'),
                    'prev': None,
                }
        mem[0, 0] = {'smallest_sum': grid[0][0], 'prev': None}

        # loop through each value in grid
        #   within each grid calculate the sum path of the right and bottom coord
        #   check against table to see if sum is less than cached value
        for j in range(len(grid)):  # row
            for i in range(len(grid[j])):  # column
                # check right
                if i + 1 <= len(grid[j]) - 1:
                    cur_sum = mem[j, i]['smallest_sum'] + grid[j][i + 1]
                    if cur_sum < mem[j, i + 1]['smallest_sum']:
                        mem[j, i + 1]['smallest_sum'] = cur_sum
                        mem[j, i + 1]['prev'] = (j, i)

                # check bottom
                if j + 1 <= len(grid) - 1:
                    cur_sum = mem[j, i]['smallest_sum'] + grid[j + 1][i]
                    if cur_sum < mem[j + 1, i]['smallest_sum']:
                        mem[j + 1, i]['smallest_sum'] = cur_sum
                        mem[j + 1, i]['prev'] = (j, i)

        max_y = len(grid) - 1
        max_x = len(grid[max_y]) - 1

        # printing the shortest path
        pt = (max_y, max_x)
        pts = [pt]
        vals = [grid[max_y][max_x]]
        while True:
            pt = mem[pt]['prev']
            if pt is None:
                break
            pts.insert(0, pt)
        
        path_sum = [grid[_y][_x] for _y, _x in pts]
        print(' + '.join(str(i) for i in path_sum))
        print("########################\n")
        return mem[max_y, max_x]['smallest_sum']


if __name__ == '__main__':
    s = Solution()
    
    matrix = [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
    s.minPathSum(matrix)

    matrix = [
        [7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],
        [9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],
        [8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],
        [6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],
        [7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],
        [9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],
        [1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],
        [3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],
        [1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],
        [5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],
        [2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],
        [0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]
    ]
    s.minPathSum(matrix)

    matrix = [
        [1,2,3,4,5,6,7]
    ]
    s.minPathSum(matrix)

    matrix = [
        [1],
        [2],
        [3],
        [4],
        [5],
        [6],
        [7],
    ]
    s.minPathSum(matrix)

    matrix = [[0]]
    s.minPathSum(matrix)

    matrix = []
    s.minPathSum(matrix)
