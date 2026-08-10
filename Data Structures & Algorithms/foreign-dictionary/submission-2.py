class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = {}

        for word in words:
            for char in word:
                indegree[char] = 0
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            min_len = min(len(word1), len(word2))

            if word1[:min_len] == word2[:min_len] and len(word1) > len(word2):
                return ""
            
            for j in range(min_len):
                char1 = word1[j]
                char2 = word2[j]

                if char1 != char2:
                    if char2 not in graph[char1]:
                        graph[char1].add(char2)
                        indegree[char2] += 1
                    
                    break
        
        que = deque()
        res = []

        for char in indegree:
            if indegree[char] == 0:
                que.append(char)

        while que:
            char = que.popleft()

            if indegree[char] == 0:
                res.append(char)

                for neighbor in graph[char]:
                    indegree[neighbor] -= 1
                    que.append(neighbor)
        
        if len(res) != len(indegree):
            return ""
        
        return "".join(res)