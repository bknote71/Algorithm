# class Solution:
#     def minTime(self, skill: list[int], mana: list[int]) -> int:
#         m = len(skill)  # 마법사 수
#         n = len(mana)  # 포션 수

#         # 마법사 스킬 누적합
#         skill_prefix = [0] * (m + 1)
#         for i in range(m):
#             skill_prefix[i + 1] = skill_prefix[i] + skill[i]

#         # potion[i][j]: i번째 포션, j번째 마법사까지 처리된 시간
#         potion = [[0] * (m + 1) for _ in range(n)]

#         # 0번째 포션: 마법사 순서대로 누적 처리
#         for j in range(1, m + 1):
#             potion[0][j] = potion[0][j - 1] + mana[0] * skill[j - 1]

#         # 나머지 포션 처리
#         for i in range(1, n):
#             best_start = float("-inf")

#             for j in range(m):
#                 best_start = max(best_start, potion[i - 1][j + 1] - mana[i] * skill_prefix[j])

#             for j in range(1, m + 1):
#                 potion[i][j] = best_start + mana[i] * skill_prefix[j]

#         return potion[n - 1][m]


# 2D DP -> 1D 슬라이딩 배열
class Solution:
    def minTime(self, skill: list[int], mana: list[int]) -> int:
        m = len(skill)
        n = len(mana)

        skill_prefix = [0] * (m + 1)
        for i in range(m):
            skill_prefix[i + 1] = skill_prefix[i] + skill[i]

        prev = [0] * (m + 1)

        for j in range(1, m + 1):
            prev[j] = prev[j - 1] + mana[0] * skill[j - 1]

        for i in range(1, n):
            best_start = float("-inf")

            for j in range(m):
                best_start = max(best_start, prev[j + 1] - mana[i] * skill_prefix[j])

            curr = [0] * (m + 1)
            for j in range(1, m + 1):
                curr[j] = best_start + mana[i] * skill_prefix[j]

            prev = curr

        return prev[m]


print(Solution().minTime([1, 5, 2, 4], [5, 1, 4, 2]))
