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

 
            
    def append(self, val):
        end = Node(val)
        n = self
        while n.next != None:
            n = n.next
        n.next = end

List = Node(3)
List.append(5)
List.append(8)
List.append(5)
List.append(10)
List.append(2)
List.append(1)


def partition(l, p):
    new_l = None

    while l != None:
        print("Here")
        if l.val < p:
            if new_l == None:
                new_l = Node(l.val)
            else:
                new_l.append(l.val)
        l = l.next

    while l != None:
        if l.val >= p:
                new_l.append(l.val)
        l = l.next
   
    while new_l != None:
        print(new_l.val)
        new_l = new_l.next
    

partition(List, 5)