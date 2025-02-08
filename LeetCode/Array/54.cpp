#include <vector>

using namespace std;

class Solution
{
public:
    vector<int> spiralOrder(vector<vector<int>> &matrix)
    {
        int dr[4] = { 0, 1, 0, -1 };
        int dc[4] = { 1, 0, -1, 0 };

        int m = matrix.size();
        int n = matrix[0].size();

        int r = 0, c = 0, dir = 0;

        vector<int> ans(m * n);
        for (int i = 0; i < m * n; ++i)
        {
            ans[i] = matrix[r][c];
            matrix[r][c] = -101;

            int nr = r + dr[dir];
            int nc = c + dc[dir];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n || matrix[nr][nc] == -101)
            {
                dir = (dir + 1) % 4;
                nr = r + dr[dir];
                nc = c + dc[dir];
            }
            r = nr;
            c = nc;
        }

        return ans;
    }
};