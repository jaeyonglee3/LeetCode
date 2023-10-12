# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Recursive solution:
        # In order traversal to save elements to list
        # least_to_greatest = self.inorderTraversal(root)
        # return least_to_greatest[k - 1]
    
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     if not root:
    #         return []

    #     return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

        # Iterative solution 
        # start at root
        num_visited = 0  # to keep track of the number of elements visited
        stack = []
        curr = root

        # while curr is not null or stack != []:
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()  # once while loop finishes, curr is null (too far left), so pop last element added to stack
            num_visited += 1

            if num_visited == k:  # will always execute b/c we are guaranteed k nodes in the tree
                return curr.val
            
            curr = curr.right


