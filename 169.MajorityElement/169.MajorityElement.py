class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
# assumptions
# majority element appears more than n / 2 times
# since majority element always exist we can assume it is the most frequent no. in the list

# First Solution
# Get the unique numbers in the list, then get the number with the most frequent appearances

#       unique_nums = set(nums)
#       return max(unique_nums, key=nums.count)

# Second Solution
# using a hash map {'no.' : count} and the return the value with the highest count

#       count = {}
#        maxNum = 0
#        maxCount = 0
#        for num in nums:
#            count[num] = 1 + count.get(num,0) 
#            if count[num] > maxCount:
#                maxNum = num
#            maxCount = max(count[num], maxCount)
#        return maxNum

# Third Solution
# using Boyer Moore Algorithm 
        count = 0
        maxNum = 0
        for num in nums:
            if count == 0:
                maxNum = num
            if num == maxNum:
                count += 1
            else:
                count -= 1
        return maxNum