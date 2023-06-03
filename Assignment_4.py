'''
Q1. Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order,
    return a sorted array of only the integers that appeared in all three arrays.
'''


def findCommon(ar1, ar2, ar3, n1, n2, n3):

	i, j, k = 0, 0, 0

	while (i < n1 and j < n2 and k < n3):

		if (ar1[i] == ar2[j] and ar2[j] == ar3[k]):
			print (ar1[i]),
			i += 1
			j += 1
			k += 1

		elif ar1[i] < ar2[j]:
			i += 1

		elif ar2[j] < ar3[k]:
			j += 1

		else:
			k += 1


ar1 = [1, 5, 5]
ar2 = [3, 4, 5, 5, 10]
ar3 = [5, 5, 10, 20]
n1 = len(ar1)
n2 = len(ar2)
n3 = len(ar3)
print ("Common elements are", findCommon(ar1, ar2, ar3, n1, n2, n3))



'''
Q2. Given two **0-indexed** integer arrays nums1 and nums2, return *a list* answer *of size* 2 *where:*

- answer[0] *is a list of all **distinct** integers in* nums1 *which are **not** present in* nums2*.*
- answer[1] *is a list of all **distinct** integers in* nums2 *which are **not** present in* nums1.

**Note** that the integers in the lists may be returned in **any** order.
'''


def findDifference(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    return [list(set1.difference(set2)), list(set2.difference(set1))]

nums1 = [1,2,3]
nums2 = [2,4,6]
print(findDifference(nums1, nums2))

'''
Q3. Given a 2D integer array matrix, return *the **transpose** of* matrix.

The **transpose** of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

'''

N = 4
def transpose(A, B):
  for i in range(N):
        for j in range(N):
            B[i][j] = A[j][i]
  
  
A = [[1, 1, 1, 1],
       [2, 2, 2, 2],
       [3, 3, 3, 3],
       [4, 4, 4, 4]]
  
  
B = [[0 for x in range(N)] for y in range(N)]

transpose(A, B)
  
print("Result matrix is")
for i in range(N):
    for j in range(N):
        print(B[i][j], " ", end='')
    print()


'''
Q4. Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn)
    such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.
'''

def arrayPairSum(nums):
    nums.sort()
    result = 0
    numsLen = len(nums)
    for i in range(0, numsLen - 1, 2):
        result += nums[i]
    return result

nums = [3,6,4,8]
print(arrayPairSum(nums))

'''
Q5. You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase **may be** incomplete.

Given the integer n, return *the number of **complete rows** of the staircase you will build*.

'''

def arrangeCoins(n):
    j=0
    while(n>j):
        j = j+1
        n = n-j
    return j

n = 9
print(arrangeCoins(n))


'''
Q6. Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
'''

def sortSquare(arr, n):
    for i in range(n):
        arr[i]= arr[i] * arr[i]
    arr.sort()
 
arr = [-6, -3, -1, 2, 4, 5]
n = len(arr)
 
print("Before sort")
for i in range(n):
    print(arr[i], end = " ")
 
print("\n")
 
sortSquare(arr, n)
 
print("After sort")
for i in range(n):
    print(arr[i], end = " ")



'''
Q7. You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

Count and return *the number of maximum integers in the matrix after performing all the operations*

'''

def maxCount(m, n, ops):
    length = len(ops)
    if length == 0:
        return m*n
    result = [ops[0][0] , ops[0][1]]
    for i in range(1,length):
        result[0] = min(result[0] , ops[i][0])
        result[1] = min(result[1] , ops[i][1])
    return result[0]*result[1] 

m = 3
n = 3
ops = [[2,2],[3,3]]
print(maxCount(m,n,ops))

'''
Q8. Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

*Return the array in the form* [x1,y1,x2,y2,...,xn,yn].
'''

def shuffleArray(a, n):
 
    i, q, k = 0, 1, n
    while(i < n):    
        j = k
        while(j > i + q):
            a[j - 1], a[j] = a[j], a[j - 1]
            j -= 1
        i += 1
        k += 1
        q += 1
 
a = [1, 3, 5, 7, 2, 4, 6, 8]
n = len(a)
shuffleArray(a, int(n / 2))
for i in range(0, n):
    print(a[i], end = " ")