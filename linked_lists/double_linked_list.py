# double_linked_list.py


class Node:
    def __init__(self, data=None, _next=None, prev=None):
        self.data = data
        self.next = _next
        self.prev = prev


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append_at_start(self, data):
        node = Node(data=data)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.count += 1

    def append(self, data):
        node = Node(data=data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.count += 1

    def append_at_a_location(self, search_data, data):
        node = Node(data=data)
        current = self.head
        prev = self.head
        while current:
            if current.data == search_data:
                node.prev = prev
                node.next = current
                prev.next = node
                current.prev = node
                self.count += 1
            prev = current
            current = current.next

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def contains(self, data):
        for node_data in self.iter():
            if node_data == data:
                return True
        return False

    def delete(self, data):
        current = self.head
        node_deleted = False
        if current is None:
            # List is empty
            print("List is empty")
        elif self.head.data == data:
            # Item to be deleted is found at starting of the list
            self.head = self.head.next
            self.head.prev = None
            node_deleted = True
        elif self.tail.data == data:
            # Item to be deleted is found at the end of the list
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True
        else:
            while current:
                # Search for the item and delete it if it's found
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next
        if node_deleted:
            self.count -= 1
        else:
            print("Item not found")


words = DoubleLinkedList()
words.append("egg")
words.append("ham")
words.append("spam")
print("Items in doubly linked list before append:")
current = words.head
while current:
    print(current.data)
    current = current.next
words.append_at_start("book")
print("Items in doubly linked list after append:")
current = words.head
while current:
    print(current.data)
    current = current.next

print("Items in doubly linked list after append")
words = DoubleLinkedList()
words.append("egg")
words.append("ham")
words.append("spam")
words.append("book")
print("Items in doubly linked list after adding element at end.")
current = words.head
while current:
    print(current.data)
    current = current.next

words = DoubleLinkedList()
words.append("egg")
words.append("ham")
words.append("spam")
words.append_at_a_location("ham", "bread")
print('Doubly linked list after adding an element after word "ham" in the list.')
current = words.head
while current:
    print(current.data)
    current = current.next


words = DoubleLinkedList()
words.append("egg")
words.append("ham")
words.append("spam")
print("ham in double linked list: ", words.contains("ham"))
print("ham2 in double linked list: ", words.contains("ham2"))

# Code to create for a doubly linked list
words = DoubleLinkedList()
words.append("egg")
words.append("ham")
words.append("spam")
words.delete("ham")
current = words.head
while current:
    print(current.data)
    current = current.next
words.delete("ham")
