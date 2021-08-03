# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def transform_int(node: ListNode) -> int:

    current_node = node
    string = ''

    while current_node:
        string = str(current_node.val) + string
        current_node = current_node.next

    return int(string)


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
#         current_l1 = l1
#         current_l2 = l2
        
#         l1_str = ''
#         l2_str = ''
        
#         while current_l1:
#             l1_str = str(current_l1.val) + l1_str
#             current_l1 = current_l1.next            
            
#         while current_l2:
#             l2_str = str(current_l2.val) + l2_str
#             current_l2 = current_l2.next          
            
        l1_int = transform_int(node=l1)
        l2_int = transform_int(node=l2)
            
        result = l1_int + l2_int
        result_str = str(result)
        
        rev = None
        for c in result_str:
            rev, rev.next = ListNode(val=c), rev
            
        return rev

