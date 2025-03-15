import heapq


class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        # extranStudents -> 10^5이거든용?
        # 할 때마다, heap? 가장 작은 녀석
        # pass/total, pass, total
        n = len(classes)
        heap = []

        for c in classes:
            passs, total = c[0], c[1]
            heapq.heappush(
                heap, (-(((passs + 1) / (total + 1)) - (passs / total)), passs, total)
            )

        # 증가폭이 큰 것으로 할까?
        # 2 / 3 vs 3 / 5

        for _ in range(extraStudents):
            _, passs, total = heapq.heappop(heap)
            passs += 1
            total += 1
            heapq.heappush(
                heap, (-(((passs + 1) / (total + 1)) - (passs / total)), passs, total)
            )

        sum = 0
        for i in range(n):
            _, x, y = heap[i]
            sum += x / y

        return sum / n


Solution().maxAverageRatio([[1, 2], [3, 5], [2, 2]], 2)
