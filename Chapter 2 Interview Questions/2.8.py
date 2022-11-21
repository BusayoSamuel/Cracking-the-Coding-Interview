"""
Loop Detection: Given a linked list which might contain a loop, implement an algorithm that returns the node at the beginning of the loop (if one extsts)
EXAMPLE
Input: A -> B -> C -> D -> E -> C [the same C as earlier]
Output: C
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

    def printe(self):
        n = self

        while n != None:
            print(n.data)
            n = n.next

List1 = Node("A")
List1.append(Node("B"))


List2 = Node("C")
List1.append(List2)
List1.append(Node("D"))
List1.append(Node("E"))
List1.append(List2)

"""
def loop_detection(l):
    current = l

    while current != None:
        runner = current.next
        while runner != None:
            if current.data == runner.data:
                return current.data
            runner = runner.next
        current = current.next

    return False

print(loop_detection(List1))
"""

List1.printe()
