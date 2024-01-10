class Solution:
    # ATTEMPT 1, correct but slow:
    # def mostFrequentEven(self, nums: List[int]) -> int:
    #     evens = {num for num in nums if num % 2 == 0}
    #     if not evens:
    #         return -1
        
    #     frequencies = defaultdict(set)  # Map frequencies to sets of numbers
    #     for num in evens:
    #         frequencies[nums.count(num)].add(num)

    #     highest = max(frequencies.keys())
    #     return min(frequencies[highest])

    def mostFrequentEven(self, nums: List[int]) -> int:
        evens = [num for num in nums if num % 2 == 0]
        if not evens:
            return -1
        
        frequencies = Counter(evens)
        return min(frequencies, key=lambda x: (-frequencies[x], x))
