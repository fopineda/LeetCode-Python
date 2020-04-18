# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        head = ListNode()
        newList = head
        
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                newList.next = l1
                l1 = l1.next
            else:
                newList.next = l2
                l2 = l2.next
            newList = newList.next
        
        if l1 is not None:
            newList.next = l1
        if l2 is not None:
            newList.next = l2
            
        return head.next