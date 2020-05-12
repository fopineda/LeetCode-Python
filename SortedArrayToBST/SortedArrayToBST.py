# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        
        # initial root will exist in the middle of the array
        # elements to the left in the array (less than root) will be left in the tree
        # elements to the right in the array (greater than the root) will be right in the tree
        rootIndex = len(nums) / 2
        
        # once it goes into its recursive calls, this will be creating the node objects for each element
        root = TreeNode(nums[rootIndex])
        
        # set the left of the current element to the results of the recursive call
        # The left side of the array is sent into the recursive call as the new nums array
        root.left = self.sortedArrayToBST(nums[0:rootIndex])
        
        # set the right of the current element to the results of the recursive call
        # The right side of the array is sent into the recursive call as the new nums array
        root.right = self.sortedArrayToBST(nums[rootIndex+1:])
        
        # [-10, -3, 0, 5, 9]
        # root: 0
        # left: [-10, -3] <- recurse in to out so -3 then -10
        # right: [5, 9] <- recurse out to in so 9 then 5
        
        #.              |
        # [-10, -3, -1, 0, 5, 9, 10]
        # root: 0
        #.             |
        # left: [-10, -3, -1] <- root will be -3 and its left will be -10 and right -1
        #.           |
        # right: [5, 9, 10] <- root will be 9 and its left will be 9 and right 10
        
        # it initially finds the root (middle) of the given array and then in the future recursive call it finds the roots of the left and right sub arrays and so on
        # please reference above examples
        
        return root