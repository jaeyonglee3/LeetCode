class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # approach: we can run a multi-source BFS from all the water cells,
        # assigning heights to adjacent cells in a breadth first approach,
        # increasing the height by 1 each time we move one direction away from 
        # the original water cell. By increasing the height by only 1 each time,
        # we ensure that we meet the condition that states two adjacent cells must have an
        # abs height difference of <= 1. This condition restricts how much we can grow the
        # height by, so we know the max height in the matrix will be maximized
        ROWS, COLS = len(isWater), len(isWater[0])
        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        height = [[-1] * COLS for _ in range(ROWS)]

        q = collections.deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                if isWater[r][c] == 1:
                    height[r][c] = 0  # mark the height as 0 since its water
                    q.append((r, c))  # add the water cell's coords to queue to be processed
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc

                    if min(nr, nc) < 0 or nr == ROWS or nc == COLS or height[nr][nc] != -1:
                        continue
                    
                    height[nr][nc] = height[r][c] + 1
                    q.append((nr, nc))
        
        return height