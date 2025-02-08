#include <map>
#include <vector>

using namespace std;

/**
 * 핵심 포인트
 * - 탐색 범위를 제한(단순화)한다.
 */

class Solution
{
public:
    int subarraySum(vector<int> &nums, int k)
    {
        unordered_map<int, int> table;
        int sum = 0;
        int answer = 0;

        table[0] = 1;

        for (auto num : nums)
        {
            sum += num;
            answer += table[sum - k];
            table[sum]++;
        }

        return answer;
    }
};