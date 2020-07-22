#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
  int minPathSum(vector<vector<int>> &grid)
  {
    int r = grid.size();
    int c = grid[0].size();

    // adding up the sums of first column
    for (int i = 1; i < grid.size(); i++)
      grid[i][0] = grid[i][0] + grid[i - 1][0];

    // adding up the sum of first row
    for (int i = 1; i < grid[0].size(); i++)
      grid[0][i] = grid[0][i] + grid[0][i - 1];

    for (int j = 1; j < grid.size(); j++)
      for (int i = 1; i < grid[j].size(); i++)
        grid[j][i] = min(grid[j][i] + grid[j - 1][i], grid[j][i] + grid[j][i - 1]);

    cout << grid[r - 1][c - 1] << "\n";
    return grid[r - 1][c - 1];
  }
};

int main()
{
  Solution s = Solution();

  vector<int> r1 = {1, 3, 1};
  vector<int> r2 = {1, 5, 1};
  vector<int> r3 = {4, 2, 1};

  vector<vector<int>> test = {r1, r2, r3};
  s.minPathSum(test);
  return 0;
}
