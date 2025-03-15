class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        # 많이 연속된 것을 선택하면 된다.
        # 그 이유는 어떤 덩어리를 선택하든 + 1 이 되기 때문이다.

        arr = []

        prev = -1

        for i, char in enumerate(road):
            if char == "x" and prev == -1:
                prev = i

            elif char == "." and prev != -1:
                arr.append(i - prev)
                prev = -1

        if prev != -1:
            arr.append(len(road) - prev)

        arr.sort(reverse=True)
        answer = 0

        for num in arr:
            cand = min(num, budget - 1)
            budget -= cand + 1
            answer += cand

            if budget == 0:
                break

        return answer
