class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # paraphrase
        # need to return a list containing all elements from the matrix visited in spiral order
        
        # dry runs (examples)
        # Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
        # visited order
        # 0, 0
        # 0, 1
        # 0, 2
        # 1, 2
        # 2, 2
        # 2, 1
        # 2, 0
        # 1, 0
        # 1, 1

        res = []
        l, r = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while r > l and bottom > top:
            # to the right
            for i in range(l, r):
                res.append(matrix[top][i])
            
            top += 1
            
            # downwards
            for j in range(top, bottom):
                res.append(matrix[j][r - 1])
            
            r -= 1

            if not (l < r and top < bottom):
                break

            # to the left
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[bottom - 1][i])
            
            bottom -= 1
            
            # upwawrds
            for j in range(bottom - 1, top - 1, -1):
                res.append(matrix[j][l])
            
            l += 1
        
        return res