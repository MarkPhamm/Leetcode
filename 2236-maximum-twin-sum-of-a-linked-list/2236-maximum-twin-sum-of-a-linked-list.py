# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dummy = ListNode(None, head)
        cur = dummy.next

        count = 0
        while cur:
            cur = cur.next
            count+=1

        middle = (count+1)/2
        
        index = 1
        array1 = []
        array2 = []
        dummy = ListNode(None,head)
        cur = dummy.next
        while cur:
            if index < middle:
                array1.append(cur.val)
            elif index > middle:
                array2.append(cur.val)
            cur = cur.next
            index +=1
        
        array2 = array2[::-1]

        ans = []
        for i in range(len(array1)):
            ans.append(array1[i]+array2[i])
        
        print(array1, array2)
        return max(ans)






        