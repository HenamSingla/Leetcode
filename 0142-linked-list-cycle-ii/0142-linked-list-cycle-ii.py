class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None

        slow = head
        fast = head

        # Phase 1: detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None  # no cycle

        # Phase 2: find cycle start
        slow=head
        while slow!=fast:
            slow=slow.next
            fast=fast.next

        return slow
