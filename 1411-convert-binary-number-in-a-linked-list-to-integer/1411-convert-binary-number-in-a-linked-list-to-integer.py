# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0
        cur = head
        count = 0
        while cur:
            count +=1
            cur = cur.next
        
        cur = head
        ans = 0
        while cur:
            ans += cur.val * (2**(count-1))
            cur = cur.next
            count -=1
        
        return ans

        