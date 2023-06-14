
'''
Q1. Given two linked list of the same size, the task is to create a new linked list using those linked lists.
The condition is that the greater node among both linked list will be added to the new linked list.
'''

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

def insert(root, item):
    temp = Node(0)
    temp.data = item
    temp.next = None

    if (root == None):
        root = temp
    else:
        curr = root
        while (curr.next != None):
            curr = curr.next
        curr.next = temp

    return root


def newList(root1, root2):
    curr1 = root1
    curr2 = root2

    root = None
    while (curr1 != None):
        temp = Node(0)
        temp.next = None

        if (curr1.data < curr2.data):
            temp.data = curr2.data
        else:
            temp.data = curr1.data

        if (root == None):
            root = temp
        else:
            curr = root
            while (curr.next != None):
                curr = curr.next

            curr.next = temp
        
        curr1 = curr1.next
        curr2 = curr2.next
    
    return root

def display(root):
 
    while (root != None) :
        print(root.data, "->", end = " ")
        root = root.next
     
    print(" ");
 
# Driver Code
if __name__=='__main__':
 
    root1 = None
    root2 = None
    root = None
 
    # First linked list
    root1 = insert(root1, 5)
    root1 = insert(root1, 2)
    root1 = insert(root1, 3)
    root1 = insert(root1, 8)
 
    print("First List: ", end = " ")
    display(root1)
 
    # Second linked list
    root2 = insert(root2, 1)
    root2 = insert(root2, 7)
    root2 = insert(root2, 4)
    root2 = insert(root2, 5)
 
    print("Second List: ", end = " ")
    display(root2)
 
    root = newList(root1, root2)
    print("New List: ", end = " ")
    display(root)


'''
Q2. Write a function that takes a list sorted in non-decreasing order and deletes any duplicate nodes from the list. The list should only be traversed once.

For example if the linked list is 11->11->11->21->43->43->60 then removeDuplicates() should convert the list to 11->21->43->60. 
'''


class Node:

	# Constructor to initialize
	# the node object
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

	def deleteNode(self, key):

		temp = self.head

		if (temp is not None):
			if (temp.data == key):
				self.head = temp.next
				temp = None
				return

		while(temp is not None):
			if temp.data == key:
				break
			prev = temp
			temp = temp.next

		if(temp == None):
			return

		prev.next = temp.next

		temp = None

	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data, end= " ")
			temp = temp.next

	def removeDuplicates(self):
		temp = self.head
		if temp is None:
			return
		while temp.next is not None:
			if temp.data == temp.next.data:
				new = temp.next.next
				temp.next = None
				temp.next = new
			else:
				temp = temp.next
		return self.head


# Driver Code
llist = LinkedList()

llist.push(20)
llist.push(13)
llist.push(13)
llist.push(11)
llist.push(11)
llist.push(11)
print("Created Linked List: ")
llist.printList()
print()
print("Linked List after removing",
	"duplicate elements:")
llist.removeDuplicates()
llist.printList()


'''
Q3. Given a linked list of size N. The task is to reverse every k nodes (where k is an input to the function) in the linked list.
If the number of nodes is not a multiple of k then left-out nodes, in the end, should be considered as a group and must be reversed (See Example 2 for clarification).
'''


class Node:
  
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
  
  
class LinkedList:
  
    def __init__(self):
        self.head = None
  
    def reverse(self, head, k):
        
        if head == None:
          return None
        current = head
        next = None
        prev = None
        count = 0
  
        while(current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
  
  
        if next is not None:
            head.next = self.reverse(next, k)
  
        return prev
  
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
  
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end=' ')
            temp = temp.next
  
  
llist = LinkedList()
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
  
print("Given linked list")
llist.printList()
k = 4
llist.head = llist.reverse(llist.head, k)
  
print ("\nReversed Linked list")
llist.printList()


'''
Q4. Given a linked list, write a function to reverse every alternate k nodes (where k is an input to the function) in an efficient way.
Give the complexity of your algorithm.
'''


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

def kAltReverse(head, k) :
	current = head
	next = None
	prev = None
	count = 0

	while (current != None and count < k) :
		next = current.next
		current.next = prev
		prev = current
		current = next
		count = count + 1
	
	if(head != None):
		head.next = current

	count = 0
	while(count < k - 1 and current != None ):
		current = current.next
		count = count + 1
		
	if(current != None):
		current.next = kAltReverse(current.next, k)

	return prev

def push(head_ref, new_data):
	
	new_node = Node(new_data)


	new_node.next = head_ref

	head_ref = new_node
	
	return head_ref

def printList(node):
	count = 0
	while(node != None):
		print(node.data, end = " ")
		node = node.next
		count = count + 1
	
if __name__=='__main__':
	
	head = None

	for i in range(20, 0, -1):
		head = push(head, i)
		
	print("Given linked list ")
	printList(head)
	head = kAltReverse(head, 3)

	print("\nModified Linked list")
	printList(head)
	

'''
Q5. Given a linked list and a key to be deleted. Delete last occurrence of key from linked. The list may have duplicates.
'''

class Node:
	def __init__(self, new_data):
		
		self.data = new_data
		self.next = None

def deleteLast(head, x):

	temp = head
	ptr = None
	
	while (temp != None):
		
		if (temp.data == x):
			ptr = temp	
			
		temp = temp.next
	
	if (ptr != None and ptr.next == None):
		temp = head
		while (temp.next != ptr):
			temp = temp.next
			
		temp.next = None
	
	if (ptr != None and ptr.next != None):
		ptr.data = ptr.next.data
		temp = ptr.next
		ptr.next = ptr.next.next
		
	return head
	
def newNode(x):

	node = Node(0)
	node.data = x
	node.next = None
	return node

def display(head):

	temp = head
	
	if (head == None):
		print("NULL\n")
		return
	
	while (temp != None):
		print( temp.data," --> ", end = "")
		temp = temp.next
	
	print("NULL")

head = newNode(1)
head.next = newNode(2)
head.next.next = newNode(3)
head.next.next.next = newNode(5)
head.next.next.next.next = newNode(2)
head.next.next.next.next.next = newNode(10)

print("Created Linked list: ", end = '')
display(head)

k = 2
head = deleteLast(head, k)
print("List after deletion of", k, ": ", end = '')

display(head)


'''
Q6. Given two sorted linked lists consisting of N and M nodes respectively. The task is to merge both of the lists (in place) and return
the head of the merged list.
'''


class Node:
	def __init__(self, key):
		self.key = key
		self.next = None
		
def newNode(key):
	return Node(key)


a = Node(5)
a.next = Node(10)
a.next.next = Node(15)
a.next.next.next = Node(40)

b = Node(2)
b.next = Node(3)
b.next.next = Node(20)

v = []
while(a is not None):
	v.append(a.key)
	a = a.next

while(b is not None):
	v.append(b.key)
	b = b.next

v.sort()
result = Node(-1)
temp = result
for i in range(len(v)):
	result.next = Node(v[i])
	result = result.next

temp = temp.next
print("Resultant Merge Linked List is : ")
while(temp is not None):
	print(temp.key, end=" ")
	temp = temp.next


'''
Q7. Given a Doubly Linked List, the task is to reverse the given Doubly Linked List.
'''

class Node:
 
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
 
 
class DoublyLinkedList:
    def __init__(self):
        self.head = None
 
    def reverse(self):
        temp = None
        current = self.head
 
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
 
        if temp is not None:
            self.head = temp.prev
 
    def push(self, new_data):
 
        new_node = Node(new_data)
 
        new_node.next = self.head
 
        if self.head is not None:
            self.head.prev = new_node
 
        self.head = new_node
 
    def printList(self, node):
        while(node is not None):
            print(node.data, end=' ')
            node = node.next
 
 
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.push(2)
    dll.push(4)
    dll.push(8)
    dll.push(10)
 
    print("\nOriginal Linked List")
    dll.printList(dll.head)
 
    dll.reverse()
 
    print("\nReversed Linked List")
    dll.printList(dll.head)


'''
Q8. Given a doubly linked list and a position. The task is to delete a node from given position in a doubly linked list.
'''

class Node:
     
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
 
def deleteNode(head_ref, del_):
 
    if (head_ref == None or del_ == None):
        return
 
    if (head_ref == del_):
        head_ref = del_.next
 
    if (del_.next != None):
        del_.next.prev = del_.prev
 
    if (del_.prev != None):
        del_.prev.next = del_.next
         
    return head_ref
 
def deleteNodeAtGivenPos(head_ref,n):
 
    if (head_ref == None or n <= 0):
        return
 
    current = head_ref
    i = 1
 
    while ( current != None and i < n ):
        current = current.next
        i = i + 1
 
    if (current == None):
        return
 
    deleteNode(head_ref, current)
     
    return head_ref
 
def push(head_ref, new_data):
 
    new_node = Node(0)
 
    new_node.data = new_data
 
    new_node.prev = None
 
    new_node.next = (head_ref)
 
    if ((head_ref) != None):
        (head_ref).prev = new_node
 
    (head_ref) = new_node
     
    return head_ref
 
def printList(head):
 
    while (head != None) :
        print( head.data ,end= " ")
        head = head.next
     

head = None
 
head = push(head, 5)
head = push(head, 2)
head = push(head, 4)
head = push(head, 8)
head = push(head, 10)
 
print("Doubly linked list before deletion:")
printList(head)
 
n = 2
 
head = deleteNodeAtGivenPos(head, n)
 
print("\nDoubly linked list after deletion:")
 
printList(head)