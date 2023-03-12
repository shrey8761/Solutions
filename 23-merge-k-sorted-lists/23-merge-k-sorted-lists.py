def merge_two_lists(l1, l2):
    head = None
    point = head
    while l1 != None and l2 != None:
        temp = ListNode()
        if l1.val > l2.val:
            temp.val = l2.val
            l2 = l2.next
        else:
            temp.val = l1.val
            l1 = l1.next
        temp.next = None
        if head is None:
            head = temp
            point = head
        else:
            point.next = temp
            point = point.next

    while l1 != None:
        if head is None:
            head = ListNode(l1.val, None)
            point = head
        else:
            point.next = l1
            point = point.next
        l1 = l1.next

    while l2 != None:
        if head is None:
            head = ListNode(l2.val, None)
            point = head
        else:
            point.next = l2
            point = point.next
        l2 = l2.next
    return head

def mergeAll(s, k , lists):
    if s == k:
        return lists[s]
    if s + 1 == k:
        return merge_two_lists(lists[s], lists[k])
    mid = (s + k) // 2
    l1 = mergeAll(s, mid, lists)
    l2 = mergeAll(mid + 1, k, lists)
    return merge_two_lists(l1, l2)

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        else:
            return mergeAll(0, len(lists) - 1, lists)