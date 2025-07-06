class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # paraphrase
        # 0 == empty
        # 1 == non-empty
        # Flowers cannot be planted next to one each other
        # So, in order to plant a flower, we need to find an index i within flowerbed where
            # flowerbed[i] == 0
            # flowerbed[i - 1] == 0 or out of range
            # flowerbed[i + 1] == 0 or out of range
        
        # sol'n approach
        # do a linear scan over flowerbed. each time we find an index i that meets the criteria above,
        # increment a counter, and return whether the counter == n
        # We can early return right when counter == n

        # edge case: when not adding any more flowers
        if n == 0: return True

        # this counts the number of additional flowers we can add
        num_flowers = 0

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i - 1 < 0 or flowerbed[i - 1] == 0) and (i + 1 >= len(flowerbed) or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                num_flowers += 1
            
            if num_flowers == n:
                return True
            
        return num_flowers == n

