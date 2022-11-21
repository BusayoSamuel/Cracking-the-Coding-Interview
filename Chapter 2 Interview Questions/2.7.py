"""
Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value. That is, if the kth node of the first
linked list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, node):
        n = self

        while n.next != None:
            n = n.next

        n.next = node

    def printl(self):
        n = self
        nodes = []

        while n != None:
            nodes.append(str(n.data))
            n = n.next

        nodes.append("None")

        print("->".join(nodes))

List1 = Node(5)
List1.append(Node(6))
List1.append(Node(7))
List1.append(Node(8))

List2 = Node(10)
List2.append(Node(15))
List2.append(Node(20))
List2.append(Node(30))
List2.append(List1)

List3 = Node("a")
List3.append(Node("e"))
List3.append(List1)



def intersection(l1, l2):
    l1_head = l1
    l2_head = l2

    while l1 != None:
        while l2 != None:
            if l1 == l2:
                return l1.data
            l2 = l2.next
        l2 = l2_head
        l1 = l1.next

    l1 = l1_head
    l2 = l2_head

    while l2 != None:
        while l1 != None:
            if l2 == l1:
                return True
            l1 = l1.next
        l1 = l1_head
        l2 = l2.next       

    return False

print(intersection(List2, List3))

def intersection_solution(l1, l2):
    l1_head = l1
    l2_head = l2

    if l1 != None and l2 != None:
        l1_size = 1
        l2_size = 1
    else:
        return False

    while l1.next != None:
        l1_size += 1
        l1 = l1.next
    

    while l2.next != None:
        l2_size += 1
        l2 = l2.next

    if l2 != l1:
        return False
    
    if l1_size > l2_size:
        longer = l1_head
        shorter = l2_head
    else:
        shorter = l1_head
        longer = l2_head

    for i in range(abs(l1_size-l2_size)):
        longer = longer.next

    while longer != shorter:
        longer = longer.next
        shorter = shorter.next
        
    return longer.data
print(intersection_solution(List2, List3))

