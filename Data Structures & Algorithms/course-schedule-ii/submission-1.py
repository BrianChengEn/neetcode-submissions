class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        path = []

        prereq = [[] for _ in range(numCourses)]
        state = [0] * numCourses

        for c, pre in prerequisites:
            prereq[c].append(pre)

        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True
            
            state[course] = 1

            for pre in prereq[course]:
                if not dfs(pre):
                    return False
            
            path.append(course)
            state[course] = 2
            return True
        
        for i in range(numCourses):
            path = []
            if not dfs(i):
                return []
            for j in range(len(path)):
                res.append(path[j])
        
        return res