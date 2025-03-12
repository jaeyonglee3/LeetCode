class Solution:
    def __init__(self):
        self.memo = {}

    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(start, curr_part):
            if start == len(s):
                res.append(curr_part.copy())
                return
            
            for end in range(start, len(s)):
                if self.isPalindrome(s[start : end + 1]):
                    curr_part.append(s[start : end + 1])
                    dfs(end + 1, curr_part)
                    curr_part.pop()
        
        dfs(0, [])
        return res
        
    def isPalindrome(self, s: str):
        if s in self.memo:
            return self.memo[s]

        # O(n) time
        l, r = 0, len(s) - 1
        while r >= l:
            if s[l] != s[r]:
                self.memo[s] = False
                return False
            l += 1
            r -= 1
        
        self.memo[s] = True
        return True