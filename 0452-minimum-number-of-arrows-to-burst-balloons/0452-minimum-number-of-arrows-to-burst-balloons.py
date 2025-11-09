class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        B  BBB
          B  B
        BB   B
             A           

        Input: points = [[10,16],[2,8],[1,6],[7,12]]
        [[1,6],[2,8],[7,12],[10,16]]
        [[1,6],[7,12]]

        Input: points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
        [[1, 10], [3, 9], [4, 11], [6, 7], [6, 9], [8, 12], [9, 12]]
        [[1, 7], [8, 12]]

        Approach:
            - sort the list by starting x positions
            - iterate over each interval and build a new array called non_olapping
            - before you add to it, check if non_olapping[-1] overlaps with the current interval
            - if so, keep the smaller end x position of the two 
                - keeping the larger one means we lose the guarantee that the balloon w/ smaller one gets hit
            - return the length of non_olapping, this is the number of arrows we need
        """
        points.sort(key=lambda pair : pair[0])
        non_olapping = []

        for start, end in points:
            if non_olapping and start <= non_olapping[-1][1]:
                non_olapping[-1][1] = min(end, non_olapping[-1][1])
            else:
                non_olapping.append([start, end])
        
        return len(non_olapping)