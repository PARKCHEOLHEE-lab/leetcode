# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
        https://leetcode.com/problems/add-two-numbers/

        You are given two non-empty linked lists representing two non-negative integers. 
        The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

        You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    """

    def _convertToIntger(self, list_node):

        list_node_cursor = list_node
        list_node_string = ""
        while list_node_cursor is not None:
                        
            list_node_string += str(list_node_cursor.val) 
            list_node_cursor = list_node_cursor.next if list_node_cursor is not None else None

        return int(list_node_string[::-1])

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l1_num = self._convertToIntger(l1)
        l2_num = self._convertToIntger(l2)

        l1_l2_addition = l1_num + l2_num
        l1_l2_addition_list = [int(str_num) for str_num in str(l1_l2_addition)[::-1]]

        node_list = []
        for each_val in l1_l2_addition_list:
            node_list.append(ListNode(each_val))
        
        for ni in range(len(node_list) - 1):
            node_list[ni].next = node_list[ni + 1]

        return node_list[0]