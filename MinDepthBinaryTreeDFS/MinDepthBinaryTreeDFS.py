# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        currentDepth = 1
        depthList = []
        # helper function traverses the tree and returns all depth counts in a list
        self.helper(root, currentDepth, depthList)
        # depthList has all depth counts taken every time the traversal algorithm hits a leaf
        return min(depthList)
        
        
    def helper(self, root, currentDepth, depthList):
        if not root:
            return
        
        # condition for leaf nodes, otherwise keep traversing down
        # append the current depth to the depthList every time the traversal reaches a leaf
        if not root.left and not root.right:
            depthList.append(currentDepth)
            
        self.helper(root.left, currentDepth+1, depthList)
        self.helper(root.right, currentDepth+1, depthList)
        
        