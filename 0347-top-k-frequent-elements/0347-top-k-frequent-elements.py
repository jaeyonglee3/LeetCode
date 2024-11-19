from queue import PriorityQueue

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use a frequency map to map value to frequency
        # extract the k values with highest frequency
        res = []
        freq_map = defaultdict(lambda: 0)

        for num in nums:
            freq_map[num] += 1

        # Throw the numbers into a priority queue
        # Priority is highest frequency
        p_queue = PriorityQueue()
        for pair in freq_map.items():
            p_queue.put((-pair[1], pair[0]))

        for _ in range(k):
            res.append(p_queue.get()[1])
        
        return res
