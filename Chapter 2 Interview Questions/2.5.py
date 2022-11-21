"""
Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit, the digits are stored in reverse order, such that the 1's digit is at the 
head of the list. Write a function that adds the two numbers and returns the sum as a linked list. (You are not allowed to "cheat" and just convert the linked list to an integer)
EXAMPLE
Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is 617 + 295
Output: 2 -> 1 -> 9. That is, 912

FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem

EXAMPLE
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is 617 + 295
Output: 9 -> 1 -> 2. That is, 912
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

listnode1 = Node(7)
listnode1.append(Node(1))
listnode1.append(Node(6))

listnode2 = Node(5)
listnode2.append(Node(9))
listnode2.append(Node(2))
listnode2.append(Node(1))


def sum_lists_reverse(n1, n2):
    output = None
    carry = 0

    while n1 != None and n2 != None:

        n3 = n1.val + n2.val + carry
        carry = 0

        if n3 >= 10:
            carry = 1
            n3 %= 10

        if output == None:
            output = Node(n3)
        else:
            output.append(Node(n3))

        if n1.next != None and n2.next == None:
            n2.append(Node(0))
            n2 = n2.next
            n1 = n1.next
        elif n2.next != None and n1.next == None:
            n1.append(Node(0))
            n1 = n1.next
            n2 = n2.next
        else:
            n1 = n1.next
            n2 = n2.next

    return output.printl()


sum_lists_reverse(listnode1, listnode2)

print("-----------")

def sum_lists_solution1(l1, l2, carry=0):
    if l1 == None and l2 == None and carry == None:
        return None

    result = None
    value = carry

    if l1 != None:
        value += l1.val

    if l2 != None:
        value += l2.val

    result = Node(value % 10)

    if value >= 10:
        carry = 1
    else:
        carry = 0

    if(l1 != None or l2 != None):
        more = sum_lists_solution1(l1.next or None, l2.next or None, carry)
        result.next = more

    return result.printl()

sum_lists_solution1(listnode1, listnode2)




