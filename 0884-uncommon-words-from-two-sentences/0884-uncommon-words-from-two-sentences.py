class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        uncommons = []
        combined = (s1 + " " + s2).split()

        for word in combined:
            if combined.count(word) == 1:
                uncommons.append(word)
        
        return uncommons