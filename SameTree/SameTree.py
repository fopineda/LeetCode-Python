# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        # Solution completes a pre-order traversal on both trees. The traversal should append elements (None if empty) in the tree to its appropriate list.
        # After the traversals are done, then compare the lists. 
        # If lists are same, the then trees are the same as well. If lists are different, then the trees are different
        nodesP = []
        nodesQ = []
        self.preOrderTraversal(p, nodesP)
        self.preOrderTraversal(q, nodesQ)
        return nodesP == nodesQ
    
    def preOrderTraversal(self, root, nodes):
        if not root:
            nodes.append(None)
            return
        nodes.append(root.val)
        self.preOrderTraversal(root.left, nodes)
        self.preOrderTraversal(root.right, nodes)
        