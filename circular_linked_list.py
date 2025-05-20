class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self._length = 0

    def length(self):
        return self._length

    def append(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
        self._length += 1

    def insert(self, element, index):
        if index < 0 or index > self._length:
            raise IndexError("Index out of bounds")
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            if index == 0:
                new_node.next = self.head
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = new_node
                self.head = new_node
            else:
                current = self.head
                for _ in range(index - 1):
                    current = current.next
                new_node.next = current.next
                current.next = new_node
        self._length += 1

    def delete(self, index):
        if index < 0 or index >= self._length:
            raise IndexError("Index out of bounds")
        if self.head is None:
            raise Exception("List is empty")

        data = None
        if self._length == 1:
            data = self.head.data
            self.head = None
        else:
            if index == 0:
                data = self.head.data
                last = self.head
                while last.next != self.head:
                    last = last.next
                last.next = self.head.next
                self.head = self.head.next
            else:
                current = self.head
                for _ in range(index - 1):
                    current = current.next
                to_delete = current.next
                data = to_delete.data
                current.next = to_delete.next
        self._length -= 1
        return data
