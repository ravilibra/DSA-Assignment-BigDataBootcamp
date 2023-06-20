
'''
Q1. Given an array arr[ ] of size N having elements, the task is to find the next greater element for each element of the array in order
of their appearance in the array.Next greater element of an element in the array is the nearest element on the right which is greater
than the current element.If there does not exist next greater of current element, then next greater element for current element is -1.
For example, next greater of the last element is always -1.
'''

def NGE(arr):
 
    for i in range(0, len(arr)):
 
        next = -1
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                next = arr[j]
                break
 
        print(str(next))
 
 
arr = [11, 13, 21, 3]
NGE(arr)


'''
Q2. Given an array a of integers of length n, find the nearest smaller number for every element such that the smaller element is on left side.
If no small element present on the left print -1.
'''

def SEOL(arr):
    for i in range(0, len(arr)):
        pre = -1
        for j in range(i-1 ,-1, -1):
            if arr[i] > arr[j]:
                pre = arr[j]
                break
        print(str(pre))

arr = [1,4,3, 6, 2]
SEOL(arr)


'''
Q3. Implement a Stack using two queues q1 and q2.
'''

from _collections import deque
 
 
class Stack:
 
    def __init__(self):
 
        self.q1 = deque()
        self.q2 = deque()
 
    def push(self, x):
 
        self.q2.append(x)
 
        while (self.q1):
            self.q2.append(self.q1.pop())
 
        self.q1, self.q2 = self.q2, self.q1
 
    def pop(self):
 
        if self.q1:
            self.q1.pop()
 
    def top(self):
        if (self.q1):
            return self.q1[0]
        return None
 
    def size(self):
        return len(self.q1)
 
 
if __name__ == '__main__':
    s = Stack()
    s.push(2)
    s.push(3)
    s.pop()
    print(s.top())
    s.push(4)
    s.pop()
    print(s.top())


'''
Q4. You are given a stack St. You have to reverse the stack using recursion.
'''


def insertAtBottom(stack, item):
    if isEmpty(stack):
        push(stack, item)
    else:
        temp = pop(stack)
        insertAtBottom(stack, item)
        push(stack, temp)
 
 
def reverse(stack):
    if not isEmpty(stack):
        temp = pop(stack)
        reverse(stack)
        insertAtBottom(stack, temp)
 
def createStack():
    stack = []
    return stack

 
def isEmpty(stack):
    return len(stack) == 0
 
 
def push(stack, item):
    stack.append(item)

 
def pop(stack):
    if(isEmpty(stack)):
        print("Stack Underflow ")
        exit(1)
 
    return stack.pop()
 
 
 
def prints(stack):
    for i in range(len(stack)-1, -1, -1):
        print(stack[i], end=' ')
    print()
 
 
 
stack = createStack()
push(stack, str(6))
push(stack, str(7))
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
print("Original Stack ")
prints(stack)
 
reverse(stack)
 
print("Reversed Stack ")
prints(stack)


'''
Q5. You are given a string S, the task is to reverse the string using stack.
'''


def createStack():
    stack = []
    return stack
 
 
def size(stack):
    return len(stack)
 
 
def isEmpty(stack):
    if size(stack) == 0:
        return true
 
 
def push(stack, item):
    stack.append(item)
 
 
def pop(stack):
    if isEmpty(stack):
        return
    return stack.pop()
 
 
def reverse(string):
    n = len(string)

    stack = createStack()
 
    for i in range(0, n, 1):
        push(stack, string[i])
 
    string = ""

    for i in range(0, n, 1):
        string += pop(stack)
 
    return string
 

string = "GeeksforGeeks"
string = reverse(string)
print("Reversed string is " + string)


'''
Q6. Given string S representing a postfix expression, the task is to evaluate the expression and find the final value.
Operators will only include the basic arithmetic operators like *, /, + and -.
'''


def evaluate_postfix(expression):
    stack = []

    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2
            elif char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2

            stack.append(result)

    return stack.pop()


postfix_expression = "231*+9-"
result = evaluate_postfix(postfix_expression)
print("Output:", result)


'''
Q7. Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:

- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with `O(1)` time complexity for each function.
'''

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        # Update the minimum stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            val = self.stack.pop()

            # Update the minimum stack
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]


stack = MinStack()
stack.push(-2)
stack.push(0)
stack.push(-3)
print(stack.getMin())
stack.pop()
stack.top()
print(stack.getMin())


'''
Q8. Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after
raining.
'''


def maxWater(arr, n):
    res = 0
  
    for i in range(1, n - 1):
  
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])
  
        right = arr[i]
  
        for j in range(i + 1, n):
            right = max(right, arr[j])
  
        res = res + (min(left, right) - arr[i])
  
    return res
  
  
if __name__ == "__main__":
  
    arr = [0,1,0,2,1,0,1,3,2,1,2,]
    n = len(arr)
  
    print(maxWater(arr, n))