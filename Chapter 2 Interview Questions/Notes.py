#Implementing a Linked List

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
            
class LinkedList:
    def __init__(self, val):
        self.head = Node(val)

    def append(self, val):
        end = Node(val)
        n = self.head
        while n.next != None:
            n = n.next
        n.next = end

    def delete(self, d):
        if self.head.val == None:
            return None

        if self.head.val == d:
            self.head = self.head.next

        n = self.head
        while n.next != None:
            if n.next.val == d:
                n.next = n.next.next
            n = n.next

List = LinkedList(1)
List.append(2)
List.append(3)
List.append(4)

List.delete(2)

print(List.head.val)
         








