class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # the result contains all coordinates from which water can flow into both oceans
        ROWS, COLS = len(heights), len(heights[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pacific_set, atlantic_set = set(), set()

        for r in range(ROWS):
            pacific_set.add((r, 0))
            atlantic_set.add((r, COLS - 1))
        
        for c in range(COLS):
            pacific_set.add((0, c))
            atlantic_set.add((ROWS - 1, c))

        def bfs(ocean):
            q = collections.deque(ocean)

            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()

                    for dr, dc in DIRS:
                        new_r, new_c = r + dr, c + dc

                        if min(new_r, new_c) < 0 or new_r == ROWS or new_c == COLS or (new_r, new_c) in ocean or heights[new_r][new_c] < heights[r][c]:
                            continue
                        
                        q.append((new_r, new_c))
                        ocean.add((new_r, new_c))
        
        bfs(pacific_set)
        bfs(atlantic_set)

        return list(pacific_set.intersection(atlantic_set))