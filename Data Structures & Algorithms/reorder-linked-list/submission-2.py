# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        newlist = []
        ans = []
        curr = head
        while curr:
            newlist.append(curr)
            curr = curr.next
        n = len(newlist)
        i = 0
        j = n-1
        while i < j:
            ans.append(newlist[i])
            ans.append(newlist[j])
            i += 1
            j -= 1
        if i == j:
            ans.append(newlist[i])
        for i in range(n-1):
            ans[i].next = ans[i+1]
        ans[n-1].next = None
        return
        