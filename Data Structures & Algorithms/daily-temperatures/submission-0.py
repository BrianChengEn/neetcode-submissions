class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        index = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1]:
                pre_i = index.pop()
                stack.pop()
                res[pre_i] = i - pre_i
            stack.append(t)
            index.append(i)
        
        return res