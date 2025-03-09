from collections import deque


class Solution:
    def sumRemoteness(self, grid: list[list[int]]) -> int:
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        n = len(grid)

        R = [[0] * n for _ in range(n)]
        W = [[0] * n for _ in range(n)]

        vst = {}

        def get_island_sum(r, c):
            vst[(r, c)] = True

            result = grid[r][c]

            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]

                if (
                    nr < 0
                    or nr >= n
                    or nc < 0
                    or nc >= n
                    or grid[nr][nc] == -1
                    or (nr, nc) in vst
                ):
                    continue

                result += get_island_sum(nr, nc)

            return result

        def flood(r, c, x):
            vvst = {}
            vvst[(r, c)] = True

            q = deque()
            q.append((r, c))

            while q:
                r, c = q.popleft()
                W[r][c] = x

                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    if (
                        nr < 0
                        or nr >= n
                        or nc < 0
                        or nc >= n
                        or grid[nr][nc] == -1
                        or (nr, nc) in vvst
                    ):
                        continue

                    vvst[(nr, nc)] = True
                    q.append((nr, nc))

            return

        # solve
        total = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] != -1 and (i, j) not in vst:
                    x = get_island_sum(i, j)

                    flood(i, j, x)
                    total += x

        answer = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == -1:
                    continue

                R[i][j] = total - W[i][j]
                answer += R[i][j]

        # for i in range(n):
        #     for j in range(n):
        #         print(W[i][j], end=" ")
        #     print()

        # for i in range(n):
        #     for j in range(n):
        #         print(R[i][j], end=" ")
        #     print()

        return answer


# Solution().sumRemoteness([[-1, 1, -1], [5, -1, 4], [-1, 3, -1]])
print(Solution().sumRemoteness([[-1, 3, 4], [-1, -1, -1], [3, -1, -1]]))
