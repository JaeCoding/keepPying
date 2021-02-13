class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        cursor = self
        out = []
        while cursor:
            out.append(cursor.val)
            cursor = cursor.next
        return str(out)


