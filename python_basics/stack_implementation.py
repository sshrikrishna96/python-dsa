class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

s = Stack()
s.push(10)
s.push(20)
s.push(30)

print(s.peek())

print(s.pop())

print(s.peek())

print(s.isEmpty())