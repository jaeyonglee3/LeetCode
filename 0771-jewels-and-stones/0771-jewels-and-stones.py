class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0

        for jewel in jewels:
            if jewel in stones:
                count += stones.count(jewel)
        
        return count
