# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        
        # if we get to a left and right where a node is null, then return the non-null node
        if not t1:
            return t2
        
        if not t2:
            return t1
        
        # sum the nodes if both are present and set it back to t1
        t1.val += t2.val
        # recurse through the left first and then right
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
    
        
        