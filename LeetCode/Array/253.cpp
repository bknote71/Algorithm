// #include <algorithm>
#include <queue>
#include <vector>

using namespace std;

/**
 * 핵심 포인트(본질이 무엇일까?)
 * - 동시에 겹치는 최대 횟수
 *
 * interval specific
 * - 정렬 (시작점 기준 혹은 끝점 기준 둘 다 생각해봐야 한다.)
 *
 * 현재 구간 기준
 * - 정렬되어 있기 때문에, 현재 구간의 시작점보다 큰 끝점을 가진 이전 구간들은 모두 겹친다.
 *
 * 참고: prioirty_queue<int>는 기본적으로 최대힙
 * 최소힙: priority_queue<int, vector<int>, greater<int>> pq;
 * - 혹은 '-' 부호 사용
 */

class Solution
{
public:
    int minMeetingRooms(vector<vector<int>> &intervals)
    {
        sort(intervals.begin(), intervals.end(), [](const vector<int> &u, const vector<int> &v) { return u[0] < v[0]; });
        priority_queue<int> pq;
        int answer = 0;

        for (auto &interval : intervals)
        {
            int s = interval[0];
            int e = interval[1];

            while (!pq.empty())
            {
                if (-pq.top() > s)
                    break;

                pq.pop();
            }

            pq.push(-e);
            answer = max(answer, (int)pq.size());
        }

        return answer;
    }
};
