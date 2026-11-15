class Node:
    def __init__(self, val, next = None, prev = None):
        self.value = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        

    def get(self, index: int) -> int:
        if 0 <= index < self.length:
            cur = self.head
            for _ in range(index):
                cur = cur.next
            return cur.value
        return -1
        

    def addAtHead(self, val: int) -> None:
        node = Node(val, next=self.head, prev=None)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            self.head = node
        self.length += 1
        

    def addAtTail(self, val: int) -> None:
        if self.length == 0:
            self.addAtHead(val)
        else:
            node = Node(val, None, self.tail)
            self.tail.next = node
            self.tail = node
            self.length += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        elif 0 < index < self.length:
            cur = self.head
            for _ in range(index):
                cur = cur.next
            node = Node(val, cur, cur.prev)
            if cur.prev:
                cur.prev.next = node
            cur.prev = node
            if index == 0:
                self.head = node
            self.length += 1
        return None

        

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self.length:
            cur = self.head
            for _ in range(index):
                cur = cur.next
            if cur.prev:
                cur.prev.next = cur.next
            else:
                self.head = cur.next
            if cur.next:
                cur.next.prev = cur.prev
            else:
                self.tail = cur.prev
            self.length -= 1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)