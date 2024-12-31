class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Convert rows to tuple and count their frequencies
        row_count = Counter(tuple(row) for row in grid)

        # Count matches between columns and rows
        res = 0
        for col in zip(*grid):  # Zip extracts columns
            res += row_count[tuple(col)]
        
        return res