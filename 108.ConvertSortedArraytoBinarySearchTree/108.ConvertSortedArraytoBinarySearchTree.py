# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
# Assumptions
# since we r given a SortedArray, We can set the middle number as the root Node and use Binary search to set elements left and right

        if not nums :
            return None
        mid = len(nums) // 2

        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node
# time complexity is O(n) and space complexity is O(n)