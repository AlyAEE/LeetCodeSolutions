# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: [ListNode]) -> [ListNode]:\
        # we will need two pointers one slow and one fast, when the fast reaches the End the slow will be at the middle
        fast = head
        while fast and fast.next:
            head = head.next
            fast = fast.next.next
        return head