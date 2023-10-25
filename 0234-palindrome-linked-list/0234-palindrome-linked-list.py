# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast=slow=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        prev=None
        current=slow
        while current:
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        
        head1=head
        head2=prev
        while head1 and head2:
            if head1.val==head2.val:
                head1=head1.next
                head2=head2.next
            else:
                return False

        return True