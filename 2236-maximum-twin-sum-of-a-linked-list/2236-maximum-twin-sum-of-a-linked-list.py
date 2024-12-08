# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dummy = ListNode(None, head)
        fast = dummy.next
        slow = dummy.next

        stack = []

        while fast and fast.next:
            fast = fast.next.next
            stack.append(slow.val)
            slow = slow.next
        
        ans = 0
        while slow:
            current_sum = stack.pop() + slow.val
            ans = max(current_sum, ans)
            slow = slow.next
        
        return ans




        