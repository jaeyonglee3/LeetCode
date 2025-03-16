class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res = set()

        for i, num in enumerate(number):
            if num == digit:
                res.add(number[:i] + number[i+1:])

        return max(res)
