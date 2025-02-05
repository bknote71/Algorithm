#include <queue>
#include <vector>

using namespace std;

/**
 * 고립된 섬 개수 문제
 *
 * 핵심 포인트
 * 1. for (i, j) 로 탐색하는 순서 (거의 고정된 형태. 다른 방식은 큐 혹은 pq 사용)
 * - 한 번 방문한 섬은 다시 카운팅하지 않도록 한다.
 * - 방문에 대한 '표시'
 *
 * 2. 왜 방문 체크(vst[r][c] = true)를 큐에서 꺼낸 후 하게되면 시간초과가 발생할까요?
 * - 4가지 방향에서 동일한 점에 대해 동일한 (큐) 레벨에 접근하여 큐에 삽입할 수 있음.
 * - 즉 쓸데없는 방문 횟수가 증가하는 것.
 */

class Solution
{
public:
    int R;
    int C;
    int count = 0;
    vector<vector<bool>> vst;

    int numIslands(vector<vector<char>> &grid)
    {
        R = grid.size();
        C = grid[0].size();

        vst.resize(R, vector<bool>(C, false));

        for (int i = 0; i < R; ++i)
        {
            for (int j = 0; j < C; ++j)
            {
                if (grid[i][j] == '1' && vst[i][j] == false)
                {
                    flood(grid, i, j);
                    count++;
                }
            }
        }

        return count;
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

                if (nr < 0 || nr >= R || nc < 0 || nc >= C || grid[nr][nc] == '0' || vst[nr][nc])
                    continue;

                vst[nr][nc] = true;
                q.push({ nr, nc });
            }
        }
    }
};