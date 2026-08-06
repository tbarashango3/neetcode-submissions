class Solution:
    def maxA(self, n: int) -> int:
        """
        1=1
        2=2
        3=3
        4=4
        5=5
        6=6
        7=9
        8=12
        9=16
        10=20
        11=25
        x + xy = z
        x + y + 2 = n
        """
        dp = [i for i in range(n + 1)]
        for i in range(7, n + 1):
            for j in range(i - 3, 0, -1):
                dp[i] = max(dp[i], dp[j] * (i - j - 1))
        return dp[n]