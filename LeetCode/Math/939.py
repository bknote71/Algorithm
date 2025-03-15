from collections import defaultdict
import bisect

# bisect_left(ylist, y):
# - y보다 크거나 같은 첫 번째 위치 (삽입해야 할 위치)
# - y가 가장 큰 값보다 크다면 len(ylist) 반환


class Solution:
    def minAreaRect(self, points: list[list[int]]) -> int:
        crd = defaultdict(list)

        # x 좌표별로 y 좌표를 그룹화
        for x, y in points:
            crd[x].append(y)

        # y 좌표 정렬
        for key in crd:
            crd[key].sort()

        x_keys = sorted(crd.keys())  # x 좌표를 정렬
        min_area = float("inf")

        for i in range(len(x_keys) - 1):
            for j in range(i + 1, len(x_keys)):
                x1, x2 = x_keys[i], x_keys[j]

                y1_list, y2_list = crd[x1], crd[x2]
                common_ys = []

                for y in y1_list:
                    idx = bisect.bisect_left(y2_list, y)  # y2_list에서 y 찾기
                    if idx < len(y2_list) and y2_list[idx] == y:
                        common_ys.append(y)

                if len(common_ys) >= 2:
                    for k in range(len(common_ys) - 1):
                        y1, y2 = common_ys[k], common_ys[k + 1]
                        area = abs(x2 - x1) * abs(y2 - y1)
                        min_area = min(min_area, area)

        return min_area if min_area != float("inf") else 0
