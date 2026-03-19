#include <vector>
#include <unordered_map> // Must include this!

using namespace std; // This allows you to skip writing 'std::' every time

class Solution {
public:
    int numberOfSubmatrices(vector<vector<char>>& grid) {
        if (grid.empty() || grid[0].empty()) return 0;

        int rows = grid.size();
        int cols = grid[0].size();

        unordered_map<char, int> mapping = {{'X', 1}, {'Y', -1}, {'.', 0}};

        // Build up the fast lookup
        vector<vector<int>> countX(rows, vector<int>(cols, 0));
        vector<vector<int>> diff(rows, vector<int>(cols, 0));
        int valid = 0;

        for(int i = 0; i < rows; i++) {
            for(int j = 0; j < cols; j++) {
                int above = (i > 0) ? diff[i-1][j] : 0;
                int left = (j > 0) ? diff[i][j-1] : 0;
                int above_left = (i > 0) && (j > 0) ? diff[i-1][j-1] : 0;

                int above_x = (i > 0) ? countX[i-1][j] : 0;
                int left_x = (j > 0) ? countX[i][j-1] : 0;
                int above_left_x = (i > 0) && (j > 0) ? countX[i-1][j-1] : 0;

                diff[i][j] = above + left - above_left + mapping[grid[i][j]];
                countX[i][j] = above_x + left_x - above_left_x + (grid[i][j] == 'X' ? 1 : 0);

                if (countX[i][j] > 0 && diff[i][j] == 0) {
                    valid++;
                }
            }
        }
        return valid;
    }
};