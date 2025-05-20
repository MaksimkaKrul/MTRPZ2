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

    def deleteAll(self, element):
        if self.head is None:
            return

        while self.head.data == element:
            if self._length == 1:
                self.head = None
                self._length = 0
                return
            last = self.head
            while last.next != self.head:
                last = last.next
            last.next = self.head.next
            self.head = self.head.next
            self._length -= 1
            if self._length == 0:
                return

        current = self.head
        prev = None
        count = 0
        while count < self._length:
            if current.data == element:
                prev.next = current.next
                self._length -= 1
                current = prev.next
            else:
                prev = current
                current = current.next
                count += 1

    def get(self, index):
        if index < 0 or index >= self._length:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def clone(self):
        new_list = CircularLinkedList()
        if self.head is None:
            return new_list
        current = self.head
        for _ in range(self._length):
            new_list.append(current.data)
            current = current.next
        return new_list

    def reverse(self):
        if self._length <= 1:
            return

        prev = None
        current = self.head
        next_node = current.next
        last_node = self.head
        while last_node.next != self.head:
            last_node = last_node.next
        last_node.next = None

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = self.head

    def findFirst(self, element):
        if self.head is None:
            return -1
        current = self.head
        index = 0
        while True:
            if current.data == element:
                return index
            current = current.next
            index += 1
            if current == self.head:
                break
        return -1

    def findLast(self, element):
        if self.head is None:
            return -1
        current = self.head
        last_index = -1
        index = 0
        while True:
            if current.data == element:
                last_index = index
            current = current.next
            index += 1
            if current == self.head:
                break
        return last_index if last_index != -1 else -1

    def clear(self):
        self.head = None
        self._length = 0

    def extend(self, elements):
        current = elements.head
        for _ in range(elements.length()):
            self.append(current.data)
            current = current.next
