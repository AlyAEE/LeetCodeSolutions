# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: [ListNode]) -> bool:
# use a hash map to map alist node to its value, if the list node exists return True else False
        hash = {}
        while head:
            if head in hash:
                return True
            else:
                hash[head] = head.val
            head = head.next
# Using Two pointer, one slow and one fast, if the fast catches slow return True else false
        # fast = head
        # while fast and fast.next:
        #     head = head.next
        #     fast = fast.next.next
        #     if head is fast:
        #         return True
        # return False
