#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

class Solution
{
public:
  int minPathSum(vector<vector<int>> &grid)
  {
    int r = grid.size();
    int c = grid[0].size();

    double **mem = new double *[r];
    for (int j = 0; j < r; j++)
    {
      mem[j] = new double[c];
      for (int i = 0; i < c; i++)
        mem[j][i] = INFINITY;
    }
    mem[0][0] = 0;

    double cur;
    int ans;
    for (int j = 0; j < r; j++)
    {
      for (int i = 0; i < c; i++)
      {
        // down
        if (j < r - 1)
        {
          cur = mem[j][i] + grid[j + 1][i];
          if (cur < mem[j + 1][i])
            mem[j + 1][i] = cur;
        }

        // right
        if (i < c - 1)
        {
          cur = mem[j][i] + grid[j][i + 1];
          if (cur < mem[j][i + 1])
            mem[j][i + 1] = cur;
        }
      }
    }
    ans = (int)mem[r - 1][c - 1] + grid[0][0];

    for (int j = 0; j < r; j++)
      delete[] mem[j];

    cout << ans << endl;
    return ans;
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
