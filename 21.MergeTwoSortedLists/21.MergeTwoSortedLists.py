# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#Assumptions 
# we r given the heads of Two Sorted linked lists
# we need to merge the two lists in one sorted list, by splicing the nodes of the two lists
#Return the head of the merged linked list.
#[1,2,3] [2,4,6]
        head = ListNode() #create a new node
        current = head # create a pointer and point it to head
        while list1 and list2 : # while both are not None
            if list1.val < list2.val:
                current.next = list1 # point current.next at list 1 current pointer
                list1 = list1.next #advance the list1 pointer
            else:
                current.next = list2 
                list2 = list2.next
            current = current.next # advance the current pointer at end of each loop
        current.next = list1 or list2 # point current.next at the list that is not no None
        return head.next # return head.next which points to the starting node