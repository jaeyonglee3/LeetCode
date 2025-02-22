class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # the question guarantees nums to have at least 1
        # element that occurs more than half the time in the array

        max_occurances = -math.inf
        res = 0
        h_map = collections.defaultdict(int)

        for n in nums:
            h_map[n] += 1
            
            if h_map[n] > max_occurances:
                max_occurances = h_map[n]
                res = n
        
        return res