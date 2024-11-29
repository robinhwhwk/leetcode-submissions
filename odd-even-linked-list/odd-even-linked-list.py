# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        index = 0
        curr = head
        odd = head
        even = head.next
        even_head = even;
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            if even:
                even = even.next
        odd.next = even_head
        return head

        



