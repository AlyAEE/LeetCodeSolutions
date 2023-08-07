class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
# This Solves the problem in Time complexity O(n*n) and space complexity O(1)
#        for i in range(len(nums)):
#           for j in range(i+1,len(nums)):
#                if nums[i] + nums[j] == target:
#                    return [i,j]
# hash tables solves the problem in time complexity O(n) and space complexity O(n)          
        dict = {}
        for index , value in enumerate(nums):
            diff = target - nums[index]
            
            if diff in dict :
                output = [index, dict[diff]]
                output.sort()
                return output
            else:
                dict[value] = index                      