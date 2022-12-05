class Node:
    data = None
    next = None
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    top = None
    
    def __init__(self):
        self.top = None
        
    def push(self, item):
        node = Node(item)
        
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
        
class MyQueue:
    stack = Stack()
    temp_stack = Stack()
    first = None
    last = None
    
    def __init__(self):
        pass
        
    def add(self, item):
        node = Node(item)
        self.stack.push(item)
        
    def remove(self):
        while not self.stack.isEmpty():
            print("Here")
            self.temp_stack.push(self.stack.pop())
            
        item = self.temp_stack.pop()
        
        while not self.temp_stack.isEmpty():
            self.stack.push(self.temp_stack.pop())
            
        return item
           
    def peek(self):
        while not self.stack.isEmpty():
            self.temp_stack.push(self.stack.pop())
            
        item = self.temp_stack.peek()
        
        while not self.temp_stack.isEmpty():
            self.stack.push(self.temp_stack.pop())
            
        return item
        
    def isEmpty(self, item):
        return self.stack.isEmpty()
        
        
queue = MyQueue()
queue.add(5)
queue.add(11)
queue.add("a")

print(queue.remove())
queue.add("7")
print(queue.remove())
print(queue.peek())
        
        
            
            