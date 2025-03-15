class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        # minimum diff

        # HH:MM에 대해서 정렬 후, 최소 diff를 찾는다.
        # 00:00 0
        # 23:59 1440 - 1
        # % 1440

        def convert(timestr: str) -> int:
            h, m = map(int, timestr.split(":"))
            return 60 * h + m

        arr = sorted([convert(timePoint) for timePoint in timePoints])

        p = convert("24:00")
        answer = (arr[0] - arr[-1] + p) % p

        for i in range(len(arr) - 1):
            answer = min(answer, arr[i + 1] - arr[i])

        return answer


print(Solution().findMinDifference(["23:59", "00:00"]))
