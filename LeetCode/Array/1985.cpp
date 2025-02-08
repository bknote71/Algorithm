#include <algorithm>
#include <vector>

using namespace std;

class Solution
{
public:
    string kthLargestNumber(vector<string> &nums, int k)
    {
        sort(nums.begin(), nums.end(),
             [](const string &u, const string &v)
             {
                 if (u.size() == v.size())
                 {
                     return u < v;
                 }
                 return u.size() < v.size();
             });

        return nums[nums.size() - k];
    }
};