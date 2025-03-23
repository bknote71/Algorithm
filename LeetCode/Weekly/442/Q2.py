from collections import defaultdict


class Solution:
    def numberOfComponents(self, properties: list[list[int]], k: int) -> int:
        # 교집합이 k개 이상인 것들을 모아놓은 컴포넌트 수
        # union-find를 하든 그래프를 만들든
        # 중요한 것은 어떻게 비교를 할 것인가임

        # intersect 비교: n^2
        # - 이거를 O(n으로 할 수 있나요?)
        # - 정렬시킨 상태에서 p[i][a] p[j][b] 비교
        # < : a+=1, > b += 1, == cnt += 1 ad a+=1,b+=1
        # 총 cnt >=k 개 이면 노드 연결
        #
        # 이러면 n^3비교 가능
        # 정렬: n^2 log n

        n = len(properties)
        props = [sorted(p) for p in properties]
        graph = defaultdict(list)

        def has_k_common(a, b) -> bool:
            i = j = cnt = 0
            s = set()

            while i < len(a) and j < len(b):
                if a[i] < b[j]:
                    i += 1
                elif a[i] > b[j]:
                    j += 1
                else:
                    if a[i] not in s:
                        s.add(a[i])
                        cnt += 1
                        if cnt >= k:
                            return True
                    i += 1
                    j += 1

            return False

        for i in range(n):
            for j in range(i + 1, n):
                if has_k_common(props[i], props[j]):
                    graph[i].append(j)
                    graph[j].append(i)

        vst = [False] * n

        def dfs(cur):
            vst[cur] = True
            for nei in graph[cur]:
                if not vst[nei]:
                    dfs(nei)

        answer = 0
        for i in range(n):
            if not vst[i]:
                dfs(i)
                answer += 1

        return answer


print(Solution().numberOfComponents([[1, 2], [1, 1], [3, 4], [4, 5], [5, 6], [7, 7]], 1))
print(Solution().numberOfComponents([[1, 1], [1, 1]], 2))
