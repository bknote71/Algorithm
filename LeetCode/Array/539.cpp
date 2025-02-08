#include <vector>

using namespace std;

/**
 * C++에서 '양수 결과'가 나오는 모듈러 연산 구현 (like python)
 * - (x % mod + mod) % mod
 * - x % mod가 음수일 때 + mod 시 양수 결과 모듈러.
 * - x % mod가 양수일 때 + mod 시 mod 보다 크기 때문에 % mod를 해줌.
 */

class Solution
{
public:
    int findMinDifference(vector<string> &timePoints)
    {
        vector<int> vt(timePoints.size());
        transform(timePoints.begin(), timePoints.end(), vt.begin(), [this](const string &u) { return getminute(u); });
        sort(vt.begin(), vt.end());

        const int p = 24 * 60;
        int answer = p;

        for (int i = 0; i < vt.size(); ++i)
        {
            int prev = i == 0 ? vt.size() - 1 : i - 1;
            answer = min(answer, ((vt[i] - vt[prev]) % p + p) % p);
        }
        return answer;
    }

    int getminute(const string &s)
    {
        int hours, minutes;
        sscanf(s.c_str(), "%d:%d", &hours, &minutes);
        return hours * 60 + minutes;
    }
};
