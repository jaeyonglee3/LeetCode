class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Mergesort
        if len(nums) == 1:
            return nums.copy()  
        else:
            mid = len(nums) // 2 
            left_sorted = self.sortArray(nums[:mid])
            right_sorted = self.sortArray(nums[mid:])

            return self._merge(left_sorted, right_sorted)
    
    def _merge(self, lst1: list, lst2: list) -> list:
        i1, i2 = 0, 0
        sorted_so_far = []

        while i1 < len(lst1) and i2 < len(lst2):
            if lst1[i1] <= lst2[i2]:
                sorted_so_far.append(lst1[i1])
                i1 += 1
            else:
                sorted_so_far.append(lst2[i2])
                i2 += 1

        if i1 == len(lst1): 
            return sorted_so_far + lst2[i2:]
        else:
            return sorted_so_far + lst1[i1:]

    #     # Quicksort, pivot will always be nums[0]
    #     # base case
    #     if len(nums) < 2:
    #         return nums.copy()
    #     else:
    #         pivot = nums[0]
    #         smaller, bigger = self._partition(nums[1:], pivot)

    #         smaller_sorted = self.sortArray(smaller)
    #         bigger_sorted = self.sortArray(bigger)

    #         return smaller_sorted + [pivot] + bigger_sorted
        
    # def _partition(self, lst: list, pivot: Any) -> tuple[list, list]:
    #     """Return a partition of lst with the chosen pivot.

    #     Return two lists, where the first contains the items in lst
    #     that are <= pivot, and the second contains the items in lst that are > pivot.
    #     """
    #     smaller = []
    #     bigger = []

    #     for item in lst:
    #         if item <= pivot:
    #             smaller.append(item)
    #         else:
    #             bigger.append(item)
        
    #     return smaller, bigger
