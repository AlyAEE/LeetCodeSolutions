# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        reversehead = None #create a new list points to None
        while head:
            next_node = head.next #this will point to next node in the linked list
            head.next = reversehead # this will point the current head to the reversehead
            reversehead = head  # update the reversehead to point at the current head
            head = next_node # point head to the next node
        return reversehead
