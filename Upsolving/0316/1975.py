class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        # negative가 짝수개일 때
        # - 페어가 둘 다 음수 -> 한 꺼번에 양수
        # - 페어에서 하나만 음수 -> 옆으로 음수를 전달하면서, 음수 페어를 만들 수 있다. (그러고 뒤집으면 됨.)

        # negative가 홀수개일 때
        # - 1 + 짝수로 분리.
        # - 따라서 무조건 하나가 음수

        # abs가 가장 작은 요소를 빼면 된다.
        n = len(matrix)
        answer = 0
        ncount = 0
        minimum = abs(matrix[0][0])

        for i in range(n):
            for j in range(n):
                ncount += 1 if matrix[i][j] < 0 else 0
                answer += abs(matrix[i][j])
                minimum = min(abs(matrix[i][j]), minimum)

        if ncount & 1:
            answer -= 2 * minimum

        return answer


print(Solution().maxMatrixSum([[-1, 0, -1], [-2, 1, 3], [3, 2, 2]]))
