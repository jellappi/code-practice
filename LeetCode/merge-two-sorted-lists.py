# https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if not l1:
            return l2
        if not l2:
            return l1
        
        l1_ls = [l1.val]
        current_l1 = l1
        while current_l1.next:
            current_l1 = current_l1.next
            l1_ls.append(current_l1.val)
            
        l2_ls = [l2.val]
        current_l2 = l2
        while current_l2.next:
            current_l2 = current_l2.next
            l2_ls.append(current_l2.val)
            
        merge = l1_ls + l2_ls
        merge.sort()
        
        node_list = ListNode(merge[0])
        current_node = node_list
        for v in merge[1:]:
            current_node.next = ListNode(v)
            current_node = current_node.next
            
        return node_list
