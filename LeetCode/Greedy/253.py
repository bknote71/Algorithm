import heapq


class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        # 정렬 + 최대힙
        intervals.sort()

        heap = []
        answer = 0

        for s, e in intervals:
            while heap and heap[0] <= s:
                heapq.heappop(heap)

            heapq.heappush(heap, e)
            answer = max(answer, len(heap))

        return answer
