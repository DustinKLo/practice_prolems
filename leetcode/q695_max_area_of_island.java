class Solution {
  int[][] grid;
  
  public int dfs(int y, int x) {
    if(y < 0 || y > this.grid.length - 1) {
      return 0;
    }
    if(x < 0 || x > this.grid[y].length - 1) {
      return 0;
    }
    
    if(this.grid[y][x] == 0) {
      return 0;
    }
    
    grid[y][x] = 0;
    return 1 + dfs(y + 1, x) + dfs(y - 1, x) + dfs(y, x + 1) + dfs(y, x - 1);
  }
  public int maxAreaOfIsland(int[][] grid) {
    this.grid = grid;
    
    int maxArea = 0;
    for(int j = 0; j < grid.length; j++) {
      for(int i = 0; i < grid[j].length; i++) {
        if (grid[j][i] == 0) {
          continue;
        }
        int curArea = dfs(j, i);
        maxArea = Math.max(curArea, maxArea);
      }
    }
    return maxArea;
  }
}
