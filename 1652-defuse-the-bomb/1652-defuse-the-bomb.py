class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        decrypt = []
        curr_sum = 0
        
        if k == 0:
            decrypt = [0]*len(code)
        elif k > 0:
            for i in range(len(code)):
                total = sum(code[j % len(code)] for j in range(i + 1, i + 1 + k))
                decrypt.append(total)
        else:
            for i in range(len(code)):
                total = sum(code[j % len(code)] for j in range(i - 1, i - 1 + k, -1))
                decrypt.append(total)
        
        return decrypt
