class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # The find() method returns the index of first occurrence of the substring (if found). If not found, it returns -1.
        # The rfind() method returns the highest index of the substring (if found). If not found, it returns -1.

        return max([s.rfind(char) - (s.find(char) + 1) for char in s if s.rfind(char) != -1])
                