# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0
        
        currentDepth = 1
        depthList = [currentDepth]
        self.helper(root, currentDepth, depthList)
        
        # at this point, the list will have all the depths taken every time the traversal hit a leaf. Just take the max of it
        return max(depthList)
        
    def helper(self, root, currentDepth, depthList):
        
        if not root:
            return
        
        # condition for leaf nodes, otherwise keep traversing down
        # append the current depth to the depthList every time the traversal reaches a leaf
        # calling this the leaf finder traversal lol although it sort of similar to pre-order traversal
        if not root.left and not root.right:
            depthList.append(currentDepth)
            
        self.helper(root.left, currentDepth+1, depthList)
        self.helper(root.right, currentDepth+1, depthList)
        
        
                
        
        