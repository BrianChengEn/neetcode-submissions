class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # initialize
        dp = [0] * (n + 1)
        # base case
        dp[0] = 1

        # start at dp[1] to identify s[0]
        for i in range(1, n + 1):
            # choice 1: select s[i - 1], so the structure will be s[0:i - 1] | s[i - 1].
            # so we can add the number of the way in the case dp[i - 1]
            # for example: "12345" | "6"
            # in this case, the number of the ways will be same as "12345", which is dp[i - 1]
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            
            # choice 2: select s[i - 2:i], then the structure will be s[0:i - 2] | s[i - 2:i]
            # for example: "1234" | "56"
            # in this case, the number of the ways will be same as "1234", which is dp[i - 2]
            if i > 1 and 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]
        
        return dp[-1]