# linked_list.py


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self._size: int = 0

    @property
    def size(self):
        return self._size

    def append(self, data):
        # Encapsulate the data in a Node
        node = Node(data)
        if self.tail:
            # previous last node's next property now points to the appended node
            self.tail.next = node
            # linked list property tail now points to the newly appended node
            self.tail = node
        else:
            # first node
            self.head = node
            self.tail = node
        self._size += 1

    def append_at_a_location(self, data, index):
        current = self.head
        prev = self.head
        node = Node(data)
        count = 0
        while current:
            if index == 0:
                node.next = current
                self.head = node
                self._size += 1
                return
            elif index == count:
                node.next = current
                prev.next = node  # type: ignore
                self._size += 1
                return
            count += 1
            prev = current
            current = current.next
        print("The list has less number of elements")

    def search(self, data):
        for node in self.iter():
            if data == node.data:
                return True
        return False

    def delete_first_node(self):
        if self.head is None:
            print("No data element to delete")
            return
        self.head = self.head.next

    def delete_last_node(self):
        current = self.head
        prev = self.head
        while current:
            if current.next is None:  # reach end of linked list
                prev.next = None  # type: ignore
                self._size -= 1
                return
            prev = current
            current = current.next

    def delete(self, index):
        current = self.head
        prev = self.head
        count = 0
        while current:
            if index == 0:
                self.head = current.next
                self._size -= 1
                return
            elif index == count:
                prev.next = current.next  # type: ignore
                self._size -= 1
                return
            prev = current
            current = current.next
            count += 1
        print("The list has less number of elements")

    def iter(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def clear(self):
        self.head = None
        self.tail = None


class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next: Node | None = None


# Creating
words = SinglyLinkedList()
words.append("egg")
words.append("ham")
words.append("spam")

print("#" * 100)
print("Original linked list")
current = words.head
while current:
    print(current.data)
    current = current.next

print("#" * 100)
print("Add bread at location 2")
words.append_at_a_location("bread", 2)
current = words.head
while current:
    print(current.data)
    current = current.next

print("#" * 100)
print("spam is in linked list: ", words.search("spam"))
print("apple is in linked list: ", words.search("apple"))
print("Size of linked is: ", words.size)

print("#" * 100)
print("Deleting first node")
words.delete_first_node()
current = words.head
while current:
    print(current.data)
    current = current.next


print("#" * 100)
print("Deleting last node")
words.delete_last_node()
current = words.head
while current:
    print(current.data)
    current = current.next

print("#" * 100)
print("Deleting second node")
words.delete(1)
current = words.head
while current:
    print(current.data)
    current = current.next
