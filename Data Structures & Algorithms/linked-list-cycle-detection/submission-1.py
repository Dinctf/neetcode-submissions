# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        if not fast or not fast.next:
            return False
        slow2=head
        while slow!=slow2:
            slow=slow.next
            slow2=slow2.next
            if slow==slow2:
                return True 
        return False
        
        