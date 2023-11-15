class Solution:
    def countSubstrings(self, s: str) -> int:
        # Use the 'expand from center' approach
        total = 0

        if len(s) == 1:
            return 1
        
        def expand_from_center(left: int, right: int):
            total = 0

            # Expand outwards from center as long as s[right] == s[left]
            while left >= 0 and right <= len(s) - 1 and s[right] == s[left]:
                total += 1
                left -= 1
                right += 1
            
            return total

        start = s[0]

        for i in range(len(s)):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i + 1)
            total += odd + even

        return total