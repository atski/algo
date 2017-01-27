#see https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        curr = result
        carry = 0
        while(l1 != None or l2 != None):
            val = (l1.val if l1 != None else 0) + (l2.val if l2 != None else 0) + carry
            carry = val / 10
            
            curr.next = ListNode(val % 10)
            curr = curr.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        if carry > 0: 
            curr.next = ListNode(1)
                            
        return result.next
