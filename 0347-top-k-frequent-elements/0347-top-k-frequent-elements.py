class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = collections.defaultdict(int)

        for n in nums:
            freq_map[n] += 1
        
        freq_elements = sorted(freq_map.keys(), key=lambda val: freq_map[val], reverse=True)
        return freq_elements[:k]
