# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        while (a != b):
            a = headB if not a else a.next
            b = headA if not b else b.next
        return a
#     def getIntersectionNode(self, head: ListNode, head3: ListNode) -> Optional[ListNode]:
        
#         c1 = get_size(head)
#         c2 = get_size(head3)
#         if c1>=c2:
#             d = c1-c2
#         else:
#             d = c2-c1

#         head1 = head
#         head2 = head3
#         ptr1 = head1
#         ptr2 = head2
#         x = 0

#         if c1>c2:
#             for i in range(d):
#                 ptr1 = ptr1.next
#         elif c2>c1:
#             for i in range(d):
#                 ptr2 = ptr2.next

#         while ptr1 is not None and ptr1.val != ptr2.val :
#             # print(ptr1.val,"    ",ptr2.val)
#     #         x = ptr1.data
#             ptr1 = ptr1.next
#             ptr2 = ptr2.next
#         if ptr1 is not None:
#             x = ptr1.val

#         return ptr1
            
# def get_size(head):
#     counter = 1
#     cur = head
#     while cur is not None:
#         cur = cur.next
#         counter += 1
#     return counter
    
    # def get_difference(headA,headB):
    #     c1 = get_size(headA)
    #     c2 = get_size(headB)
    #     if c1>=c2:
    #         d = c1-c2
    #     else:
    #         d = c2-c1
    #     return d
    
            
           