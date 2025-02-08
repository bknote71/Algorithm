#include <vector>

using namespace std;

/**
 * 핵심 포인트
 * - 요소간의 순서가 존재하고, 어떤 '순서' 혹은 '방식'으로 탐색할 것인가.
 * - 예) 작은 순서의 요소(그룹)부터 탐색
 *
 * k번째 푸는 방식 중 하나: 작은 순서의 요소 혹은 그룹부터 탐색 및 포인트까기
 * group < left_k: left_k -= group
 * else: 그룹에 포함되는 것.
 *
 * ++ 순서대로 탐색하는 방법 이외에도, 어떤 값을 기준으로 연산을 했을 때 결과가 k개에 포함되는지를 판단하는 방식도 존재
 * - 그것을 기반으로 이분탐색..
 */

class Solution
{
public:
    int findKthLargest(vector<int> &nums, int k)
    {
        auto base = pow(10, 4);
        vector<int> vt(2 * base + 1, 0);

        for (auto num : nums)
        {
            vt[num + base]++;
        }

        // 0부터 ~ 2 * base 까지
        int left_k = k;
        for (int i = 2 * base; i >= 0; --i)
        {
            if (vt[i] < left_k)
                left_k -= vt[i];
            else
                return i - base;
        }

        return 0;
    }
};