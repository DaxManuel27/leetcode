# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True
        def height(curr):
            if not curr:
                return 0 
            left = height(curr.left)
            right = height(curr.right)
            diff = left - right
            if diff != 0 and diff != -1 and diff != 1:
                self.isBalanced = False
            return 1 + max(left, right)
        height(root)
        return self.isBalanced
