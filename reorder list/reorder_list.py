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
        i=head
        j=head.next
        while j and j.next:
            i=i.next
            j=j.next.next
        half=i.next
        i.next=None
        prev=None
        while half:
            temp=half.next
            half.next=prev
            prev=half
            half=temp
        f=head
        s=prev
        while s:
            temp1=f.next
            temp2=s.next
            f.next=s
            s.next=temp1
            f=temp1
            s=temp2