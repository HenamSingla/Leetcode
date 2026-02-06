# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # print(head)
        # arr=[head]
        # while arr[-1].next:
        #     arr.append(arr[-1].next)
        # print(arr)
        # return arr[len(arr)//2]
        # #time and space: O(n)

        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        return slow
        #time: O(n) amd Space: O(1)



        