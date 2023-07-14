class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for substring in patterns:
            if substring in word:
                count += 1
        
        return count