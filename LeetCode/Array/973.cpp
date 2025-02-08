#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    vector<vector<int>> kClosest(vector<vector<int>> &points, int k)
    {
        int n = points.size();
        vector<pair<int, int>> vt;

        for (int i = 0; i < n; ++i)
        {
            auto point = points[i];
            vt.push_back({ point[0] * point[0] + point[1] * point[1], i });
        }

        sort(vt.begin(), vt.end(), [](const pair<int, int> &u, const pair<int, int> &v) { return u.first < v.first; });

        vector<vector<int>> answer;

        for (int i = 0; i < k; ++i)
        {
            answer.push_back(points[vt[i].second]);
        }
        return answer;
    }
};