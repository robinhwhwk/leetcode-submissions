# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryOver = 0
        head = ListNode()
        curr = head
        prev = head

        while l1 or l2:
            if l1 and l2:
                digit = (l1.val + l2.val + carryOver) % 10
                if l1.val + l2.val + carryOver > 9:
                    carryOver = 1
                else:
                    carryOver = 0
                l1 = l1.next
                l2 = l2.next
            elif l1:
                digit = (l1.val + carryOver) % 10
                if l1.val + carryOver > 9:
                    carryOver = 1
                else:
                    carryOver = 0
                l1 = l1.next
            elif l2:
                digit = (l2.val + carryOver) % 10
                if l2.val + carryOver > 9:
                    carryOver = 1
                else:
                    carryOver = 0
                l2 = l2.next
            prev = curr
            curr = ListNode(digit)
            prev.next = curr

        if carryOver:
            curr.next = ListNode(1)
        return head.next

            
        