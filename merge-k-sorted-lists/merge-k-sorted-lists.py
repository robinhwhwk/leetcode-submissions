# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # intuition: merge sort
        # divide and conquer
        # divide list into half
        # merge 
        if not lists:
            return
        elif len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            list1, list2 = lists[0], lists[1]
            if not list1:
                return list2
            if not list2:
                return list1
            temp = list1
            if list1.val <= list2.val:
                list1 = list1.next
            else:
                temp = list2
                list2 = list2.next
            curr = temp
            while list1 and list2:
                if list1.val <= list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next
            if list1:
                curr.next = list1
            if list2:
                curr.next = list2
            return temp
        else:
            # divide array into 2 halves: left, right
            # recurse on both
            mid = len(lists) // 2
            list1 = lists[:mid]
            list2 = lists[mid:]
            left = self.mergeKLists(list1)
            right = self.mergeKLists(list2)
            return self.mergeKLists([left, right])

