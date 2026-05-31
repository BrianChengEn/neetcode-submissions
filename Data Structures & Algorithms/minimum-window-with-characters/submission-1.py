class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = Counter(t)
        window = defaultdict(int)

        have = 0
        required = len(need)

        res = [-1, -1]
        resLen = float("inf")

        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in need and window[c] == need[c]:
                have += 1
            
            while have == required:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                leftChar = s[l]
                window[leftChar] -= 1

                if leftChar in need and window[leftChar] < need[leftChar]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r + 1] if resLen != float("inf") else ""
