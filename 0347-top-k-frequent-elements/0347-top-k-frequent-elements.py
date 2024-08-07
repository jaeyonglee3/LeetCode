class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq_map = defaultdict(lambda: 0)

        for num in nums:
            freq_map[num] += 1

        sorted_map = dict(sorted(freq_map.items(), key=lambda item: item[1]))
        sorted_keys = list(sorted_map.keys())

        for _ in range(k):
            res.append(sorted_keys.pop())
        
        return res
