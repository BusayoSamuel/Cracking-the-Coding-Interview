from cProfile import run
from faulthandler import cancel_dump_traceback_later
from platform import node


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
		nodes = []
		node = self

		while node != None:
			nodes.append(str(node.data))
			node = node.next

		nodes.append("None")

		print("->".join(nodes))

LinkedList = Node("a")
LinkedList.append(Node("e"))
LinkedList.append(Node("f"))
LinkedList.append(Node("a"))
LinkedList.append(Node("b"))

#Q2.1
def remove_dups(node):
	letter_counts = [0] * 128
	current = node

	while current != None:
		if letter_counts[ord(current.data)] >= 1:
			current.data = current.next.data
			current.next = current.next.next
		else:
			letter_counts[ord(node.data)] += 1
		current = current.next

remove_dups(LinkedList)
LinkedList.printl()

LinkedList = Node("a")
LinkedList.append(Node("e"))
LinkedList.append(Node("f"))
LinkedList.append(Node("a"))
LinkedList.append(Node("b"))

#Q2.2 
def k_to_last(node, k):
	current = node
	runner = node

	for i in range(k - 1):
		runner = runner.next

	while runner.next != None:
		current = current.next
		runner = runner.next

	return current.data

print(k_to_last(LinkedList, 2))

LinkedList = Node("a")
LinkedList.append(Node("e"))
LinkedList.append(Node("f"))
LinkedList.append(Node("a"))
LinkedList.append(Node("b"))

#Q2.3
def del_middle(node):
	current = node
	runner = node

	while runner.next != None and runner.next.next != None:
		current = current.next
		runner = runner.next.next

	current.data = current.next.data
	current.next = current.next.next


del_middle(LinkedList)
LinkedList.printl()


LinkedList = Node(5)
LinkedList.append(Node(2))
LinkedList.append(Node(1))
LinkedList.append(Node(20))
LinkedList.append(Node(30))

#Q2.4
def partition(node, part):
	lower = None
	higher = None

	while node != None:
		if node.data < part:
			if lower == None:
				lower = Node(node.data)
			else:
				lower.append(Node(node.data))
		else:
			if higher == None:
				higher = Node(node.data)
			else:
				higher.append(Node(node.data))
		node = node.next

	lower.append(higher)
	return lower

partition(LinkedList, 5).printl()

List1 = Node(7)
List1.append(Node(1))
List1.append(Node(6))

List2 = Node(5)
List2.append(Node(9))
List2.append(Node(2))
List2.append(Node(7))

#Q2.4 
def sum_lists(l1, l2):
	carry = 0
	result = None

	while l1 != None or l2 != None:
		node_sum = (l1.data if l1 != None else 0) + (l2.data if l2 != None else 0) + carry
		carry = 0

		if node_sum >= 10:
			node_sum %= 10
			carry = 1

		if result == None:
			result = Node(node_sum)
		else:
			result.append(Node(node_sum))

		l1 = l1.next if l1 != None else None
		l2 = l2.next if l2 != None else None

	return result.printl()

sum_lists(List1, List2)

def recursive_sum_lists(l1, l2, carry=0):
	if l1 == None and l2 == None and carry == 0:
		return None

	node_sum = carry

	if l1 != None:
		node_sum += l1.data

	if l2 != None:
		node_sum += l2.data

	if node_sum >= 10:
		node_sum %= 10
		carry = 1
	else:
		carry = 0

	result = Node(node_sum)
	result.next = recursive_sum_lists(l1.next if l1 != None else None, l2.next if l2 != None else None, carry)

	return result

recursive_sum_lists(List1, List2).printl()

LinkedList = Node("a")
LinkedList.append(Node("b"))
LinkedList.append(Node("c"))
LinkedList.append(Node("b"))
LinkedList.append(Node("a"))

#Q2.6
def is_palindrome(node):
	def reverse(node):
		head = None
		while node != None:
			n = Node(node.data)
			n.next = head
			head = n
			node = node.next 
		return head

	reversedl = reverse(node)

	while reversedl != None and node != None:
		if reversedl.data != node.data:
			return False
		reversedl = reversedl.next
		node = node.next
	return True

print(is_palindrome(LinkedList))

def is_palindrome_v2(node):
	stack = []

	current = node
	runner = node

	while runner.next != None and runner.next.next != None:
		stack.append(current.data)
		current = current.next
		runner = runner.next.next

	if runner.next == None:
		current = current.next

	while current != None:
		if current.data != stack.pop():
			return False
		current = current.next
	return True

print(is_palindrome_v2(LinkedList))

List1 = Node(7)
List1.append(Node(1))
List1.append(Node(6))

List2 = Node(5)
List2.append(Node(9))
List2.append(Node(2))
List2.append(Node(7))
List2.append(List1)

def intersection(l1, l2):
	if l1 != None and l2 != None:
		l1_size = 1
		l2_size = 1
		l1_head = l1
		l2_head = l2
	else:
		return None

	while l1.next != None:
		l1_size += 1
		l1 = l1.next

	while l2.next != None:
		l2_size += 1
		l2 = l2.next

	if l1 != l2:
		return False

	longer = l1_head if l1_size > l2_size else l2_head
	shorter = l2_head if longer == l1_head else l1_head

	for i in range(abs(l1_size - l2_size)):
		longer = longer.next

	while longer != shorter:
		longer = longer.next
		shorter = shorter.next

	return longer.data

print(intersection(List1, List2))

List2 = Node(5)
List2.append(Node(9))
List2.append(Node(2))
List2.append(Node(7))
List2.append(List2)

#Q2.8
def detect_loop(head):
	current = head
	runner = head

	while runner != None and runner.next != None:
		current = current.next
		runner = runner.next.next

		if current == runner:
			current = head
			while current != runner:
				current = current.next
				runner = runner.next
			return current.data

	return False

print(detect_loop(List2))





		
			








"""
current = l

while current != None:
	runner = current.next
	while runner != None:
		if current.data = runner.data:
			runner.next = runner.next.next
		runner = runner.next
	current = current.next
"""




		
