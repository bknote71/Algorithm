class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        cand = min(n * n * w, maxWeight)
        return cand // w
