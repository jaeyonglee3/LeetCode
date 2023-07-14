class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_num = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        number = 0
        for i in range(len(s) - 1):
            if roman_to_num[s[i]] < roman_to_num[s[i + 1]]:
                number = number - roman_to_num[s[i]]
            else:
                number = number + roman_to_num[s[i]]

        return number + roman_to_num[s[len(s) - 1]]