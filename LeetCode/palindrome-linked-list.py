# https://leetcode.com/problems/palindrome-linked-list/

# solution 1 (652ms)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        rev = None
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
            
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
            
        return not rev

# solution 2 (824ms)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        ls = []
        
        current_node = head
        current_val = current_node.val
        ls.append(current_val)
        
        while current_node.next != None:
            current_node = current_node.next
            ls.append(current_node.val)
            
        if ls == ls[::-1]:
            return True
        else:
            return False
