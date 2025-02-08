#include <map>
#include <vector>

using namespace std;

class Solution
{
public:
    vector<int> topKFrequent(vector<int> &nums, int k)
    {
        unordered_map<int, int> freqs;
        for (auto num : nums)
        {
            freqs[num]++;
        }

        int pivot = pow(10, 5) + 1;
        vector<vector<int>> vec(pivot);

        for (auto freq : freqs)
        {
            int key = freq.first;
            int value = freq.second;
            vec[value].push_back(key);
        }

        vector<int> ans;

        for (int i = pivot - 1; i > 0; --i)
        {
            for (int j = 0; j < min((int)vec[i].size(), k); ++j)
            {
                ans.push_back(vec[i][j]);
            }

            if ((k -= vec[i].size()) <= 0)
                break;
        }
        return ans;
    }
};