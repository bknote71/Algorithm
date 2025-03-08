from collections import defaultdict
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = defaultdict(int)
        for char in s:
            cnt[char] += 1

        heap = []
        for k, v in cnt.items():
            heapq.heappush(heap, (-v, k))

        answer = []

        while len(heap) >= 2:
            v1, k1 = heapq.heappop(heap)
            v2, k2 = heapq.heappop(heap)

            print(k1, k2)
            answer.append(k1)
            answer.append(k2)

            v1, v2 = -v1 - 1, -v2 - 1
            if v1 > 0:
                heapq.heappush(heap, (-v1, k1))
            if v2 > 0:
                heapq.heappush(heap, (-v2, k2))

        while heap:
            v, k = heapq.heappop(heap)
            if answer and answer[-1] == k:
                return ""

            answer.append(k)
            if -v - 1 > 0:
                heapq.heappush(heap, (-v - 1, k))

        return "".join(answer)


# print(Solution().reorganizeString("aaab"))
# print(Solution().reorganizeString("vvvlo"))
print(Solution().reorganizeString("baaba"))
