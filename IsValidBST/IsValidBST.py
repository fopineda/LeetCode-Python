# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def helper(root, lower, upper):
            if not root:
                return True
            
            rootValue = root.val
            if rootValue <= lower or rootValue >= upper:
                return False
            
            # going in the right direction so the root value must be the lower
            # if not "false" will make it go inside the if condition
            if not helper(root.right, rootValue, upper):
                return False
            
            # going in the left direction so the root value must be the upper
            # if not "false" will make it go inside the if condition
            if not helper(root.left, lower, rootValue):
                return False
            
            # ran through the entire BST and found no issues
            return True
        
        # calling the nested function...
        lower = float('-inf')
        upper = float('inf')
        return helper(root, lower, upper)