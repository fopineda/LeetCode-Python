# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        # base case 
        if not root: 
            return

        # Create an empty queue for level order traversal and add root to it
        queue = [root] 

        # initialize variables that'll take in the level items and ending results
        results = []
        level = []
        
        # normal Breadth First Search (BFS) algorithm
        while queue: 
            queueSize = len(queue)
            level = []
            # loop though queue to add each item into the level list.
            # at any point in the queue it'll have the all the items for that given nth level.
            # after it's done adding to the level list, it'll add the entire level list to results list
            while queueSize > 0:
                level.append(queue[0].val)
                node = queue.pop(0)
                
                # Enqueues left child 
                if node.left:
                    queue.append(node.left)
                    
                # Enqueues left child 
                if node.right:
                    queue.append(node.right)
                queueSize -= 1
            results.append(level)
            
        return results
            
        
            