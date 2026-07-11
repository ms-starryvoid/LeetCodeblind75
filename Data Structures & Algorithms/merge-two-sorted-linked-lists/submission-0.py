# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1=list1
        l2=list2
        if not l1 and not l2:
            return l1
        if not l2:
            return l1
        if not l1:
            return l2
        if l1.val<l2.val:
            head=l1
            l1=l1.next
        else:
            head=l2
            l2=l2.next
        p=head
        while l1 and l2:
            if l1.val<l2.val:
                nxt=l1.next
                nxt2=p.next
                p.next=l1
                l1.next=nxt2
                l1=nxt
                p=p.next
            else:
                nxt=l2.next
                nxt2=p.next
                p.next=l2
                l2.next=nxt2
                l2=nxt
                p=p.next
        if l1:
            while l1:
                p.next=l1
                p=p.next
                l1=l1.next
        if l2:
            while l2:
                p.next=l2
                p=p.next
                l2=l2.next
        return head
