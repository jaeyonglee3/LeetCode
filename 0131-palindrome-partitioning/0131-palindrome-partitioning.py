class Solution:
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
        l, r = 0, len(s) - 1
        while r >= l:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True