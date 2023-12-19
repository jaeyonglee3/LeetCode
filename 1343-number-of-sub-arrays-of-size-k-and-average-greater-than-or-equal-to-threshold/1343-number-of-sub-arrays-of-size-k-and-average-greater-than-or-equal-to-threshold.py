class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        curr_sum = sum(arr[:k - 1])

        for left in range(len(arr) - k + 1):
            curr_sum += arr[left + k - 1]  # add the rightmost value
            if (curr_sum / k) >= threshold:
                res += 1
            curr_sum -= arr[left]  # subtract the leftmost value
        
        return res