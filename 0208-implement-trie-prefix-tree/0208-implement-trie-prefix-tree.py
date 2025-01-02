class TrieNode:
    def __init__(self):
        self.children = {} # Maps character to its representative TrieNode
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_node = self.root
        
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode()
            
            curr_node = curr_node.children[char]
        
        # By end of for loop, curr_node refers to last char of the word
        curr_node.isEndOfWord = True

    def search(self, word: str) -> bool:
        curr_node = self.root

        for char in word:
            if char not in curr_node.children:
                return False
            else:
                curr_node = curr_node.children[char]
        
        return curr_node.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root

        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)