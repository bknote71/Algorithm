class Solution:
    def smallestSufficientTeam(
        self, req_skills: list[str], people: list[list[str]]
    ) -> list[int]:
        n = len(people)
        sn = len(req_skills)

        skill_map = {skill: i for i, skill in enumerate(req_skills)}
        inf = float("inf")

        dp = {}

        def dfs(idx, state):
            if state == (1 << sn) - 1:
                return 0

            if idx >= n:
                return inf

            if (idx, state) in dp:
                return dp[(idx, state)]

            ret = dfs(idx + 1, state)

            cand = 0

            for ps in people[idx]:
                cand |= 1 << skill_map[ps]

            if state | cand != state:
                ret = min(ret, 1 + dfs(idx + 1, state | cand))

            dp[((idx, state))] = ret
            return ret

        dfs(0, 0)

        answer = []

        def reconstruct(idx, state):
            if state == (1 << sn) - 1:
                return

            if idx >= n:
                return

            if dp.get((idx, state), inf) == dp.get((idx + 1, state), inf):
                reconstruct(idx + 1, state)
            else:
                cand = 0
                for ps in people[idx]:
                    cand |= 1 << skill_map[ps]

                answer.append(idx)
                reconstruct(idx + 1, state | cand)

        reconstruct(0, 0)

        return answer


print(
    Solution().smallestSufficientTeam(
        ["java", "nodejs", "reactjs"], [["java"], ["nodejs"], ["nodejs", "reactjs"]]
    )
)
