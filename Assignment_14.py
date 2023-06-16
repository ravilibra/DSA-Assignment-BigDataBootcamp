
'''
Q1. Given a linked list of **N** nodes such that it may contain a loop.
A loop here means that the last node of the link list is connected to the node at position X(1-based index).
If the link list does not have any loop, X=0.
Remove the loop from the linked list, if it is present, i.e. unlink the last node which is forming the loop.
'''

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def createLinkedListWithLoop():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node3

    return node1

def printLinkedList(head):
    nodes = []
    current = head
    while current:
        nodes.append(str(current.val))
        current = current.next
        if current in nodes:
            break

    print('->'.join(nodes))

def detectAndRemoveLoop(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    if not fast or not fast.next or not fast.next.next:
        return head

    slow = head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    prev = None
    while fast.next != slow:
        fast = fast.next

    fast.next = None

    return head

linked_list = createLinkedListWithLoop()

print("Linked List before loop removal:")
printLinkedList(linked_list)

modified_linked_list = detectAndRemoveLoop(linked_list)

print("\nLinked List after loop removal:")
printLinkedList(modified_linked_list)


'''
Q2. A number N is represented in Linked List such that each digit corresponds to a node in linked list. You need to add 1 to it.
'''

import sys
import math


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


def newNode(data):
	return Node(data)


def reverseList(head):
	if not head:
		return
	curNode = head
	prevNode = head
	nextNode = head.next
	curNode.next = None

	while(nextNode):
		curNode = nextNode
		nextNode = nextNode.next
		curNode.next = prevNode
		prevNode = curNode

	return curNode


def addOne(head):
	head = reverseList(head)
	k = head
	carry = 0
	prev = None
	head.data += 1

	while(head != None) and (head.data > 9 or carry > 0):
		prev = head
		head.data += carry
		carry = head.data // 10
		head.data = head.data % 10
		head = head.next

	if carry > 0:
		prev.next = Node(carry)
	return reverseList(k)



def printList(head):
	if not head:
		return
	while(head):
		print("{}".format(head.data), end="")
		head = head.next


if __name__ == '__main__':
	head = newNode(1)
	head.next = newNode(2)
	head.next.next = newNode(3)

	print("List is: ", end="")
	printList(head)

	head = addOne(head)

	print("\nResultant list is: ", end="")
	printList(head)
	

'''
Q3. Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:(i) a next pointer to the next node,
(ii) a bottom pointer to a linked list where this node is head.Each of the sub-linked-list is in sorted order.
Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order. Note:
The flattened list will be printed using the bottom pointer instead of next pointer.
'''



class Node():
	def __init__(self, data):
		self.data = data
		self.right = None
		self.down = None


class LinkedList():
	def __init__(self):
		self.head = None

	def push(self, head_ref, data):

		new_node = Node(data)

		new_node.down = head_ref

		head_ref = new_node

		return head_ref

	def printList(self):

		temp = self.head
		while(temp != None):
			print(temp.data, end=" ")
			temp = temp.down

		print()

	def merge(self, a, b):
		if(a == None):
			return b

		if(b == None):
			return a

		result = None

		if (a.data < b.data):
			result = a
			result.down = self.merge(a.down, b)
		else:
			result = b
			result.down = self.merge(a, b.down)

		result.right = None
		return result

	def flatten(self, root):

		if(root == None or root.right == None):
			return root

		root.right = self.flatten(root.right)

		root = self.merge(root, root.right)

		return root


if __name__ == '__main__':
	L = LinkedList()

	'''
	Let us create the following linked list
			5 -> 10 -> 19 -> 28
			| |	 |	 |
			V V	 V	 V
			7 20 22 35
			|		 |	 |
			V		 V	 V
			8		 50 40
			|			 |
			V			 V
			30			 45
	'''
	L.head = L.push(L.head, 30)
	L.head = L.push(L.head, 8)
	L.head = L.push(L.head, 7)
	L.head = L.push(L.head, 5)

	L.head.right = L.push(L.head.right, 20)
	L.head.right = L.push(L.head.right, 10)

	L.head.right.right = L.push(L.head.right.right, 50)
	L.head.right.right = L.push(L.head.right.right, 22)
	L.head.right.right = L.push(L.head.right.right, 19)

	L.head.right.right.right = L.push(L.head.right.right.right, 45)
	L.head.right.right.right = L.push(L.head.right.right.right, 40)
	L.head.right.right.right = L.push(L.head.right.right.right, 35)
	L.head.right.right.right = L.push(L.head.right.right.right, 20)

	L.head = L.flatten(L.head)

	L.printList()


'''
Q4. You are given a special linked list with **N** nodes where each node has a next pointer pointing to its next node.
You are also given **M** random pointers, where you will be given **M** number of pairs denoting two nodes **a** and **b**  **
i.e. a->arb = b** (arb is pointer to random node)**.**

Construct a copy of the given list. The copy should consist of exactly **N** new nodes, where each new node has its value set to the value
of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that
the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes
in the original list.

For example, if there are two nodes **X** and **Y** in the original list, where **X.arb** **-->** **Y**, then for the corresponding two nodes
 **x** and **y** in the copied list, **x.arb --> y.**

Return the head of the copied linked list.
'''


class Node:
	def __init__(self, d):
		self.data = d
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		
	def newNode(self, key):
		temp = Node(key)
		self.next = None
		return temp
	
	def rearrangeEvenOdd(self, head):
		if (self.head == None):
			return None

		odd = self.head
		even = self.head.next

		evenFirst = even

		while (1 == 1):
			
			if (odd == None or even == None or
							(even.next) == None):
				odd.next = evenFirst
				break

			odd.next = even.next
			odd = even.next
			
			if (odd.next == None):
				even.next = None
				odd.next = evenFirst
				break

			even.next = odd.next
			even = odd.next
		return head

	def printlist(self, node):
		while (node != None):
			print(node.data, end = "")
			print("->", end = "")
			node = node.next
		print ("NULL")
		
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

ll = LinkedList()
ll.push(5)
ll.push(4)
ll.push(3)
ll.push(2)
ll.push(1)
print ("Given Linked List")
ll.printlist(ll.head)

start = ll.rearrangeEvenOdd(ll.head)

print ("\nModified Linked List")
ll.printlist(start)

	

'''
Q6. Given a singly linked list of size N. The task is to left-shift the linked list by k nodes, where k is a given positive integer smaller than
or equal to length of the linked list.
'''



class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)

		new_node.next = self.head

		self.head = new_node

	def printList(self):
		temp = self.head
		while(temp):
			print (temp.data),
			temp = temp.next

	def rotate(self, k):
		if k == 0:
			return

		current = self.head

		count = 1
		while(count < k and current is not None):
			current = current.next
			count += 1

		if current is None:
			return

		kthNode = current

		while(current.next is not None):
			current = current.next

		current.next = self.head

		self.head = kthNode.next

		kthNode.next = None


llist = LinkedList()

for i in range(60, 0, -10):
	llist.push(i)

print ("Given linked list")
llist.printList()
llist.rotate(4)

print ("\nRotated Linked list")
llist.printList()


'''
Q7. You are given the `head` of a linked list with `n` nodes.

For each node in the list, find the value of the **next greater node**. That is, for each node, find the value of the first node that is
next to it and has a **strictly larger** value than it.

Return an integer array `answer` where `answer[i]` is the value of the next greater node of the `ith` node (**1-indexed**).
If the `ith` node does not have a next greater node, set `answer[i] = 0`.
'''


head = None


class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None



def sizeOfLL(head):
	count = 0
	while (head != None):
		count = count + 1
		head = head.next

	return count


def nextLargerLL(head):
	count = sizeOfLL(head)
	ans = [None]*count
	k = 0
	j = None
	temp = 0

	while (head != None):
		if (head.next == None):
			ans[k] = 0
			break

		j = head.next
		if (head.val < j.val):
			ans[k] = j.val
			k += 1

		elif (head.val >= j.val):
			while (
					j != None and head.val >= j.val):
				j = j.next


			if (j != None):
				ans[k] = j.val
				k += 1

			else:
				ans[k] = 0
				k += 1

		else:
			ans[k] = 0
			k += 1

		head = head.next

	return ans


def push(new_data):
	global head
	new_node = ListNode(new_data)

	new_node.next = head

	head = new_node


def printList():
	print(nextLargerLL(head))


if __name__ == '__main__':
	push(5)
	push(3)
	push(4)
	push(7)
	push(2)

	nextLargerLL(head)
	printList()


'''
Q8. Given the `head` of a linked list, we repeatedly delete consecutive sequences of nodes that sum to `0` until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

(Note that in the examples below, all sequences are serializations of `ListNode` objects.)
'''

class Solution:
	def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:

		dummy = ListNode(0,head)
		pre = 0
		dic = {0: dummy}

		while head:
			pre+=head.val
			dic[pre] = head
			head = head.next

		head = dummy
		pre = 0
		while head:
			pre+=head.val
			head.next = dic[pre].next
			head = head.next

		return dummy.next
	