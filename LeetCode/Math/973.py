class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        arr = sorted([(p[0] ** 2 + p[1] ** 2, i) for i, p in enumerate(points)])[:k]
        answer = []
        for _, i in arr:
            answer.append(points[i])
        return answer
