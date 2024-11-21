# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        count = 0
        while cur:
            count +=1
            cur = cur.next
        
        index = ceil((count+1)/2)
        print(index)
        
        count = 1
        c = head
        while c:
            if count == index:
                return c 
            count +=1 
            c = c.next
        

        
        