from collections import defaultdict


class Solution:
    def isReflected(self, points: list[list[int]]) -> bool:
        crd = defaultdict(list)
        for point in points:
            x, y = point
            crd[y].append(x)

        # 최초의 라인 설정이 필요함.
        cand = sorted(list(crd.values())[0])
        pivot = cand[0] + cand[-1]

        # 해쉬
        # - 현재 값이 해쉬에 포함 O: 통과
        # - 포함 X: 포함시키기

        # 실시간으로 무언가를 확인하는 것이 까다롭거나 어려울 때 -> 미래에 등장할 무언가가 필요(영향)
        # - 그렇다면 모두 채운 후에 검사하는 것이 편할 때가 있다.

        # 마지막에 모든 value를 돌아가면서, 반대가 있는지 확인만 하면 된다.

        for value in crd.values():
            value.sort()
            n = len(value)

            hash = {}

            for i in range(n):
                if value[i] not in hash:
                    hash[value[i]] = True

            for i in range(n):
                if pivot - value[i] not in hash:
                    return False

        return True


# print(Solution().isReflected([[1, 1], [-1, 1]]))
# print(Solution().isReflected([[0, 0], [1, 0]]))
print(Solution().isReflected([[-16, 1], [16, 1], [16, 1]]))
