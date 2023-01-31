from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
        https://leetcode.com/problems/merge-two-sorted-lists/
        https://leetcode.com/problems/merge-two-sorted-lists/solutions/3085869/easy-solution-explained-and-visualization/
        
        You are given the heads of two sorted linked lists list1 and list2.

        Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

        Return the head of the merged linked list.
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2

        elif list2 is None:
            return list1

        dummy = ListNode()
        pointer = dummy

        # if None in [list1, list2], break loop
        while list1 and list2:
            if list1.val < list2.val:
                pointer.next = list1
                list1 = list1.next
            else:
                pointer.next = list2
                list2 = list2.next

            pointer = pointer.next

        # then list1 is not None, next -> list1. list2 vice versa
        if list1:
            pointer.next = list1
        else:
            pointer.next = list2

        # why is the dummy updated?
        return dummy.next 
