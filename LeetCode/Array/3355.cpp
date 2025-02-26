#include <vector>

using namespace std;

// 본질?
// - 숫자 x(idx), idx가 쿼리 범위에 포함되는 개수가 x보다 크거나 같아야 함.
// - 모든 인자에 대해서..

// 세그트리?

class Solution
{
public:
    bool isZeroArray(vector<int> &nums, vector<vector<int>> &queries)
    {
        // open(0), close(1)로 구분 및 sorting
        // 둘이 같으면, close 먼저 (딱히 필요 없겠군)

        vector<pair<int, int>> vt;
        for (auto query : queries)
        {
            vt.push_back({ query[0], 0 });
            vt.push_back({ query[1] + 1, 1 });
        }

        sort(vt.begin(), vt.end(),
             [](const pair<int, int> u, const pair<int, int> v)
             {
                 if (u.first == v.first)
                     return u.second > v.second;
                 return u.first < v.first;
             });

        int n = vt.size();
        int cnt = 0;
        int idx = 0;

        for (int i = 0; i < nums.size(); ++i)
        {
            // cnt 증가 처리
            while (idx < n && vt[idx].first == i)
            {
                cnt += vt[idx++].second == 0 ? 1 : -1;
            }

            if (cnt < nums[i])
                return false;
        }

        return true;
    }
};