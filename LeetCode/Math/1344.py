class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:

        # 360 / 12 = 30
        alpha = 30 * (minutes / 60)

        # 360 / 60
        # 1분에 6

        minutes = (minutes * 6) % 360
        hour = (30 * hour + alpha) % 360

        # min(hour - minutes + 360) % 360 vs (minutes - hour + 360) % 360

        return min((hour - minutes + 360) % 360, (minutes - hour + 360) % 360)
