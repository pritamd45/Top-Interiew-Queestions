# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode(0)
        curr=head
        sum1=0
        sum2=0
        i=0
        while l1.next!=None:
            mul=10**i
            sum1=l1.val*mul+sum1
            l1=l1.next
            i+=1
        sum1=sum1+l1.val*(10**(i))
        j=0
        while l2.next!=None:
            mul=10**j
            sum2=l2.val*mul+sum2
            l2=l2.next
            j+=1
        sum2=sum2+l2.val*(10**(j))
        print(sum1,sum2)
        total=sum1+sum2
        total=str(total)
        i=len(total)-1
        while i>=0:
            newNode=ListNode(int(total[i]))
            curr.next=newNode
            curr=newNode
            i-=1
        return head.next