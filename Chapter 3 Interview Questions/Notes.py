class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = StackNode(data)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top == None:
            return None

        item = self.top
        self.top = item.next
        return item.data

    def peek(self):
        if (self.top == None) : return None
        return self.top.data

    def isEmpty(self):
        return self.top == None


StackList = Stack()
StackList.push("Hey")
StackList.push("I")
StackList.push("Love")
StackList.push("You")

print(StackList.peek())
print(StackList.peek())
print(StackList.isEmpty())


class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue: 
    first = None
    last = None

    def __innit__(self):
        self.first = None
        self.last = None

    def add(self, item):
        node = QueueNode(item)
        if self.first == None:
            self.first = node
        else:
            self.last.next = node

        self.last = node

    def remove(self):
        if self.first == None: 
            return None

        item = self.first
        self.first = self.first.next
        return self.first.data

    def peek(self):
        if self.first == None: 
            return None

        return self.first.data

    def isEmpty(self):
        return self.first == None

queue = Queue()
queue.add("a")
queue.add("b")
queue.add("c")
queue.add("d")
queue.add("e")

print("-----------------------------------------------------")
print(queue.isEmpty())







