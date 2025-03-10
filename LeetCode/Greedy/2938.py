class Solution:
    def minimumSteps(self, s: str) -> int:
        # white 기준으로 진행
        # answer += 현재 white 위치 - 원래 있어야 하는 위치

        white_count = 0
        cur_white_pos = 0

        for i, char in enumerate(s):
            if char == "0":
                answer += i - cur_white_pos
                cur_white_pos += 1

        return answer
