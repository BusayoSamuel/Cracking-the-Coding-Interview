"""
Stack Min: How would you design a stack which, in addition to push and pop, has a function min which returns minimum element? Push, pop and min should all operate in O(1) time.
"""

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.min = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        node = StackNode(item)
        if self.top == None:
            self.top = node
            self.top.min = node
        else:
            node.next = self.top
            node.min = min(node, self.top.min, key=lambda x:x.data)
            self.top = node

    def pop(self):
        if self.top == None:
            return None

        item = self.top.data
        self.top = self.top.next
        return item

    def peek(self):
        if self.top == None:
            return None
        return self.top.data

    def min(self):
        if self.top == None:
            return None
        return self.top.min.data

values = Stack()
values.push(3)
values.push(5)
values.push(1)
values.push(2)
values.push(0)

print(values.min())
values.pop()
print(values.min())
values.pop()
print(values.min())
values.pop()
print(values.min())

