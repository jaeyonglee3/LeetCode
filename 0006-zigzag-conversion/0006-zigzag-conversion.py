class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        
        strs = [[] for _ in range(numRows)]  # a list of strings
        curr_row = 0
        direction_down = True

        for c in s:
            strs[curr_row].append(c)

            if curr_row == 0:
                direction_down = True
            if curr_row == numRows - 1:
                direction_down = False

            if direction_down:
                curr_row += 1
            else:
                curr_row -= 1

        new_strs = ["".join(s) for s in strs]
        res = "".join(new_strs)
        
        return res