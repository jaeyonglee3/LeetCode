class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # # Variable sized sliding window technique
        # left = right = 0
        # count = {}
        # res = 0

        # while right <= len(s) - 1:
        #     # At each window, we need to update our hashmap w/ character counts
        #     substring = s[left : right + 1]
        #     unique_chars = set(substring)

        #     for c in unique_chars:
        #         count[c] = substring.count(c)
            
        #     # Subtract most freq char count from length of substring 
        #     most_freq = max(count.values())
        #     total_replacements = (right - left + 1) - most_freq

        #     if total_replacements <= k:
        #         res = max(res, len(substring))
        #     else:
        #         left += 1

        #     right += 1

        # return res

        count = {}
        res = 0

        left = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)

            if (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res

        