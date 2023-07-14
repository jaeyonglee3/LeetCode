class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def helper(word) -> str:
            letter_value = ""
            for char in word:
                letter_value += str(ord(char) - 97)
            
            return letter_value

        lvalue_one = helper(firstWord)
        lvalue_two = helper(secondWord)
        lvalue_target = helper(targetWord)

        return int(lvalue_one) + int(lvalue_two) == int(lvalue_target)
    

        
