# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        results = []
        self.traversal(root, results)
        return results
    
    # function that recursively visits children in order left (append it), parent (append it) and lastly right (append it)
    # a little different from N-ary Traversals as this problem allows the tree to have a ".right" and a ".left"
    # N-ary traversals, at least by LeetCode standards, had ".children" instead of the common left and right options
    def traversal(self, root, results):
        if not root:
            return
        
        self.traversal(root.left, results)
        results.append(root.val)
        self.traversal(root.right, results)