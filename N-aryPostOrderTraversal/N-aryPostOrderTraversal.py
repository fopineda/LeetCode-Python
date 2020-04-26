"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        results = []
        self.postOrderTraversal(root, results)
        return results
        
    def postOrderTraversal(self, root, results):
        if not root:
            return
        
        # It'll loop through all children of the current node starting at left then right
        # If node is a leaf (no children), then it won't start the loop and just append the value
        # Eventually it'll jump back to the parent/root to append the value, but only after it's visited its children
        for child in root.children:
            self.postOrderTraversal(child, results)
        results.append(root.val)
        
        