
'''
Q1. Given an array, for each element find the value of the nearest element to the right which is having a frequency greater than that
of the current element. If there does not exist an answer for a position, then make the value ‘-1’.
'''

def NFG(a, n):
 
    if (n <= 0):
        print("List empty")
        return []
 
    stack = [0]*n
 
    freq = {}
    for i in a:
        freq[a[i]] = 0
    for i in a:
        freq[a[i]] += 1
 
    res = [0]*n
 
    top = -1
 
    top += 1
    stack[top] = 0
 
    for i in range(1, n):
        if (freq[a[stack[top]]] > freq[a[i]]):
            top += 1
            stack[top] = i
 
        else:
 
            while (top > -1 and freq[a[stack[top]]] < freq[a[i]]):
                res[stack[top]] = a[i]
                top -= 1
 
            top += 1
            stack[top] = i
 
    while (top > -1):
        res[stack[top]] = -1
        top -= 1
    return res
 
a = [1, 1, 2, 3, 4, 2, 1]
n = 7
print(NFG(a, n))


'''
Q2. Given a stack of integers, sort it in ascending order using another temporary stack.
'''

def sortStack ( stack ):
    tmpStack = createStack()
    while(isEmpty(stack) == False):
         
        tmp = top(stack)
        pop(stack)
 
        while(isEmpty(tmpStack) == False and
             int(top(tmpStack)) < int(tmp)):
             
            push(stack,top(tmpStack))
            pop(tmpStack)
 
        push(tmpStack,tmp)
     
    return tmpStack
 
def createStack():
    stack = []
    return stack
def isEmpty( stack ):
    return len(stack) == 0
 
def push( stack, item ):
    stack.append( item )
 
def top( stack ):
    p = len(stack)
    return stack[p-1]
 
def pop( stack ):
 
    if(isEmpty( stack )):
        print("Stack Underflow ")
        exit(1)
 
    return stack.pop()
 
def prints(stack):
    for i in range(len(stack)-1, -1, -1):
        print(stack[i], end = ' ')
    print()
 
stack = createStack()
push( stack, str(34) )
push( stack, str(3) )
push( stack, str(31) )
push( stack, str(98) )
push( stack, str(92) )
push( stack, str(23) )
 
print("Sorted numbers are: ")
sortedst = sortStack ( stack )
prints(sortedst)


'''
Q3. Given a stack with push(), pop(), and empty() operations, The task is to delete the middle element of it without using any
additional data structure.
'''


import math

st = []
st.append('1')
st.append('2')
st.append('3')
st.append('4')
st.append('5')

v = []

while(len(st) > 0):
	v.append(st[0])
	del st[0]
	
n = len(v)

if n%2==0:
	target = math.floor(n/2)
	for i in range(0, n):
		if i==target:
			continue
		st.append(v[i])
else:
	target = math.floor(n/2)
	for i in range(0, n):
		if i==target:
			continue
		st.append(v[i])

print("Printing stack after deletion of middle:", end = " ")

while (len(st) > 0):
	p = st[0]
	del st[0]
	print(p, end = " ")


'''
Q4. Given a Queue consisting of first **n** natural numbers (in random order). The task is to check whether the given Queue elements can be arranged in increasing order in another Queue using a stack. The operation allowed are:

1. Push and pop elements from the stack
2. Pop (Or Dequeue) from the given Queue.
3. Push (Or Enqueue) in the another Queue.
'''

from queue import Queue
 
def checkSorted(n, q):
    st = []
    expected = 1
    fnt = None
 
    while (not q.empty()):
        fnt = q.queue[0]
        q.get()
 
        if (fnt == expected):
            expected += 1
 
        else:
             
            if (len(st) == 0):
                st.append(fnt)
 
            elif (len(st) != 0 and st[-1] < fnt):
                return False
 
            else:
                st.append(fnt)
 
        while (len(st) != 0 and
                   st[-1] == expected):
            st.pop()
            expected += 1
 
    if (expected - 1 == n and len(st) == 0):
        return True
 
    return False
 
if __name__ == '__main__':
    q = Queue()
    q.put(5)
    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)
 
    n = q.qsize()
 
    if checkSorted(n, q):
        print("Yes")
    else:
        print("No")


'''
Q5. Given a number , write a program to reverse this number using stack.
'''


stack = []
 
def push_digits(number):
 
    while (number != 0):
        stack.append(number % 10)
        number = int(number / 10)
 
def reverse_number(number):
     
    push_digits(number)
     
    reverse = 0
    i = 1
     
    while (len(stack) > 0):
        reverse = reverse + (stack[len(stack) - 1] * i)
        stack.pop()
        i = i * 10
     
    return reverse
 
number = 6899
 
print(reverse_number(number))


'''
Q6. Given an integer k and a **[queue] of integers, The task is to reverse the order of the first **k** elements of the queue, leaving the other elements in the same relative order.

Only following standard operations are allowed on queue.

- **enqueue(x) :** Add an item x to rear of queue
- **dequeue() :** Remove an item from front of queue
- **size() :** Returns number of elements in queue.
- **front() :** Finds front item.
'''


from collections import deque

def reverse_first_k(q, k):
	solve(q, k)
	s = len(q) - k
	for _ in range(s):
		x = q.popleft()
		q.append(x)
	return q

def solve(q, k):
	if k == 0:
		return
	e = q.popleft()
	solve(q, k - 1)
	q.append(e)

queue = deque([57, 65, 25, 84, 35, 47, 16, 35, 62, 42])
k = 5
queue = reverse_first_k(queue, k)

while queue:
	print(queue.popleft(), end=' ')



'''
Q7. Given a sequence of n strings, the task is to check if any two similar words come together and then destroy each other then print the
number of words left in the sequence after this pairwise destruction.
'''

def removeConsecutiveSame(v):
 
    n = len(v)
    i = 0
    while(i < n - 1):
         
        if ((i + 1) < len(v)) and (v[i] == v[i + 1]) :
         
            v = v[:i]
            v = v[:i]
            if (i > 0):
                i -= 1
    
            n = n - 2
        else:
            i += 1
    return len(v[:i - 1])
     
if __name__ == '__main__':
    v = ["tom", "jerry", "jerry", "tom"]
    print(removeConsecutiveSame(v))



'''
Q8. Given an array of integers, the task is to find the maximum absolute difference between the nearest left and the right smaller
element of every element in the array.

**Note:** If there is no smaller element on right side or left side of any element then we take zero as the smaller element.
For example for the leftmost element, the nearest smaller element on the left side is considered as 0.Similarly, for rightmost elements, the smaller element on the right side is considered as 0.
'''

def leftsmaller(arr, n, SE):
 
    sta = []
    for i in range(n):
         
        while(sta != [] and sta[len(sta)-1] >= arr[i]):
            sta.pop()
 
        if(sta != []):
            SE[i]=sta[len(sta)-1]
        else:
            SE[i]=0
 
        sta.append(arr[i])
 
def findMaxDiff(arr, n):
    ls=[0]*n
    rs=[0]*n
 
    leftsmaller(arr, n, ls)
     
    leftsmaller(arr[::-1], n, rs)
 
    res = -1
    for i in range(n):
        res = max(res, abs(ls[i] - rs[n-1-i]))
    return res
 
     
if __name__=='__main__':
    arr = [2, 4, 8, 7, 7, 9, 3]
    print ("Maximum Diff :",(findMaxDiff(arr, len(arr))))

