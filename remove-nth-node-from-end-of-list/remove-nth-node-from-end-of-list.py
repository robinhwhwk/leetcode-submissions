# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # intution:
        # count number of nodes: sz
        # edge case:
        # if n == number of nodes (i.e. nth node is last node.)
        # then return head
        fast = head
        slow = head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        # at this point, fast is null, slow is at n-1th node
        if not slow.next:
            return head
        slow.next = slow.next.next
        return head