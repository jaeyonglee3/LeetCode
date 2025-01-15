class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partition = []

        def backtrack(i):
            if i >= len(s):
                res.append(partition[:])
                return
            
            for j in range(i, len(s)):
                curr_string = s[i : j + 1]
                if self.isPalindrome(curr_string):
                    partition.append(curr_string)
                    backtrack(j + 1)
                    partition.pop()
        
        backtrack(0)
        return res

    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        while r > l:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True