class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def pairSum(self, head):
        values = []
        while head:
            values.append(head.val)
            head = head.next

        max_sum = 0
        n = len(values)
        for i in range(n // 2):
            max_sum = max(max_sum, values[i] + values[n - 1 - i])

        return max_sum

