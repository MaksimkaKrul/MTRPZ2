class ArrayList:
    def __init__(self):
        self.data = []

    def length(self):
        return len(self.data)

    def append(self, element):
        self.data.append(element)

    def insert(self, element, index):
        if index < 0 or index > len(self.data):
            raise IndexError("Index out of bounds")
        self.data.insert(index, element)

    def delete(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of bounds")
        return self.data.pop(index)

    def deleteAll(self, element):
        self.data = [e for e in self.data if e != element]

    def get(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of bounds")
        return self.data[index]

    def clone(self):
        new_list = ArrayList()
        new_list.data = self.data.copy()
        return new_list

    def reverse(self):
        self.data.reverse()

    def findFirst(self, element):
        try:
            return self.data.index(element)
        except ValueError:
            return -1

    def findLast(self, element):
        for i in reversed(range(len(self.data))):
            if self.data[i] == element:
                return i
        return -1

    def clear(self):
        self.data.clear()

    def extend(self, elements):
        self.data.extend(elements.data)
