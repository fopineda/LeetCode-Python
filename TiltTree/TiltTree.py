# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0
        
        tilt = [0]
        self.postOrderTraversal(root, tilt)
        print(tilt)
        return tilt[0]
        
        
    def postOrderTraversal(self, root, tilt):
        if not root:
            return 0
        
        leftNum = self.postOrderTraversal(root.left, tilt)
        rightNum = self.postOrderTraversal(root.right, tilt)
        # print(leftNum, rightNum, root.val)
        tilt[0] += abs(leftNum - rightNum)
        return root.val + leftNum + rightNum