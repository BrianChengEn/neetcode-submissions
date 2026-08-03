class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = [[] for _ in range(numCourses)]
        state = [0] * numCourses

        for course, pre in prerequisites:
            prereq[course].append(pre)
        
        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True
            
            state[course] = 1
            for pre in prereq[course]:
                if not dfs(pre):
                    return False
            state[course] = 2

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True