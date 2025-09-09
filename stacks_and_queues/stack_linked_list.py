# stack_linked_list.py


class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next: Node | None = None


class Stack:
    def __init__(self):
        self.top: Node | None = None
        self.size = 0

    def push(self, data):
        # create a new node
        node = Node(data)

        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size += 1

    def pop(self):
        if not self.top:
            return None
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None


if __name__ == "__main__":

    words = Stack()
    print("*" * 40)
    print("Push")
    print("*" * 40)
    words.push("egg")
    words.push("ham")
    words.push("spam")
    # print the stack elements.
    current = words.top
    while current:
        print(current.data)
        current = current.next
    print()
    print("*" * 40)
    print("Pop")
    print("*" * 40)
    words.pop()
    current = words.top
    while current:
        print(current.data)
        current = current.next
    words.pop()
    words.pop()
    words.pop()
