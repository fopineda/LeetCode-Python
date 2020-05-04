# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        results = []
        pathString = ""
        # calls recursive pre-order traversal (Root->Left->Right) on the tree
        self.preOrderTraversal(root, results, pathString)
        return results
        
        
    def preOrderTraversal(self, root, results, pathString):
        if not root:
            return
        
        # everytime it visits an exisiting node (root), it will add that value to the path string
        # after it will traverse the tree in a left to right fashion
        pathString += str(root.val) + "->"
        left = self.preOrderTraversal(root.left, results, pathString)
        right = self.preOrderTraversal(root.right, results, pathString)
        
        
        # Once it gets to the bottom of the tree, if the node doesn't have a left or right then it is a leaf and append the pathstring
        # It checks for both left and right as some nodes may have a left but not right and vice verse.
        # The string splicing is there because I'm lazy to add logic to line 27. It adds an additional "->" at the end lol
        if not root.left and not root.right:
            results.append(pathString[0:-2])