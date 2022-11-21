"""
Palindrome: Implement a function to check if a linked list is a palindrome
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

        print("->".join(nodes))

LinkedList = Node("b")
LinkedList.append(Node("b"))
LinkedList.append(Node("b"))
LinkedList.append(Node("b"))
LinkedList.append(Node("b"))
LinkedList.append(Node("b"))
LinkedList.printl()


def is_palindrome(node: Node) -> bool:
    stack = []

    current = node
    runner = node

    while runner != None and runner.next != None:
        stack.append(current.data)
        current = current.next
        runner = runner.next.next

    if runner != None:
        current = current.next

    while current != None:
        if current.data != stack.pop():
            return False
        else:
            current = current.next

    return True

print(is_palindrome(LinkedList))

def is_palindrome_solution1(node: Node) -> bool:

    def reverse(node: Node) -> Node:
        head = None
        while node != None:
            n = Node(node.data)
            n.next = head
            head = n
            node = node.next
        return head

    reverse_node = reverse(node)

    while node != None and reverse_node != None:
        if node.data != reverse_node.data:
            return False
        
        node = node.next
        reverse_node = node.next

    return True

print(is_palindrome_solution1(LinkedList))





