"""
Remove Dups: Write code to remove duplicates from an unsorted linked list
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
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

List = Node(1)
List.append(2)
List.append(1)
List.append(4)
List.append(1)

"""
while List != None:
    print(List.val)
    List = List.next
"""

def remove_dups(head):
    current = head
    while current != None:
        runner = current
        while runner.next != None:
            if runner.next.val == current.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next


    while head != None:
        print(head.val)
        head = head.next

remove_dups(List)

def remove_dups_solution(node):
    data_set = set()
    head = node
    previous_node = None
    while head != None:
        if head.val in data_set:
            previous_node.next = head.next
        else:
            data_set.add(head.val)
            previous_node = head
        head = head.next

    while node != None:
        print(node.val)
        node = node.next

remove_dups_solution(List)
