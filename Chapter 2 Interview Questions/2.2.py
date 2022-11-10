"""
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list
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

def k_to_last(k, head):
    current = head
    runner = head
    count = 0

    while runner != None and count < k - 1:
        runner = runner.next
        count += 1

    while runner.next != None:
        current = current.next
        runner = runner.next

    return current.val

print(k_to_last(0, List))

def k_to_last_solution1(k, head):
    current = head
    runner = head

    for i in range(k-1):
        if runner == None:
            return None
        runner = runner.next

    while runner.next != None:
        current = current.next
        runner = runner.next

    return current.val

print(k_to_last_solution1(0, List))

def k_to_last_solution2(k, head):
    if head == None:
        return 0

    index = k_to_last_solution2(k, head.next) + 1
    if index == k:
        print(f"The {k}th to last element is {head.val}")  

    return index

print(k_to_last_solution2(1, List))



