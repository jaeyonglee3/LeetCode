class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # MOST OPTIMAL SOLUTION
        
        # Step 1: Immediate length check (O(1))
        # If lengths differ, they cannot be anagrams.
        if len(s) != len(t):
            return False
        
        # Step 2: Frequency Counting (O(n))
        # collections.Counter is implemented in C, making it 
        # faster than a manual loop in standard Python.
        return Counter(s) == Counter(t)