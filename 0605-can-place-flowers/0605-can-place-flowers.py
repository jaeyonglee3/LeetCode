class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        res = 0
        
        for i in range(len(flowerbed)):
            if flowerbed[i] != 1:
                if i == 0 and (len(flowerbed) == 1 or flowerbed[i + 1] == 0):
                    res += 1  
                    flowerbed[i] = 1
                elif i == (len(flowerbed) - 1) and flowerbed[i - 1] == 0:
                    res += 1 
                    flowerbed[i] = 1
                elif (not (i == 0 or i == len(flowerbed) - 1) and 
                    flowerbed[i + 1] != 1 and flowerbed[i - 1] != 1):
                    res += 1
                    flowerbed[i] = 1
            else:
                pass

        return res >= n

        