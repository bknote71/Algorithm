#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

/**
 * 핵심 포인트
 * - (정렬) 두 요소(u, v) 간 순서 비교: 어느 요소가 먼저 와야할까?
 * - 이것이 sort 'cmp'의 정체이다.
 *
 * 좀 더 일반적인 결론을 낼 수 있도록.. (항상 그렇게 생각하지만 잘 안되는..)
 * 일반적인 결론을 내기 위해서 뭘 해야할까?
 */
class Solution
{
public:
    string largestNumber(vector<int> &nums)
    {
        vector<string> vt(nums.size());
        transform(nums.begin(), nums.end(), vt.begin(), [](int num) { return to_string(num); });

        sort(vt.begin(), vt.end(), [](const string &u, const string &v) { return u + v > v + u; });

        string ans;
        for (auto &s : vt)
        {
            ans += s;
        }

        return ans[0] == '0' ? "0" : ans;
    }
};

int main()
{
    vector<int> v = { 901, 92, 9 };
    Solution sol;
    sol.largestNumber(v);
    return 0;
}