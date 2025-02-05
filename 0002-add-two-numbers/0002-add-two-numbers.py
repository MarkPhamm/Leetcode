# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 342 + 465 = 807
        # Idea: create a carry variable
        # Step 1: carry will be the sum of the current index of l1 and l2
        # Step 2: traverse l1 and l2
        # Step 3: update next node = carry % 10, update cur node = cur.next
        # Step 4: update carry = carry // 10
        dummy = cur = ListNode()
        carry = 0

        while l1 != None or l2!= None or carry != 0:
            if l1 != None:
                carry += l1.val
                l1 = l1.next
            if l2 != None:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10
        return dummy.next




        