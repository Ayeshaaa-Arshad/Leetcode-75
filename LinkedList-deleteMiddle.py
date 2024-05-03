class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None

        slowPtr = head
        fastPtr = head
        prevPtr = None

        while fastPtr and fastPtr.next:
            prevPtr = slowPtr
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next

        if prevPtr:
            prevPtr.next = slowPtr.next
        else:
            head = slowPtr.next

        return head
