# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t=0
        rst=ListNode()
        ans=rst
        while l1 and l2:
            q,r = divmod(l1.val+l2.val+t,10) 
            t=q
            rst.next=ListNode(r)
            rst=rst.next
            l1=l1.next
            l2=l2.next
        while l1:
            q,r = divmod(l1.val+t,10)
            t=q
            rst.next=ListNode(r)            
            l1=l1.next
            rst=rst.next
        while l2:
            q,r = divmod(l2.val+t,10)
            t=q
            rst.next=ListNode(r)            
            l2=l2.next  
            rst=rst.next
        if t:
            rst.next=ListNode(t)
        return ans.next
            