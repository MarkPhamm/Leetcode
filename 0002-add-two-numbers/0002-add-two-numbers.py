# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1_str = ""
        
        cur = l1
        while cur: 
            num1_str += str(cur.val)
            cur = cur.next
        
        num2_str = ""
        cur = l2
        while cur: 
            num2_str += str(cur.val)
            cur = cur.next
        
        sum = int(num1_str[::-1]) + int(num2_str[::-1])
        sum_list =list(str(sum)[::-1])
        
        dummy = ListNode(None)
        cur = dummy
        for str_sum in sum_list:
            new_node = ListNode(int(str_sum))
            cur.next = new_node
            cur = cur.next
        
        return dummy.next
        
