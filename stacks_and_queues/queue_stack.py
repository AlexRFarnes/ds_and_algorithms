# queue_stack.py


class Queue:
    def __init__(self):
        self.Stack1 = []
        self.Stack2 = []

    def enqueue(self, item):
        self.Stack1.append(item)

    def dequeue(self):
        if not self.Stack2:
            while self.Stack1:
                self.Stack2.append(self.Stack1.pop())
        if not self.Stack2:
            raise IndexError("dequeue from empty queue")
        return self.Stack2.pop()


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(23)
    queue.enqueue(13)
    queue.enqueue(11)
    print(queue.Stack1)

    queue = Queue()
    queue.enqueue(23)
    queue.enqueue(13)
    queue.enqueue(11)
    print(queue.Stack1)

    item = queue.dequeue()
    print(f"Dequed element: {item}")
    print(queue.Stack2)
