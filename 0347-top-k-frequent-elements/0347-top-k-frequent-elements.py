class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)  # {1 : 3, 2 : 2, 3 : 1}
        res = []
        freq = dict(sorted(freq.items(), key=lambda item: item[1]))
        freqs = freq.keys()
        freqs = list(freqs)

        for _ in range(k):
            res.append(freqs.pop())

        return res
        