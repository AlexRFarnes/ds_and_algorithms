# stack_array.py


class Stack:
    def __init__(self, size):
        self.size = size
        self.top = -1
        self.data = [None] * self.size

    def push(self, data):
        if self.top + 1 >= self.size:
            print("Stack Overflow")
        else:
            self.top += 1
            self.data[self.top] = data

    def pop(self):
        if self.top < 0:
            print("Stack Underflow")
        else:
            data = self.data[self.top]
            self.data[self.top] = None
            self.top -= 1
            return data

    def peek(self):
        if self.top < 0:
            print("Stack is empty")
        else:
            print(self.data[self.top])


if __name__ == "__main__":
    stack = Stack(3)
    stack.push("egg")
    stack.push("ham")
    stack.push("spam")
    print(stack.data[0 : stack.top + 1])
    stack.push("new")
    stack.push("new2")

    print(stack.data[0 : stack.top + 1])
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.data[0 : stack.top + 1])
