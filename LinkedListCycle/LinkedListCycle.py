# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """    
        
        if head is None or head.next is None:
            return False
        
        
        pointer = head
        visted = set()
        while pointer is not None:
            if pointer in visted:
                return True
            else:
                visted.add(pointer)
            pointer = pointer.next
        
        return False


    
            
        