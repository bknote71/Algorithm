#include <vector>

using namespace std;

class Solution
{
public:
    int maxScoreSightseeingPair(vector<int> &values)
    {

        // 현재 인덱스 i 이전의 가장 큰 숫자.
        // - max(인덱스가 증가할 때마다 하나 감소 , values[i])
        int prev_max_value = 0;
        int answer = 0;

        for (int i = 0; i < values.size(); ++i)
        {
            answer = max(answer, values[i] + prev_max_value - 1);
            prev_max_value = max(prev_max_value - 1, values[i]);
        }

        return answer;
    }
};