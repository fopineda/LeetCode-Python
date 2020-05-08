class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        target_indices = []
        index_dict = {}
        for i in range(0, len(nums)):
            index_dict[nums[i]] = i
            
        for j in range(0, len(nums)):
            complement = target - nums[j]
            if ((complement in index_dict) and (index_dict.get(complement) != j)):
                target_indices.append(j)
                target_indices.append(index_dict.get(complement))
                break
        return target_indices
       