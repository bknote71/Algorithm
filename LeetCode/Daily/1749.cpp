#include <vector>

using namespace std;

class Solution
{
public:
    int maxAbsoluteSum(vector<int> &nums)
    {
        int answer1 = 0, answer2 = 0;

        for (int i = 0, cursum = 0; i < nums.size(); ++i)
        {
            cursum += nums[i];
            if (cursum < 0)
            {
                cursum = 0;
            }

            answer1 = max(answer1, cursum);
        }

        for (int i = 0, cursum = 0; i < nums.size(); ++i)
        {
            cursum += nums[i];
            if (cursum > 0)
            {
                cursum = 0;
            }

            answer2 = min(answer2, cursum);
        }

        return max(answer1, -answer2);
    }
};