"""
Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e any node but the first and last node, not necessarily the exact middle) of a single linked list,
given only access to that node
EXAMPLE
Input: the node c from the linked list a -> b -> c -> d -> e -> f
Result: nothing is returned, but the new linked list looks like a -> b -> d -> e -> f
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
            
    def append(self, val):
        end = Node(val)
        n = self
        while n.next != None:
            n = n.next
        n.next = end

List = Node("a")
List.append("b")
List.append("c")
List.append("d")
List.append("e")
List.append("f")

"""
def del_mid_node(head):
    current = head
    runner = head
    previous = None

    while runner.next != None and runner.next.next != None:
        previous = current
        current = current.next
        runner = runner.next.next

    previous.next = current.next

del_mid_node(List)
"""

"""
def del_mid_node(mid_node, l):

    previous = None
    while l != None:
        if l.val == mid_node:
            previous.next = l.next
        else:
            previous = l
        l = l.next

del_mid_node("c", List)
"""

def del_mid_node_solution(mid_node):
    if mid_node == None or mid_node.next == None:
        return False

    temp = mid_node.next
    mid_node.data = temp.data
    mid_node.next = temp.next

del_mid_node_solution(Node("c"))
print(Node("c").next)

while List != None:
    print(List.val)
    List = List.next








    
