class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Set = sorted(s1)
        for i in range(len(s2) - len(s1) + 1):
            s2Set = sorted(s2[i:i + len(s1)])
            if s2Set == s1Set:
                return True
        return False