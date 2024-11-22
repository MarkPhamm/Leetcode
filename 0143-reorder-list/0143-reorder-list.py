# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        cur = head
        arr = []
        while cur:
            arr.append(cur)
            n = cur.next
            cur.next = None
            cur = n
        
        l = 0
        r = len(arr)-1
        print(len(arr))

        while l<r:
            n = arr[l+1]
            if n == arr[r]:
                arr[l].next = arr[r]
            else: 
                arr[l].next = arr[r]
                arr[r].next = n
            l+=1
            r-=1
        