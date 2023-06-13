
'''
Q1. Given a singly linked list, delete middle of the linked list. For example, if given linked list is 1->2->3->4->5 then linked list
should be modified to 1->2->4->5.If there are even nodes, then there would be two middle nodes, we need to delete the second middle element.
For example, if given linked list is 1->2->3->4->5->6 then it should be modified to 1->2->3->5->6.If the input linked list is NULL or has 1 node,
then it should return NULL
'''


class Node:
	
	def __init__(self):
		
		self.data = 0
		self.next = None

def deleteMiddle(head):
        if head.next == None:
            return None
        
        count = 0
        p1 = p2 = head
        
        while p1:
            count += 1
            p1 = p1.next
        
        middle_index = count // 2
        
        for _ in range(middle_index - 1):
            p2 = p2.next
        
        p2.next = p2.next.next
        return head


def printList(ptr):

	while (ptr != None):
		print(ptr.data, end = '->')
		ptr = ptr.next
	
	print('NULL')

def newNode(data):

	temp = Node()
	temp.data = data
	temp.next = None
	return temp

# Driver Code
if __name__=='__main__':
	
	# Start with the empty list
	head = newNode(1)
	head.next = newNode(2)
	head.next.next = newNode(3)
	head.next.next.next = newNode(4)
	head.next.next.next.next = newNode(5)

	print("Given Linked List")
	printList(head)

	head = deleteMiddle(head)

	print("Linked List after deletion of middle")
	printList(head)
	


'''
Q2. Given a linked list of N nodes. The task is to check if the linked list has a loop. Linked list can contain self loop.
'''


class newNode:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None


def printList(head):
	while (head != None):
		print(head.key, end=" ")
		head = head.next

	print()


def detectLoop(head):
	temp = ""
	while (head != None):
		if (head.next == None):
			return False

		if (head.next == temp):
			return True

		next = head.next

		head.next = temp

		head = next

	return False


# Driver Code
head = newNode(1)
head.next = newNode(8)
head.next.next = newNode(3)
head.next.next.next = newNode(4)

# loop (4 has address of 1)
head.next.next.next.next = head

found = detectLoop(head)
if (found):
	print("Loop Found")
else:
	print("No Loop")



'''
Q3. Given a linked list consisting of L nodes and given a number N. The task is to find the Nth node from the end of the linked list.
'''


class Node:
	def __init__(self, new_data):
		self.data = new_data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def printNthFromLast(self, L):
		temp = self.head 

		count = 0
		while temp is not None:
			temp = temp.next
			count += 1

		if L > count:
			print('-1')
			return
		temp = self.head
		for i in range(0, count - L):
			temp = temp.next
		print(temp.data)


# Driver's Code
if __name__ == "__main__":
	llist = LinkedList()
	llist.push(9)
	llist.push(8)
	llist.push(7)
	llist.push(6)
	llist.push(5)
	llist.push(4)
	llist.push(3)
	llist.push(2)
	llist.push(1)
	
	L = 2

	llist.printNthFromLast(L)


'''
Q4. Given a singly linked list of characters, write a function that returns true if the given list is a palindrome, else false.
'''

class Node:
	def __init__(self, data):

		self.data = data
		self.ptr = None


def ispalindrome(head):

	temp = head

	stack = []

	ispalin = True

	while temp != None:
		stack.append(temp.data)

		temp = temp.ptr

	while head != None:

		i = stack.pop()

		if head.data == i:
			ispalin = True
		else:
			ispalin = False
			break

		head = head.ptr

	return ispalin



one = Node("R")
two = Node("A")
three = Node("D")
four = Node("A")
five = Node("R")

one.ptr = two
two.ptr = three
three.ptr = four
four.ptr = five

result = ispalindrome(one)

print("isPalindrome:", result)


'''
Q5. Given a linked list of **N** nodes such that it may contain a loop.
A loop here means that the last node of the link list is connected to the node at position X(1-based index).
If the link list does not have any loop, X=0.
Remove the loop from the linked list, if it is present, i.e. unlink the last node which is forming the loop.
'''


# Python program to detect and remove loop in linked list

# Node class
class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	def detectAndRemoveLoop(self):
		slow_p = fast_p = self.head
		
		while(slow_p and fast_p and fast_p.next):
			slow_p = slow_p.next
			fast_p = fast_p.next.next

			# If slow_p and fast_p meet at some point then
			# there is a loop
			if slow_p == fast_p:
				self.removeLoop(slow_p)
		
				# Return 1 to indicate that loop is found
				return 1
		
		# Return 0 to indicate that there is no loop
		return 0

	# Function to remove loop
	# loop_node --> pointer to one of the loop nodes
	# head --> Pointer to the start node of the linked list
	def removeLoop(self, loop_node):
		ptr1 = loop_node
		ptr2 = loop_node
		
		# Count the number of nodes in loop
		k = 1
		while(ptr1.next != ptr2):
			ptr1 = ptr1.next
			k += 1

		# Fix one pointer to head
		ptr1 = self.head
		
		# And the other pointer to k nodes after head
		ptr2 = self.head
		for i in range(k):
			ptr2 = ptr2.next

		# Move both pointers at the same place
		# they will meet at loop starting node
		while(ptr2 != ptr1):
			ptr1 = ptr1.next
			ptr2 = ptr2.next

		# Get pointer to the last node
		while(ptr2.next != ptr1):
			ptr2 = ptr2.next

		# Set the next node of the loop ending node
		# to fix the loop
		ptr2.next.next = None

	# Function to insert a new node at the beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# Utility function to print the LinkedList
	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data, end = ' ')
			temp = temp.next


# Driver program
llist = LinkedList()
llist.push(4)
llist.push(3)
llist.push(1)

llist.head.next.next.next= llist.head

llist.detectAndRemoveLoop()

print("Linked List after removing loop")
llist.printList()
	

'''
Q6. Given a linked list and two integers M and N. Traverse the linked list such that you retain M nodes then delete next N nodes,
continue the same till end of the linked list.
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
			print (temp.data,end=" ")
			temp = temp.next

	def skipMdeleteN(self, M, N):
		curr = self.head
		
		while(curr):
			for count in range(1, M):
				if curr is None:
					return
				curr = curr.next
					
			if curr is None :
				return

			t = curr.next
			for count in range(1, N+1):
				if t is None:
					break
				t = t.next
	
			curr.next = t
			curr = t

llist = LinkedList()
M = 3
N = 2
llist.push(10)
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print ("M = %d, N = %d\nGiven Linked List is:" %(M, N))
llist.printList()
print()

llist.skipMdeleteN(M, N)

print ("\nLinked list after deletion is")
llist.printList()



'''
Q7. Given two linked lists, insert nodes of second list into first list at alternate positions of first list.
For example, if first list is 5->7->17->13->11 and second is 12->10->2->4->6, the first list should become 5->12->7->10->17->2->13->4->11->6
and second list should become empty. The nodes of second list should only be inserted when there are positions available.
For example, if the first list is 1->2->3 and second list is 4->5->6->7->8, then first list should become 1->4->2->5->3->6
and second list to 7->8.

Use of extra space is not allowed (Not allowed to create additional nodes), i.e., insertion must be done in-place.
Expected time complexity is O(n) where n is number of nodes in first list.
'''

class Node(object):
	def __init__(self, data:int):
		self.data = data
		self.next = None


class LinkedList(object):
	def __init__(self):
		self.head = None
		
	def push(self, new_data:int):
		new_node = Node(new_data)
		new_node.next = self.head
		
		self.head = new_node
		
	def printList(self):
		temp = self.head
		while temp != None:
			print(temp.data)
			temp = temp.next
			
	def merge(self, p, q):
		p_curr = p.head
		q_curr = q.head

		while p_curr != None and q_curr != None:

			p_next = p_curr.next
			q_next = q_curr.next

			q_curr.next = p_next
			p_curr.next = q_curr

			p_curr = p_next
			q_curr = q_next
			q.head = q_curr



llist1 = LinkedList()
llist2 = LinkedList()


llist1.push(3)
llist1.push(2)
llist1.push(1)

for i in range(8, 3, -1):
	llist2.push(i)

print("First Linked List:")
llist1.printList()

print("Second Linked List:")
llist2.printList()

llist1.merge(p=llist1, q=llist2)

print("Modified first linked list:")
llist1.printList()

print("Modified second linked list:")
llist2.printList()



'''
Q8. Given a singly linked list, find if the linked list is circular or not.
A linked list is called circular if it is not NULL-terminated and all nodes are connected in the form of a cycle.
Below is an example of a circular linked list.
'''


class Node:

	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:

	def __init__(self):
		self.head = None


def Circular(head):
	if head == None:
		return True

	node = head.next
	i = 0

	while((node is not None) and (node is not head)):
		i = i + 1
		node = node.next

	return(node == head)


if __name__ == '__main__':
	llist = LinkedList()
	llist.head = Node(10)
	second = Node(12)
	third = Node(14)
	fourth = Node(16)

	llist.head.next = second
	second.next = third
	third.next = fourth
	fourth.next = llist.head

	if (Circular(llist.head)):
		print('Yes')
	else:
		print('No')
