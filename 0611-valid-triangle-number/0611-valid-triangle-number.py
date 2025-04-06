class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # the sum of any two sides of a triangle must be greater than the third side
        # the third side c must be less than the sum of a and b but also greater than their difference

        # First, sort the input array to arrange numbers in non-decreasing order
        nums.sort()
      
        # Initialize the answer and get the length of the array
        triangle_count, n = 0, len(nums)
      
        # Loop over each triple. For triangles, we just need to ensure that
        # the sum of the lengths of any two sides is greater than the length of the third side.
        for i in range(n - 2):  # The last two numbers are not needed as they are candidates for the longest side of the triangle
            for j in range(i + 1, n - 1):  # j is always after i
              
                # Find the index of the smallest number that is greater than
                # the sum of nums[i] and nums[j] using binary search.
                # This determines the right boundary of possible valid triangles.
                # We subtract 1 because bisect_left returns the index where we could insert the
                # number keeping the list sorted, but we want the last valid index.
                k = bisect_left(nums, nums[i] + nums[j], lo=j + 1) - 1
              
                # The count of triangles for this specific (i, j) pair is k - j
                # because any index between j and k (exclusive) can be chosen as the
                # third side of the triangle.
                triangle_count += k - j

        # Return the total count of triangles that can be formed
        return triangle_count