class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
# First Solution       
#        if len(set(nums)) < len(nums):
#            return True
#        else:
#            return False
#second Solution        
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]: 
                return True
        return False            