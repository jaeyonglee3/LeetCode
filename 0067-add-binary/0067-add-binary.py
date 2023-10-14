class Solution:
    def addBinary(self, a: str, b: str) -> str:
        dec_a = 0
        dec_b = 0
        
        for idx, num in enumerate(a):
            power = len(a) - idx - 1
            dec_a += int(num) * (2 ** power)
        
        for idx, num in enumerate(b):
            power = len(b) - idx - 1
            dec_b += int(num) * (2 ** power)
        
        total = dec_a + dec_b

        return str(bin(total))[2:]