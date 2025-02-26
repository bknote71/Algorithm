#include <queue>
#include <vector>

using namespace std;

class Solution
{
public:
    int shortestPathBinaryMatrix(vector<vector<int>> &grid)
    {
        int n = grid.size();
        if (grid[0][0] != 0 || grid[n - 1][n - 1] != 0)
            return -1;

        vector<vector<bool>> vst(n, vector<bool>(n, false));

        queue<pair<pair<int, int>, int>> q;
        q.push({ { 0, 0 }, 1 });
        vst[0][0] = true;

        int answer = 1;

        int dr[8] = { 0, -1, -1, -1, 0, 1, 1, 1 };
        int dc[8] = { 1, 1, 0, -1, -1, -1, 0, 1 };

        while (q.empty() == false)
        {
            int r = q.front().first.first;
            int c = q.front().first.second;
            int dist = q.front().second;

            q.pop();

            if (r == n - 1 && c == n - 1)
                return dist;

            for (int d = 0; d < 8; ++d)
            {
                int nr = r + dr[d];
                int nc = c + dc[d];
                if (nr < 0 || nr >= n || nc < 0 || nc >= n || vst[nr][nc] || grid[nr][nc] != 0)
                    continue;

                vst[nr][nc] = true;
                q.push({ { nr, nc }, dist + 1 });
            }
        }

        return -1;
    }
};