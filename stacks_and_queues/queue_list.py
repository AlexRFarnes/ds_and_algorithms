# queue_list.py


class ListQueue:
    def __init__(self):
        self.items = []
        self.front = self.rear = 0
        self.size = 3  # max size of the queue

    def enqueue(self, data):
        if self.rear == self.size:
            print("\nQueue is full")
            return
        self.items.append(data)
        self.rear += 1

    def dequeue(self):
        if self.front == self.rear:
            print("\nQueue is empty")
            return
        data = self.items.pop(0)
        self.rear -= 1
        return data


if __name__ == "__main__":
    q = ListQueue()
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    print(q.items)

    data = q.dequeue()
    print(data)
    print(q.items)
