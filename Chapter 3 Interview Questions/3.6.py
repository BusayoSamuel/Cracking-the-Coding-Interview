"""
Animal Shelter, An animal shelter which holds only dogs and cats, operates on a strictly "first in, first out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they can 
select whether they would prefer a dog or a cat (and will receive the oldest animal of that type). They cannot select which specific animal they would like. Create the data structures to maintain this system and impement
operations such as enqueue, dequeuAny, dequeueDog, and dequeueCat. You may use the built-in LinkedList data structure.
"""

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    head = None
    
    def __init__(self):
        self.head = None
        
    def append(self, item):
        node = Node(item)
        n = self.head
        
        if n == None:
            self.head = node
            return
        
        while n.next != None:
            n = n.next
            
        n.next = node
        
    def remove(self, item):
        if self.head == None:
            return None
            
        n = self.head
        
        while n.data != item:
            if n.next == None:
                return None
            n = n.next
            
        n.data = n.next.data
        n.next = n.next.next
        
        
class AnimalShelter:
    any = LinkedList()
    dogs = LinkedList()
    cats = LinkedList()
    
    
    def __init__(self):
        pass
        
    def enqueue(self, animal):
        
        if animal.find("cat") != -1:
            self.cats.append(animal)
            
        if animal.find("dog") != -1:
            self.dogs.append(animal)
            
        self.any.append(animal)
           
    def dequeueAny(self):
        
        item = self.any.head.data
        
        self.any.head = self.any.head.next
        
        if item.find("dog") != -1:
            node = self.dogs.head
            
            while node.data != item:
                node = node.next
                
            node.data = node.next.data
            node.next = node.next.next
            
        if item.find("cat") != -1:
            node = self.cats.head
            
            while node.data != item:
                node = node.next
                
            node.data = node.next.data
            node.next = node.next.next
        
        return item
        
    def dequeueCat(self):
        
        item = self.cats.head.data
        
        self.cats.head = self.cats.head.next
        
        node = self.any.head
        
        while node.data != item:
            node = node.next
            
        node.data = node.next.data
        node.next = node.next.next
        
        return item 
        
    
    def dequeueDog(self):
        
        item = self.dogs.head.data
        
        self.dogs.head = self.dogs.head.next
        
        node = self.any.head
        
        while node.data != item:
            node = node.next
            
        node.data = node.next.data
        node.next = node.next.next
        
        return item 
        
        
a = AnimalShelter()
a.enqueue("cat1")
a.enqueue("cat2")
a.enqueue("rabbit")
a.enqueue("dog1")
a.enqueue("snake")

print(a.dequeueAny())
print(a.dequeueCat())
print(a.dequeueAny())
print(a.dequeueDog())
print(a.dequeueAny())
"""

##Solution
class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    head = None

    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)

        if self.head == None:
            self.head = node
        else:
            n = self
            while n.next != None:
                n = n.next
            n.next = node

class Animal:
    def __init__(self, animal:str , order: int):
        self.animal = animal
        self.order = order

class AnimalShelter:
    dog_list = None
    cat_list = None
    order = 0

    def __init__(self):
        self.dog_List = LinkedList()
        self.dog_List = LinkedList()

    def enqueue(self, item):
        if item.find("dog") != -1:
            self.dog_list.append(Animal(item, order))

        if item.find("cat") != -1:
            self.cat_list.append(Animal(item, order))

        order += 1





      


















