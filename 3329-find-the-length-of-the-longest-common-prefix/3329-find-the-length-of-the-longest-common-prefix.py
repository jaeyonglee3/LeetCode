class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # Hashset solution: construct two hashsets, each containing the possible
        # prefixes of each number from both arr1 and arr2. Then, do a set intersection
        # and return the max length from the prefixes that result from it.
        arr1 = [str(n) for n in arr1]
        arr2 = [str(n) for n in arr2]
        
        set1 = set()
        set2 = set()

        for n in arr1:
            curr_prefix = []
            for digit in n:
                curr_prefix.append(digit)
                set1.add(''.join(curr_prefix))
        
        for n in arr2:
            curr_prefix = []
            for digit in n:
                curr_prefix.append(digit)
                set2.add(''.join(curr_prefix))
        
        common_prefixes = set1.intersection(set2)

        if len(common_prefixes) == 0:
            return 0
        else:
            return max(len(prefix) for prefix in common_prefixes)