class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Use a nested loop to compare every row to every column
        # cols = defaultdict(tuple)
        # rows = defaultdict(tuple)

        # for row_num, row in enumerate(grid):
        #     for col_num, val in enumerate(row):
        #         rows[row_num].append(val)
        #         cols[col_num].append(val)
        
        # Now, determine the number of equal row and column pairs
        row_count = Counter(tuple(row) for row in grid)

        # Count matches between columns and rows
        res = 0
        for col in zip(*grid):  # Zip extracts columns
            res += row_count[tuple(col)]
        
        return res

        # all_rows = list(rows.values())
        # res = 0

        # for col in cols.values():
        #     res += all_rows.count(col)

        # return res