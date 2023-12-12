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
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        cursor_1 = list1
        cursor_2 = list2
        
        merged = ListNode()
        dummy = merged

        while cursor_1 or cursor_2:
            
            if cursor_1 is None:
                dummy.next = cursor_2
                break
            elif cursor_2 is None:
                dummy.next = cursor_1    
                break

            if cursor_1.val <= cursor_2.val:
                dummy.next = cursor_1
                cursor_1 = cursor_1.next

            else:
                dummy.next = cursor_2
                cursor_2 = cursor_2.next
            
            dummy = dummy.next
            
        return merged.next


if __name__ == "__main__":
    list1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4, next=None)))
    list2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4, next=None)))
    
    Solution().mergeTwoLists(list1, list2)