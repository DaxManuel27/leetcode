class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        newHead = prev
        if n == 1:
            newHead = newHead.next
        else:
            cur = newHead
            for i in range(n-2):
                cur = cur.next
            cur.next = cur.next.next

        curr, prev = newHead, None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
