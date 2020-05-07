# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        head = point = ListNode(0)
        list1 = []
        list2 = []
        while l1:
            list1.append(str(l1.val))
            l1 = l1.next
        while l2:
            list2.append(str(l2.val))
            l2 = l2.next
        
        #reverse the lists
        list1 = list1[::-1]
        list2 = list2[::-1]
        str1 = "".join(list1)
        str2 = "".join(list2)
        int1 = int(str1)
        int2 = int(str2)
        finalInt = int1 + int2
        finalIntStr = str(finalInt)
        for i in finalIntStr[::-1]:
            point.next = ListNode(i)
            point = point.next
        return head.next
        