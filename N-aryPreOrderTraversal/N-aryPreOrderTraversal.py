"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        results = []
        self.preOrderTraversal(root, results)
        return results
    
    def preOrderTraversal(self, root, results):
        if not root:
            return
        
        results.append(root.val)
        for child in root.children:
            self.preOrderTraversal(child, results)