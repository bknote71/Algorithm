# TODO: pruning


class Solution:
    def minSessions(self, tasks: list[int], sessionTime: int) -> int:
        dp = {}
        n = len(tasks)

        # 인덱스 순회가 아닌 문제!
        # 대신 방문 상태 기록 (비트마스크) + 모든 요소 순회하여 가능한 요소 포함
        # - 총 요소의 개수가 작아야 가능

        def dfs(state, remain):
            if state == (1 << n) - 1:
                return 0

            if (state, remain) in dp:
                return dp[(state, remain)]

            result = float("inf")

            for i in range(n):
                if state & (1 << i):
                    continue

                new_state = state | (1 << i)
                if remain - tasks[i] >= 0:
                    result = min(result, dfs(new_state, remain - tasks[i]))
                else:
                    result = min(result, 1 + dfs(new_state, sessionTime - tasks[i]))

            dp[(state, remain)] = result
            return result

        return 1 + dfs(0, sessionTime)
