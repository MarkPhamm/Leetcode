# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = l1
        str1 = ""
        while cur:
            str1 += str(cur.val)
            cur = cur.next
        
        cur = l2
        str2 = ""
        while cur:
            str2 += str(cur.val)
            cur = cur.next
        
        sum_list = list(str(int(str1[::-1])  + int(str2[::-1])))[::-1]
        
        head = ListNode(int(sum_list[0]))
        cur = head

        for i in range(1, len(sum_list)):
            cur.next = ListNode(int(sum_list[i]))
            cur = cur.next
        
        return head
        