class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Use a nested loop to compare every row to every column
        cols = defaultdict(list)
        rows = defaultdict(list)

        for row_num, row in enumerate(grid):
            for col_num, val in enumerate(row):
                rows[row_num].append(val)
                cols[col_num].append(val)
        
        # Now, determine the number of equal row and column pairs
        all_rows = list(rows.values())
        res = 0

        for col in cols.values():
            res += all_rows.count(col)

        return res