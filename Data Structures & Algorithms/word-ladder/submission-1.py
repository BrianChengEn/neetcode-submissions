class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        que = deque([[beginWord, 1]])

        if beginWord in wordSet:
            wordSet.remove(beginWord)
        
        while que:
            word, length = que.popleft()

            if word == endWord:
                return length
            
            chars = list(word)

            for i in range(len(chars)):
                origin = chars[i]

                for char in "abcdefghijklmnopqrstuvwxyz":
                    if char == origin:
                        continue
                    
                    chars[i] = char
                    next_word = "".join(chars)

                    if next_word in wordSet:
                        wordSet.remove(next_word)
                        que.append([next_word, length + 1])
                chars[i] = origin
        
        return 0