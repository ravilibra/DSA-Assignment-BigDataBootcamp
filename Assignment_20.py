
'''
Q1. Given a binary tree, your task is to find subtree with maximum sum in tree.
'''

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findMaxSumSubtree(node, ans):

    if node is None:
        return 0
    
    left_sum = findMaxSumSubtree(node.left, ans)
    right_sum = findMaxSumSubtree(node.right, ans)
    
    current_sum = node.value + left_sum + right_sum
    
    ans[0] = max(ans[0], current_sum)
    
    
    return current_sum

def findMaxSubtreeSum(root):
    if (root == None):    
        return 0
    
    ans = [-999999999999]

    findMaxSumSubtree(root, ans)

    return ans[0]

# Create the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Find the subtree with maximum sum
max_sum = findMaxSubtreeSum(root)
print("Maximum subtree sum:", max_sum)


'''
Q2. Construct the BST (Binary Search Tree) from its given level order traversal.
'''

import math

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


def getNode(data):

	newNode = Node(data)

	newNode.data = data
	newNode.left = None
	newNode.right = None
	return newNode


def LevelOrder(root, data):
	if(root == None):
		root = getNode(data)
		return root

	if(data <= root.data):
		root.left = LevelOrder(root.left, data)
	else:
		root.right = LevelOrder(root.right, data)
	return root


def constructBst(arr, n):
	if(n == 0):
		return None
	root = None

	for i in range(0, n):
		root = LevelOrder(root, arr[i])

	return root


def inorderTraversal(root):
	if (root == None):
		return None

	inorderTraversal(root.left)
	print(root.data, end=" ")
	inorderTraversal(root.right)


if __name__ == '__main__':

	arr = [7, 4, 12, 3, 6, 8, 1, 5, 10]
	n = len(arr)

	root = constructBst(arr, n)

	print("Inorder Traversal: ", end="")
	root = inorderTraversal(root)
	

'''
Q3. Given an array of size n. The problem is to check whether the given array can represent the level order traversal of a
Binary Search Tree or not.
'''


INT_MIN, INT_MAX = float('-inf'), float('inf')
 
class NodeDetails:
 
    def __init__(self, data, min, max):
        self.data = data
        self.min = min
        self.max = max
 
def levelOrderIsOfBST(arr, n):
 
    if n == 0:
        return True
     
    q = []
     
    i = 0
     
    newNode = NodeDetails(arr[i], INT_MIN, INT_MAX)
    i += 1
    q.append(newNode)
     
    while i != n and len(q) != 0:    
     
        temp = q.pop(0)
         
        if i < n and (arr[i] < temp.data and
                    arr[i] > temp.min):
         
            newNode = NodeDetails(arr[i], temp.min, temp.data)
            i += 1
            q.append(newNode)            
         
        if i < n and (arr[i] > temp.data and
                    arr[i] < temp.max):
         
            newNode = NodeDetails(arr[i], temp.data, temp.max)
            i += 1
            q.append(newNode)        
                 
    if i == n:
        return True
         
    return False       
 
if __name__ == "__main__":
 
    arr = [7, 4, 12, 3, 6, 8, 1, 5, 10]
    n = len(arr)    
    if levelOrderIsOfBST(arr, n):
        print("Yes")
    else:
        print("No")

