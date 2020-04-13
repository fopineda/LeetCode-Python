class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        result = []
        uniqueDict = {}
        nums1Length = len(nums1)
        nums2Length = len(nums2)
        
        ## want to do the smallest list to make sure we looping process is as small as possible
        if nums1Length < nums2Length:
            for number in nums1:
                if number in nums2:
                    result.append(number)
                    nums2.remove(number)
        else:
            # nums2 list is either smaller than nums1 or they are equal length
            for number in nums2:
                if number in nums1:
                    result.append(number)
                    nums1.remove(number)
  
        return result