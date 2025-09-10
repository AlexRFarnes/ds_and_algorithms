# queue_linked_list.py


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Queue:
    def __init__(self):
        self.head = None  # dequeue from head
        self.tail = None  # enqueue at tail
        self.count = 0

    def enqueue(self, data):
        new_node = Node(data, None, None)
        if self.head is None:  # Queue is empty
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node  # type: ignore
            self.tail = new_node
        self.count += 1

    def dequeue(self):
        if self.head is None:  # Queue is empty
            return None
        removed_node = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:  # Queue is now empty
            self.tail = None
        self.count -= 1
        return removed_node.data
