# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        ans = []
        if n == 0:
            return None
        if n == 1:
            return lists[0]
        for i in range(n):
            curr = lists[i]
            ans.append(curr.val)
            while curr.next:
                curr = curr.next
                ans.append(curr.val)
        ans = sorted(ans)
        #print(ans)
        head = ListNode(ans[0])
        curr = head
        for i in range(1, len(ans)):
            curr.next = ListNode(ans[i])
            curr = curr.next
        return head