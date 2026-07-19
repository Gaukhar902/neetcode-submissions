class ListNode:
    def __init__(self, val: int = 0, next_node = None):
        self.val = val
        self.next = next_node

class MyLinkedList:

    def __init__(self):
        self.dummy = ListNode()
        self.size = 0
        
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        current = self.dummy.next

        for _ in range(index):
            current = current.next
        
        return current.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val, self.dummy.next)
        self.dummy.next = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        current = self.dummy

        while current.next:
            current = current.next

        current.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        
        if index < 0:
            index = 0

        previous = self.dummy

        for _ in range(index):
            previous = previous.next

        new_node = ListNode(val, previous.next)
        previous.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        previous = self.dummy

        for _ in range(index):
            previous = previous.next

        previous.next = previous.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)