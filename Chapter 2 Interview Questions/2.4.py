"""
Partition: Write code to partition a linked list around a value x such that all nodes less than x come before all nodes greater than or equal to x. (IMPORTANT: The partition 
element can appear in the "right partition"; it does not need to appear between the left and right partitions, The additional spacing in the example below indicates the partition.
Yes, the output below is one of many valid outputs!)
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 (partition = 5)
Output: 3 -> 1 -> 2    ->     10 -> 5 -> 5 -> 8
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def append(self, node):
        n = self

        while n.next != None:
            n = n.next

        n.next = node

    def printl(self):
        n = self

        while n != None:
            print(n.val)
            n = n.next


List = Node(3)
List.append(Node(5))
List.append(Node(8))
List.append(Node(5))
List.append(Node(10))
List.append(Node(2))
List.append(Node(1))

#List.printl()

def partition(listnode, part):
    lower_part = None
    higher_part = None

    n = listnode

    while n != None:
        if n.val < part:
            if lower_part == None:
                lower_part = Node(n.val)
            else:
                lower_part.append(Node(n.val))
        else:
            if higher_part == None:
                higher_part = Node(n.val)
            else:
                higher_part.append(Node(n.val))
        n = n.next

    lower_part.append(higher_part)
    new_list = lower_part

    return new_list

partition(List, 5).printl()





