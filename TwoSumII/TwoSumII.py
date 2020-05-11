class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        numDict = {}
        for i,x in enumerate(numbers):
            if x in numDict:
                return [numDict[x]+1, i+1]
            else:
                numDict[(target-x)] = i