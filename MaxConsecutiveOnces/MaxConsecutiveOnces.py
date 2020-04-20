class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """   
        count = 0
        countList = []
        for num in nums:
            if num == 1:
                count += 1
            else:
                countList.append(count)
                count = 0
        countList.append(count)
        return max(countList)