# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(None, head)
        cur = dummy.next
        
        length = 0
        while cur:
            length +=1
            cur = cur.next
        
        middle = (length-1)/2

        stack = []
        cur = dummy.next 
        index = 0
        
        while cur: 
            if index < middle:
                stack.append(cur.val)
            elif index > middle:
                if stack[-1] == cur.val:
                    stack.pop()
            cur = cur.next 
            index +=1
        
        return len(stack)==0