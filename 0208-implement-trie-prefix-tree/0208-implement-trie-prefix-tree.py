class TrieNode:
    def __init__(self, isEndOfWord=False):
        self.children = {} # Maps character to its representative TrieNode
        self.isEndOfWord = isEndOfWord

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_node = self.root
        
        for i, char in enumerate(word):
            is_last_char = i == len(word) - 1

            if char in curr_node.children:
                if is_last_char:
                    curr_node.children[char].isEndOfWord = True
                else:
                    curr_node = curr_node.children[char]
            else:
                curr_node.children[char] = TrieNode(isEndOfWord=is_last_char)
                curr_node = curr_node.children[char]

    def search(self, word: str) -> bool:
        curr_node = self.root

        for i, char in enumerate(word):
            is_last_char = i == len(word) - 1

            if char in curr_node.children:
                if is_last_char:
                    return curr_node.children[char].isEndOfWord
                else:
                    curr_node = curr_node.children[char]
            else:
                return False

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