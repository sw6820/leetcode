# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy=ListNode(-1)
        dummy.next=head
        c=dummy        
        while c.next!=None:
            if c.next.val==val:
                c.next=c.next.next
            else:
                c=c.next
        return dummy.next
        