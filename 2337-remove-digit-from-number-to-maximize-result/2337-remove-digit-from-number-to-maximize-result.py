class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res = []

        for i, num in enumerate(number):
            if num == digit:
                res.append(number[:i] + number[i+1:])

        return max(res)
