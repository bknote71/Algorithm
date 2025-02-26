#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

struct hash_pair
{
    size_t operator()(const pair<int, int> &p) const { return hash<int>()(p.first) ^ hash<int>()(p.second); }
};

class Solution
{
public:
    const int MOD = 1e9 + 7;
    unordered_map<pair<int, int>, int, hash_pair> memo;

    int n;

    int dfs(vector<int> &arr, int idx, int odd)
    {
        if (idx >= n)
        {
            return odd == 1 ? 1 : 0;
        }

        pair<int, int> key = { idx, odd };
        if (memo.find(key) != memo.end())
        {
            return memo[key];
        }

        int ret = (odd == 1) ? 1 : 0;

        if (arr[idx] & 1 == 1)
        {
            ret += dfs(arr, idx + 1, odd ? 0 : 1);
        }
        else
        {
            ret += dfs(arr, idx + 1, odd ? 1 : 0);
        }

        return memo[key] = ret % MOD;
    }

    int numOfSubarrays(vector<int> &arr)
    {
        n = arr.size();

        int ret = 0;
        memo.clear();
        for (int i = 0; i < arr.size(); ++i)
        {
            ret = (ret + dfs(arr, i, 0)) % MOD;
        }
        return ret;
    }
};