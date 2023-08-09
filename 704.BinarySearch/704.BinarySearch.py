class Solution:
    def search(self, nums, target):

# since numbers are unique and numbers are sorted , we will solve this proplem using binary search
# divide the list into subsets, if num in the middle return, else if it is higher search in the right part of the array and vice versa

        low = 0
        high = len(nums) -1
        mid = 0
        if len(nums) == 1 and nums[0] == target:
            return 0
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid -1
        return -1
                
