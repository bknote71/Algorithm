#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>

using namespace std;

class Solution
{
public:
    vector<int> missingRolls(vector<int> &rolls, int mean, int n)
    {
        int m = rolls.size();
        int sumOfRolls = mean * (n + m) - accumulate(rolls.begin(), rolls.end(), 0);

        if (sumOfRolls < n || sumOfRolls > 6 * n)
            return {};

        int base = sumOfRolls / n;
        int extra = sumOfRolls % n;

        vector<int> result(n, base);
        for (int i = 0; i < extra; ++i)
            ++result[i];

        return result;
    }
};