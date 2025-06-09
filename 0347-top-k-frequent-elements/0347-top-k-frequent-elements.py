class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.defaultdict(int)

        for n in nums:
            freq[n] += 1
        
        # freq.keys() - This gives you an iterable of all the keys in freq.
        # The sorted() function takes an iterable and returns a new sorted list.
        # For each key val in freq.keys(), this lambda returns freq_map[val], i.e. its frequency.
        # reverse the sort to sort in descending order (highest first)
        freq_elements = sorted(freq.keys(), key=lambda val : freq[val], reverse=True)
        return freq_elements[ : k]