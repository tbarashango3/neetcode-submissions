# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        newlist = []
        curr = head
        while curr:
            newlist.append(curr)
            curr = curr.next
        #print(newlist)
        n = len(newlist)
        orderedlist = [0] * n
        for i in range(n):
            if (i * 2) < n:
                orderedlist[i*2] = newlist[i]
                #print("lower: ", i)
        for i in range(n - 1, 0, -1):
            if (i * 2) >= n:
                #print("higher: ", i)
                orderedlist[(n - i - 1) * 2 + 1] = newlist[i]
        m = len(orderedlist)
        for i in range(m-1):
            orderedlist[i].next = orderedlist[i+1]
        orderedlist[m-1].next = None
        #print(orderedlist[0].val)
        return

        