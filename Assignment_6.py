
'''
Q1. A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

- s[i] == 'I' if perm[i] < perm[i + 1], and
- s[i] == 'D' if perm[i] > perm[i + 1].

Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return **any of them**.
'''

import shutil


def diStringMatch(S):
    lo, hi = 0, len(S)
    ans = []
    for x in S:
        if x == 'I':
            ans.append(lo)
            lo += 1
        else:
            ans.append(hi)
            hi -= 1

    return ans + [lo]

S =  "IDID"
print(diStringMatch(S))


'''
Q2. You are given an m x n integer matrix matrix with the following two properties:

- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true *if* target *is in* matrix *or* false *otherwise*.

You must write a solution in O(log(m * n)) time complexity.

'''

M = 3
N = 4

def binarySearch1D(arr, target):
	low = 0
	high = N - 1
	while (low <= high):
		mid = low + int((high - low) / 2)

		if (arr[mid] == target):
			return True

		if (arr[mid] < target):
			low = mid + 1
		else:
			high = mid - 1

	return False

def searchMatrix(matrix, target):
	low = 0
	high = M - 1
	while (low <= high):
		mid = low + int((high - low) / 2)

		if (target >= matrix[mid][0] and
			target <= matrix[mid][N - 1]):
			return binarySearch1D(matrix[mid], target)

		if (target < matrix[mid][0]):
			high = mid - 1
		else:
			low = mid + 1

	return False

if __name__ == '__main__':
	matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
	target = 3
	if (searchMatrix(matrix, target)):
		print("True")
	else:
		print("False")


'''
Q3. Given an array of integers arr, return *true if and only if it is a valid mountain array*.

Recall that arr is a mountain array if and only if:

- arr.length >= 3
- There exists some i with 0 < i < arr.length - 1 such that:
    - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
'''

def isMountainArray(arr):
 
    if (len(arr) < 3):
        return False
    flag = 0
    i = 0
    for i in range(1, len(arr)):
        if (arr[i] <= arr[i - 1]):
            break
 
    if (i == len(arr) or i == 1):
        return False
 
    while i < len(arr):
        if (arr[i] >= arr[i - 1]):
            break
        i += 1
    return i == len(arr)
 
if __name__ == "__main__":
 
    arr = [1, 2]
    if (isMountainArray(arr)):
        print("true")
    else:
        print("false")


'''
Q4. Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
'''


def findSubArray(arr, n):

	sum = 0
	count = -1

	for i in range(0, n-1):
	
		sum = -1 if(arr[i] == 0) else 1

		for j in range(i + 1, n):
		
			sum = sum + (-1) if (arr[j] == 0) else sum + 1

			if (sum == 0 and count < j-i + 1):
				
				count = j - i + 1
				startindex = i
			
		
	
	if (count == -1):
		print("No such subarray");
	else:
		print(count);

	return count

arr = [1, 0, 1, 1, 1, 0, 0]
size = len(arr)
findSubArray(arr, size)


'''
Q5. The **product sum** of two equal-length arrays a and b is equal to the sum of a[i] * b[i] for all 0 <= i < a.length (**0-indexed**).

- For example, if a = [1,2,3,4] and b = [5,2,3,1], the **product sum** would be 1*5 + 2*2 + 3*3 + 4*1 = 22.

Given two arrays nums1 and nums2 of length n, return *the **minimum product sum** if you are allowed to **rearrange** the **order** of the elements in* nums1.
'''


def minValue(nums1, nums2, n):
	nums1.sort()
	nums2.sort()

	result = 0
	for i in range(n):
		result += (nums1[i] * nums2[n - i - 1])

	return result


nums1 = [5,3,4,2]
nums2 = [4,2,2,5]
n = len(nums1)
print (minValue(nums1, nums2, n))


'''
Q6. An integer array original is transformed into a **doubled** array changed by appending **twice the value** of every element in original, and then randomly **shuffling** the resulting array.

Given an array changed, return original *if* changed *is a **doubled** array. If* changed *is not a **doubled** array, return an empty array. The elements in* original *may be returned in **any** order*.
'''


def findOriginal(arr):

	numFreq = {}

	for i in range(0, len(arr)):
		if (arr[i] in numFreq):
			numFreq[arr[i]] += 1
		else:
			numFreq[arr[i]] = 1

	arr.sort()

	res = []

	for i in range(0, len(arr)):
	
		freq = numFreq[arr[i]]
		if (freq > 0):
		
			res.append(arr[i])

			numFreq[arr[i]] -= 1

			twice = 2 * arr[i]

			numFreq[twice] -= 1

	return res

arr = [1,3,4,2,6,8]
res = findOriginal(arr)

for i in range(0, len(res)):
	print(res[i], end=" ")


'''
Q7. Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
'''


def generateMatrix(n):
    matrix = [[0] * n for _ in range(n)]
    num = 1
    row = 0
    col = 0
    direction = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    while num <= n * n:
        matrix[row][col] = num
        num += 1
        nextRow = row + dr[direction]
        nextCol = col + dc[direction]
        if nextRow < 0 or nextRow >= n or nextCol < 0 or nextCol >= n or matrix[nextRow][nextCol] != 0:
            direction = (direction + 1) % 4
        row += dr[direction]
        col += dc[direction]
    return matrix

n = 3
print(generateMatrix(n))



'''
Q8. Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.
'''

def multiply(mat1, mat2):
    ret = [[0 for j in range(len(mat2[0]))] for i in range(len(mat1))]

    for i, row in enumerate(mat1):
      for k, a in enumerate(row):
        if a:
          for j, b in enumerate(mat2[k]):
            if b:
              ret[i][j] += a * b
    return ret

mat1 = [[1,0,0],[-1,0,3]]
mat2 = [[7,0,0],[0,0,0],[0,0,1]]
print(multiply(mat1, mat2))