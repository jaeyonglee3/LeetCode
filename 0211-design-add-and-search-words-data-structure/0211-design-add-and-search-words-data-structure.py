class TrieNode:
    def __init__(self):
        self.children = {}
        self.ends_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                curr.children[c] = TrieNode()
                curr = curr.children[c]
        
        curr.ends_word = True

    def search(self, word: str) -> bool:
        # use a recursive helper function
        return self.searchHelper(0, word, self.root)
    
    def searchHelper(self, i, word, curr) -> bool:
        if i == len(word):
            return curr.ends_word
        
        is_dot = word[i] == "."
        if len(curr.children) == 0:
            return False
        if not is_dot and word[i] not in curr.children:
            return False
        
        if is_dot:
            for c in curr.children:
                if self.searchHelper(i + 1, word, curr.children[c]):
                    return True
        else:
            return self.searchHelper(i + 1, word, curr.children[word[i]])
        
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)