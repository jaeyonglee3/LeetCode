class Solution:
    def maxPower(self, s: str) -> int:
        count, max_count = 1, 1

        for i in range(len(s) - 1):
            if s[i + 1] == s[i]:
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 1

        return(max_count)