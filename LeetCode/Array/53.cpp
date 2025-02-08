#include <vector>

using namespace std;

class Solution
{
public:
    int maxSubArray(vector<int> &nums)
    {
        int mval = 0;
        int answer = -pow(10, 4);
        int sum = 0;

        for (int i = 0; i < nums.size(); ++i)
        {
            sum += nums[i];
            answer = max(answer, sum - mval);
            mval = min(mval, sum);
        }
        return answer;
    }
};