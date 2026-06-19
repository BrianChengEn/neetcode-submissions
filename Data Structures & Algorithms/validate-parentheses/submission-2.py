class Solution:
    def isValid(self, s: str) -> bool:
        
        d = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        q = deque()

        for c in s:
            if c in ['(', '{', '[']:
                q.append(c)
            else:
                if q and c == d[q[-1]]:
                    q.pop()
                else:
                    return False
        
        return True if not q else False