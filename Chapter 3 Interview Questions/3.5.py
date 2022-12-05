class StackNode:
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
        
        
stack = Stack()
stack.push(1)        
stack.push(10)
stack.push(3)
stack.push(5)
stack.push(20)

def sort_stack(stack: Stack) -> Stack:
    temp_stack = Stack()
    
    temp_stack.push(stack.pop())
    
    while not stack.isEmpty():
        if stack.peek() >= temp_stack.peek():
            temp_stack.push(stack.pop())
        else:
            item = stack.pop()
            count = 0
            
            while not temp_stack.isEmpty() and temp_stack.peek() > item:
                stack.push(temp_stack.pop())
                count += 1
                
            temp_stack.push(item)
            
            for i in range(count):
                temp_stack.push(stack.pop())
            
    while not temp_stack.isEmpty():
        stack.push(temp_stack.pop())
        
    return stack
    
stack = sort_stack(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
                
                
                
            
            
