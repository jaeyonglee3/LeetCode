class TrieNode:
    def __init__(self):
        self.children = {}  # maps char to trienode, implicitly assigns character to TrieNode
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
        
        # By the end of the loop, the curr node refers to the last character of the word        
        curr_node.isEndOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        # First, populate a Trie data structure with the words from the input arr
        all_words = Trie()
        for word in words:
            all_words.insert(word)
        
        res, visit = set(), set()
        def dfs(r, c, char_node, curr_word):
            # Base cases
            if (r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) 
                or (r, c) in visit or board[r][c] not in char_node.children):
                return
            
            visit.add((r, c))
            char_node = char_node.children[board[r][c]]
            curr_word += board[r][c]
            if char_node.isEndOfWord:
                res.add(curr_word)

            for dr, dc in directions:
                dfs(r + dr, c + dc, char_node, curr_word)

            visit.remove((r, c))
            
        
        # Call dfs helper on every cell in the board
        for row_num, row in enumerate(board):
            for col_num, _ in enumerate(row):
                dfs(row_num, col_num, all_words.root, "")
        
        return list(res)