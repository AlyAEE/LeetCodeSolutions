# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # def binaryToDecimal(n):
        #     return int(n,2)
        decimal = ''
        while head:
            decimal += str(head.val)
            head = head.next
        return int(decimal,2)