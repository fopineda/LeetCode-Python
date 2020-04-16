# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        # rightPointer jumps ahead n times so that leftPointer and rightPointer are n nodes in between
        rightPointer = head
        for idx in range(n):
            if (rightPointer.next is None): # edge case: n is larger than the list's size return head
                if (idx == n-1): # deeper edge case: original head node is the node to be deleted
                    head = head.next
                return head
            else:
                rightPointer = rightPointer.next
               
        # leftPointer stays at head 
        # now both leftPointer and rightPointer will traverse the list one at a time until end of list
        leftPointer = head
        while rightPointer.next != None:
            leftPointer = leftPointer.next
            rightPointer = rightPointer.next
            
        leftPointer.next = leftPointer.next.next
            
        return head
    
    
    
# [1]
# 1

# output: []
# 1 -> ""


# [1,2]
# 2

# output: [2]
# 1 -> 2 -> ""


#      p   cur
# [1,2,3,4,5]
# n = 2
# output: [1,2,3,5]

# size: 
# 1,2,3,4,5

# n + 1 = 3