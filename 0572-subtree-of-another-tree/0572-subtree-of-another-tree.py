# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # brute force approach
        # dfs on the root tree 
        # check root, left, and right to see if they are the same

        # implementing solution
        # check first if root and subRoot are the same tree
        # check if subRoot is a subtree of the left subtree by calling sametree fn on left subtree

        # Edge cases
        # - both trees are null, then yes they're same tree
        # - 2 trees have same root, left, right, but one of them is taller, then not same tree
        # - is root was null but subRoot was non empty, subRoot is not a subtree of root
        # - is an empty subRoot tree a subtree of a non empty root? Yes (good clarification question for interview)

        # Two of our edge cases
        if not subRoot: return True
        if not root: return False
        
        if self.sameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))

    def sameTree(self, root, subRoot):
        # Alternate implementation of sameTree from Neetcode Video
        # if not root and not subRoot:
        #     return True

        # # if both non-empty, we compare the trees
        # if root and subRoot and root.val == subRoot.val:
        #     return (self.sameTree(root.left, subRoot.left) and 
        #             self.sameTree(root.right, subRoot.right))
        
        # return False  # One tree is empty while the other isn't, so return False

        # Original implementation of sameTree by me from lc #100
        if not root and not subRoot: return True
        if not root or not subRoot: return False
        if root.val != subRoot.val: return False

        return (self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right))

        