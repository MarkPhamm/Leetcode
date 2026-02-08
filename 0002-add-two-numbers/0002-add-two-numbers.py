# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            ## brute force
            l1_list = []
            l2_list = []

            while l1:
                l1_list.append(l1.val)
                l1 = l1.next 
            
            while l2:
                l2_list.append(l2.val)
                l2 = l2.next
            
            num1 = 0
            for x in reversed(l1_list):
                num1 = num1 * 10 + x

            
            num2 = 0
            for x in reversed(l2_list):
                num2 = num2 * 10 + x

            total = num1+num2  
            
            dummy = ListNode()
            cur = dummy

            for digit in str(total)[::-1]:
                cur.next = ListNode(int(digit))
                cur = cur.next
        
            return dummy.next 

