class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Fixed length sliding window
        left = 0
        right = left + k
        min_recolors = math.inf

        while right <= len(blocks):
            sub_blocks = blocks[left: right]
            recolors = sub_blocks.count('W')
            min_recolors = min(min_recolors, recolors)
            left += 1
            right += 1

        return min_recolors