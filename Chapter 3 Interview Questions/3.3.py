"""
Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore in real life, we would likely start a new stack when the previous stack exceeds some threshold. Implement a data
structure SetsOfStacks that mimics this. SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should behave 
identically to a single stack (that is, pop() should return the same values as it would if there were just a single stack)
FOLLOW UP 
Implement a function popAt(int index) which performs a pop operation on a specific sub-stack
"""

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    top = None
    next = None

    def __init__(self):
        self.top = None
        self.next = None

    def push(self, item):
        node = StackNode(item)

        if self.top == None:
            self.top = node
        else:
            node.next = self.top
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

    def isEmpty(self):
        return self.top == None

    def size(self):
        n = self.top
        count = 0

        while n != None:
            count += 1
            n = n.next

        return count

class SetOfStacks:
    THRESHOLD = 2
    topset = None
    sets = 0

    def __innit__(self):
        self.topset = None
        self.sets = 0


    def push(self, item):
        if self.topset == None:
            self.topset = Stack()
            self.topset.push(item)
            self.sets += 1
        else:
            if self.topset.size() <= self.THRESHOLD:
                self.topset.push(item)
            else:
                self.sets += 1
                stack = Stack()
                stack.next = self.topset
                self.topset = stack
                self.topset.push(item)

    def pop(self):
        if self.topset.peek() == None:
            if self.topset.next != None:
                self.topset = self.topset.next
                self.sets -= 1
            else:
                return None

        return self.topset.pop()

    def popAt(self, index):
        n = self.topset
        if n == None:
            return None

        for i in range(self.sets - index - 1):
                n = n.next

        return n.pop()

values = SetOfStacks()
values.push(3)
values.push(5)
values.push(1)
values.push(2)
values.push(0)
values.push(11)

print(values.topset.size())
print(values.popAt(0))


