class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1

        for n in nums:
            product *= n
        
        return self.signFunc(product)
    
    def signFunc(self, x) -> int:
        if x == 0:
            return 0
        elif x > 0:
            return 1
        else:
            return -1