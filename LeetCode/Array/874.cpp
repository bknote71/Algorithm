#include <iostream>
#include <map>
#include <vector>

using namespace std;

// unordered_map의 키는 기본적으로 해시 가능한 타입이어야 한다.
// - pair<int, int>는 해시를 지원하지 않음

// 전용 해시 함수
struct pair_hash
{
    size_t operator()(const pair<int, int> &p) const { return hash<int>()(p.first) ^ hash<int>()(p.second); }
};

class Solution
{
public:
    int robotSim(vector<int> &commands, vector<vector<int>> &obstacles)
    {
        int x = 0, y = 0;
        int answer = 0;

        // 동, 북, 서, 남
        int dx[4] = { 1, 0, -1, 0 };
        int dy[4] = { 0, 1, 0, -1 };
        int dir = 1;

        unordered_map<pair<int, int>, int, pair_hash> obs;
        for (auto &ob : obstacles)
        {
            obs[{ ob[0], ob[1] }] = 1;
        }

        for (int cmd : commands)
        {
            if (cmd == -1)
            {
                dir = (dir + 3) % 4;
            }
            else if (cmd == -2)
            {
                dir = (dir + 1) % 4;
            }
            else
            {
                for (int i = 0; i < cmd; ++i)
                {
                    int nx = x + dx[dir];
                    int ny = y + dy[dir];

                    if (obs[{ nx, ny }] > 0)
                        break;

                    x = nx;
                    y = ny;
                    answer = max(answer, x * x + y * y);
                }
            }
        }
        return answer;
    }
};

int main()
{
    vector<int> v = { 4, -1, 4, -2, 4 };
    vector<vector<int>> obs = { { 2, 4 } };
    Solution sol;
    cout << sol.robotSim(v, obs) << endl;

    return 0;
}