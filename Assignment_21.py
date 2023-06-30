
'''
Q1. You are given a binary tree. The binary tree is represented using the TreeNode class. Each TreeNode has an integer value and left and
right children, represented using the TreeNode class itself. Convert this binary tree into a binary search tree.
'''


class Node:
     
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def storeInorder(root, inorder):
     
    if root is None:
        return
     
    storeInorder(root.left, inorder)
     
    inorder.append(root.data)
 
    storeInorder(root.right, inorder)
 
def countNodes(root):
    if root is None:
        return 0
 
    return countNodes(root.left) + countNodes(root.right) + 1
 
def arrayToBST(arr, root):
 
    if root is None:
        return
     
    arrayToBST(arr, root.left)
 
    root.data = arr[0]
    arr.pop(0)
 
    arrayToBST(arr, root.right)
 
def binaryTreeToBST(root):
     
    if root is None:
        return
     
    n = countNodes(root)
 
    arr = []
    storeInorder(root, arr)
     
    arr.sort()
 
    arrayToBST(arr, root)
 
def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print (root.data,end=" ")
    printInorder(root.right)
 
root = Node(10)
root.left = Node(2)
root.right = Node(8)
root.left.left = Node(7)
root.right.right = Node(4)
 
binaryTreeToBST(root)
 
print(printInorder(root))



'''
Q2. Given a Binary Search Tree with all unique values and two keys. Find the distance between two nodes in BST. The given keys always
exist in BST.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
 
def pathToNode(root, path, k):
 
    if root is None:
        return False
 
    path.append(root.data)
  
    if root.data == k :
        return True
  
    if ((root.left != None and pathToNode(root.left, path, k)) or
            (root.right!= None and pathToNode(root.right, path, k))):
        return True
  
    path.pop()
    return False
 
def distance(root, data1, data2):
    if root:
        path1 = []
        pathToNode(root, path1, data1)
 
        path2 = []
        pathToNode(root, path2, data2)
 
        i=0
        while i<len(path1) and i<len(path2):
            if path1[i] != path2[i]:
                break
            i = i+1
 
        return (len(path1)+len(path2)-2*i)
    else:
        return 0
 
root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.right.right = Node(14)
root.left.right = Node(6)
root.right.right.left = Node(13)
 
print(distance(root, 6, 14))


'''
Q3. Write a program to convert a binary tree to a doubly linked list.
'''


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
  
prev = None
  
def BinaryTree2DoubleLinkedList(root):
      
    if root is None:
        return root
              
    head = BinaryTree2DoubleLinkedList(root.left);
      
    global prev
      
    if prev is None : 
        head = root
          
    else:
        root.left = prev
        prev.right = root
      
    prev = root; 
      
    BinaryTree2DoubleLinkedList(root.right)
      
    return head
  
def print_dll(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.right
  
  
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(5)
    root.right = Node(20)
    root.right.right = Node(35)
    root.right.left = Node(30)
      
    head = BinaryTree2DoubleLinkedList(root)
      
    print_dll(head)



'''
Q4. Write a program to connect nodes at the same level.
'''

class newnode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = self.nextRight = None
 
 
def connect(root):
 
    if root is None:
        return
 
    queue = []
    queue.append(root)
    while len(queue) != 0:
 
        size = len(queue)
 
        prev = newnode(None)
        for i in range(size):
            temp = queue.pop(0)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
            if prev != None:
                prev.nextRight = temp
                prev = temp
        prev.nextRight = None
 
 
if __name__ == '__main__':
 
    root = newnode(1)
    root.left = newnode(2)
    root.right = newnode(3)
    root.left.left = newnode(4)
    root.left.right = newnode(5)
    root.right.left = newnode(6)
    root.right.right = newnode(7)
 
    connect(root)
 
    print(root.data, "-> ", end="")
    if root.nextRight:
        print(root.nextRight.data)
    else:
        print(-1)
    print(root.left.data, "-> ", end="")
    if root.left.nextRight:
        print(root.left.nextRight.data)
    else:
        print(-1)
    print(root.right.data, "-> ", end="")
    if root.right.nextRight:
        print(root.right.nextRight.data)
    else:
        print(-1)
    print(root.left.left.data, "-> ", end="")
    if root.left.left.nextRight:
        print(root.left.left.nextRight.data)
    else:
        print(-1)
    print(root.left.right.data, "-> ", end="")
    if root.left.right.nextRight:
        print(root.left.right.nextRight.data)
    else:
        print(-1)
    print(root.right.left.data, "-> ", end="")
    if root.right.left.nextRight:
        print(root.right.left.nextRight.data)
    else:
        print(-1)
    print(root.right.right.data, "-> ", end="")
    if root.right.right.nextRight:
        print(root.right.right.nextRight.data)
    else:
        print(-1)