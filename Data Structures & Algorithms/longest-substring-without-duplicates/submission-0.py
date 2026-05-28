class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = {}
        l = 0
        r = 0
        lenMax = 0
        while r < len(s):
            if s[r] not in char:
                char[s[r]] = r
                r += 1
                lenMax = max(lenMax, r - l)
            else:
                del char[s[l]]
                l += 1
        return lenMax