class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # NeetCode video solution - most efficient but requires some tricks
        prefix_set = set()
        res = 0

        for n in arr1:
            while n and n not in prefix_set:
                prefix_set.add(n)
                # use // 10 to remove the rightmost digit
                # we start with each numbers LARGEST possible prefix because
                # it is likely that its smaller prefixes are already in the prefix set.
                # so do n // 10 and keep going until n is either 0 or n is already in the set.
                n = n // 10
        
        for n in arr2:
            while n and n not in prefix_set:
                # now, we want to update the result only if we find a prefix in arr2 that is in prefix_set.
                # again start with the biggest prefix n can be, and // 10 to remove rightmost digit each time.
                # if this loop stops before n == 0, that means we've found a prefix that some num in arr1
                # and some num in arr2 share. So update the result only if n does not become 0.
                n = n // 10
            
            if n != 0:
                res = max(res, len(str(n)))
        
        return res