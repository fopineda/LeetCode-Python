# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        return self.helper(root,root)

    def helper(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False

        return (node1.val == node2.val) and self.helper(node1.right,node2.left) and self.helper(node1.left, node2.right)