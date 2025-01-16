class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
        
            curr = curr.children[c]
        
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        # j is index param, 
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    # backtracking approach
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else: 
                    if c not in curr.children:
                        return False
                
                    curr = curr.children[c]
            
            return curr.isEndOfWord
        
        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)