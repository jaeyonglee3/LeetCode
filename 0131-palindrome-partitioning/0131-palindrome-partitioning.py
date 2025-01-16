class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partition = []

        def backtrack(i):
            if i > len(s) - 1:
                res.append(partition[:])
                return
            
            for j in range(i, len(s)):
                curr_sstring = s[i : j + 1]
                if self.isPalindrome(curr_sstring):
                    partition.append(curr_sstring)
                    backtrack(j + 1)
                    partition.pop()
        
        backtrack(0)
        return res
        
    def isPalindrome(self, word):
        l, r = 0, len(word) - 1

        while r > l:
            if word[l] != word[r]:
                return False
            
            l += 1
            r -= 1
        
        return True