class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        
        def dfs(index, node):
            if index == len(word):
                return node.isEnd
            
            c = word[index]
            if c == ".":
                for w in node.children:
                    if dfs(index + 1, node.children[w]):
                        return True
                return False
            
            if c not in node.children:
                return False

            return dfs(index + 1, node.children[c])

        return dfs(0, self.root)