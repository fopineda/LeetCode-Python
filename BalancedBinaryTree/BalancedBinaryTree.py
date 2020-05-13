# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root) != -1
        
    def helper(self,root):
        if not root:
            return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        if left == -1 or right == -1 or (abs(left-right) > 1):
            return -1
        
        return 1 + max(left, right)