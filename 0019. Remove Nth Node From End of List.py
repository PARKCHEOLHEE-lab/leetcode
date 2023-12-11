from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
        https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
        
        Given the head of a linked list, remove the nth node from the end of the list and return its head.

        Example 1:
            Input: head = [1,2,3,4,5], n = 2
            Output: [1,2,3,5]

        Example 2:
            Input: head = [1], n = 1
            Output: []

        Example 3:
            Input: head = [1,2], n = 1
            Output: [1]

        Constraints:
            The number of nodes in the list is sz.
            1 <= sz <= 30
            0 <= Node.val <= 100
            1 <= n <= sz
            
        Reference:
            https://leetcode.com/problems/remove-nth-node-from-end-of-list/solutions/3668568/python-beginner-friendly-solution-with-explanation/
    """
    
    def getListLength(self, head: Optional[ListNode]):
        list_node_length = 0
        cursor_for_length_calculating = head
        
        while cursor_for_length_calculating:
            list_node_length += 1
            cursor_for_length_calculating = cursor_for_length_calculating.next
        
        return list_node_length
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        target_index = self.getListLength(head) - n
        if target_index == 0:
            return head.next

        # Set this below cursor to be just before the target list node
        nth_removed_cursor = head
        
        while target_index > 1:
            nth_removed_cursor = nth_removed_cursor.next
            target_index -= 1   
            
        nth_removed_cursor.next = nth_removed_cursor.next.next

        return head    
    
    
if __name__ == "__main__":
    removed = Solution().removeNthFromEnd(
        head=ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5, next=ListNode(val=6, next=ListNode(val=7, next=None))))))), 
        n=3
    )