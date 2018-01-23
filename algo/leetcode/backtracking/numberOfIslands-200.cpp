#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void mark(vector< vector<char> >& grid, int i, int j) {
        if (grid[i][j] == '1') {
            grid[i][j] == '2';
        }

        if (i > 0 && grid[i-1][j] == '1'){
            mark(grid, i - 1, j);
        }

        if (i < grid.size() - 1 && grid[i+1][j] == '1') {
            mark(grid, i+1, j);
        }

        if (j > 0 && grid[i][j-1] == '1') {
            mark(grid, i, j - 1);
        }

        if (j < grid[0].size() - 1 && grid[i][j+1] == '1') {
            mark(grid, i, j + 1);
        }
    }

    int search(vector< vector<char> >& grid, int i, int j) {
        if (grid[i][j] == '1') {
            mark(grid, i, j);
            return 1;
        }

        return 0;
    }

    int numIslands(vector<vector<char>>& grid) {
        if (grid.size() == 0 || grid[0].size() == 0) {
            return 0;
        }

        int ret = 0;

        for (int i = 0; i < grid.size(); i ++) {
            for (int j = 0; j < grid[0].size(); j ++) {
                ret += search(grid, i, j);
            }
        }

        return ret;
    }
};


int main(int argc, char *argv[])
{
  Solution s;
  char s0[5] = {'1', '1', '1', '1', '0'};
  char s1[5] = {'1', '1', '0', '1', '0'};
  char s2[5] = {'1', '1', '0', '0', '0'};
  char s3[5] = {'0', '0', '0', '0', '0'};


  
  return 0;
}
