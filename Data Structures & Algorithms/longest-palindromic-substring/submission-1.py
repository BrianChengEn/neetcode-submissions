class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        res = ""
        for length in range(1, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1

                if s[left] == s[right] and (length <= 2 or dp[left + 1][right - 1]):
                    dp[left][right] = True

                    if length > len(res):
                        res = s[left:right + 1]
        
        return res