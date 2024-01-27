# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #start a list with no previous 
        previous = None
        current = head #curent one as  a list

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous