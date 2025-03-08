class Solution:
    def maximumSwap(self, num: int) -> int:
        # 앞에서부터 시작하여 이후 것이 자신보다 큰 것이 있기만 하면 스왑
        # 숫자의 가장 뒤의 위치를 기록

        positions = {}

        strnum = list(str(num))
        for i in range(len(strnum) - 1, -1, -1):
            if strnum[i] not in positions:
                positions[strnum[i]] = i

        swapped = False

        for i in range(len(strnum)):
            for j in range(9, int(strnum[i]), -1):
                if str(j) in positions and i < positions[str(j)]:
                    pos = positions[str(j)]
                    strnum[pos], strnum[i] = strnum[i], strnum[pos]

                    swapped = True
                    break

            if swapped:
                break

        return int("".join(strnum))


print(Solution().maximumSwap(2736))
