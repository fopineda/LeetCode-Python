class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        
        # first array had larger numbers, meaning they were moved to end and the start was untouched
        # second array either was never "touched" (decremented) or was barely, hence the
        # splicing up to n
        # ex: nums1: [4,5,6,0,0,0]
        #     m = 3
        #     nums2 = [1,2,3]
        #     n = 3
        if n > 0: 
            nums1[:n] = nums2[:n]
            
