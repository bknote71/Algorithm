#include <iostream>
#include <queue>
#include <vector>

using namespace std;

/**
 * 핵심 포인트
 * - '빈' 칸은 이동할 수 있다.
 * - 그렇다면 빈 칸이 아닌 (slash) '/', '\' 에 대한 표현을 어떻게 할 것인가?
 */

class Solution
{
public:
    vector<vector<bool>> vst;
    int n;
    int newSize;

    int regionsBySlashes(vector<string> &grid)
    {
        n = grid.size();
        newSize = 3 * n;
        vst.resize(newSize, vector<bool>(newSize, false));

        vector<vector<char>> vec(newSize, vector<char>(newSize, ' '));

        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                char ch = grid[i][j];
                int r = 3 * i;
                int c = 3 * j;
                if (ch == '/')
                {
                    vec[r][c + 2] = '.';
                    vec[r + 1][c + 1] = '.';
                    vec[r + 2][c] = '.';
                }
                else if (ch == '\\')
                {
                    vec[r][c] = '.';
                    vec[r + 1][c + 1] = '.';
                    vec[r + 2][c + 2] = '.';
                }
            }
        }

        int answer = 0;
        for (int i = 0; i < newSize; ++i)
        {
            for (int j = 0; j < newSize; ++j)
            {
                if (vec[i][j] == ' ' && vst[i][j] == false)
                {
                    answer++;
                    flood(vec, i, j);
                }
            }
        }
        return answer;
    }

    void flood(vector<vector<char>> &grid, int r, int c)
    {
        queue<pair<int, int>> q;
        q.push({ r, c });

        vst[r][c] = true;

        int dr[] = { 0, -1, 0, 1 };
        int dc[] = { 1, 0, -1, 0 };

        while (!q.empty())
        {
            int r = q.front().first;
            int c = q.front().second;

            q.pop();

            for (int d = 0; d < 4; ++d)
            {
                int nr = r + dr[d];
                int nc = c + dc[d];

                if (nr < 0 || nr >= newSize || nc < 0 || nc >= newSize || grid[nr][nc] == '.' || vst[nr][nc])
                    continue;

                vst[nr][nc] = true;
                q.push({ nr, nc });
            }
        }
    }
};

int main()
{
    vector<string> grid = { " /", "/ " };

    Solution sol;
    cout << sol.regionsBySlashes(grid) << endl;

    return 0;
}