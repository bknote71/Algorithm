#include <algorithm>
#include <vector>

using namespace std;

/**
 * 핵심 포인트
 * 1. 추적하는 최고 끝과, 현재 순회 요소의 시작 위치를 비교하는 것
 * - 최고 끝 >= 시작위치: 구간에 포함
 * - 최고 끝 < 시작위치: 기존 구간을 기록([left, right])하고, 새로운 left, right로 시작.
 *
 * 2. 마지막 부분에 대한 처리
 * - for 문이 끝났을 때 한 번 더 넣어줘야 할 까?
 * - 마지막 처리 부분에 대한 예시를 생각해보기.
 *
 *
 * sort(begin, end, cmp)
 * - cmp: [](const Element& e1, const Element& e2) { e1 < e2; }
 *
 * ++ vector.push_back(vector)
 * - {벡터요소1, 요소2, .. 요소n} push_back 가능
 */

class Solution
{
public:
    vector<vector<int>> merge(vector<vector<int>> &intervals)
    {
        sort(intervals.begin(), intervals.end(), [](const vector<int> &a, const vector<int> &b) { return a[0] < b[0]; });

        vector<vector<int>> ans;

        int left = intervals[0][0];
        int right = intervals[0][1];

        for (int i = 0; i < intervals.size(); ++i)
        {
            int l = intervals[i][0];
            int r = intervals[i][1];

            if (right >= l)
                right = max(right, r);
            else
            {
                ans.push_back({ left, right });
                left = l;
                right = r;
            }
        }

        ans.push_back({ left, right });
        return ans;
    }
};