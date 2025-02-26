#include <algorithm>
#include <numeric>
#include <set>
#include <vector>

using namespace std;

class Solution
{
public:
    string rankTeams(vector<string> &votes)
    {
        int arr[26][1001] = { 0 };
        int n = votes[0].length();

        set<int> s;

        for (auto vote : votes)
        {
            for (int i = 0; i < n; ++i)
            {
                ++arr[vote[i] - 'A'][i];
                s.insert(vote[i] - 'A');
            }
        }

        // set의 key를 vt로
        vector<int> vt(s.begin(), s.end());

        sort(vt.begin(), vt.end(),
             [&arr, n](const int a, const int b)
             {
                 for (int i = 0; i < n; ++i)
                 {
                     if (arr[a][i] == arr[b][i])
                         continue;

                     return arr[a][i] > arr[b][i];
                 }

                 return a < b;
             });

        string result = accumulate(vt.begin(), vt.end(), string(), [](string a, int b) { return a + char(b + 'A'); });

        return result;
    }
};