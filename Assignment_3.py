
'''
Q1. Given an integer array nums of length n and an integer target, find three integers
in nums such that the sum is closest to the target.
Return the sum of the three integers.

You may assume that each input would have exactly one solution.
'''


import sys

def solution(nums, x):
	
	closestSum = sys.maxsize
	
	for i in range (len(nums)) :
		for j in range(i + 1, len(nums)):
			for k in range(j + 1, len( nums)):
				
				if(abs(x - closestSum) > abs(x - (nums[i] + nums[j] + nums[k]))):
					closestSum = (nums[i] + nums[j] + nums[k])
					
	return closestSum

nums = [4, -3, 2, 5, -1, -1]
x = 7
print(solution(nums, x))



'''
Q2. Given an array nums of n integers, return an array of all the unique quadruplets
[nums[a], nums[b], nums[c], nums[d]] such that:
           ● 0 <= a, b, c, d < n
           ● a, b, c, and d are distinct.
           ● nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.
'''


class Pair:
	def __init__(self, x, y):
		self.index1 = x
		self.index2 = y

def GetQuadruplets(nums, target):
	map = {}

	for i in range(len(nums) - 1):
		for j in range(i + 1, len(nums)):
			sum = nums[i] + nums[j]

			if sum not in map:
				map[sum] = [Pair(i, j)]
			else:
				map[sum].append(Pair(i, j))

	ans = set()

	for i in range(len(nums) - 1):
		for j in range(i + 1, len(nums)):
			lookUp = target - (nums[i] + nums[j])

			if lookUp in map:
				temp = map[lookUp]

				for pair in temp:
					if pair.index1 != i and pair.index1 != j and pair.index2 != i and pair.index2 != j:
						l1 = [nums[pair.index1], nums[pair.index2], nums[i], nums[j]]
						
						l1.sort()
						
						ans.add(tuple(l1))

	print(*reversed(list(ans)), sep = '\n')

arr = [1, 0, -1, 0, -2, 2]
K = 0
GetQuadruplets(arr, K)




'''
Q3. A permutation of an array of integers is an arrangement of its members into a
sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr:
[1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].

The next permutation of an array of integers is the next lexicographically greater
permutation of its integer. More formally, if all the permutations of the array are
sorted in one container according to their lexicographical order, then the next
permutation of that array is the permutation that follows it in the sorted container.

If such an arrangement is not possible, the array must be rearranged as the
lowest possible order (i.e., sorted in ascending order).

● For example, the next permutation of arr = [1,2,3] is [1,3,2].
● Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
● While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not
have a lexicographical larger rearrangement.

Given an array of integers nums, find the next permutation of nums.
The replacement must be in place and use only constant extra memory.

'''


def swapPositions(list, pos1, pos2):
	list[pos1], list[pos2] = list[pos2], list[pos1]
	return list


def nextPermutation(arr):
	n = len(arr)
	i = 0
	j = 0
	
	for i in range(n-2, -1, -1):
		if (arr[i] < arr[i + 1]):
			break
			
	if (i < 0):
		arr.reverse()

	else:
		
		for j in range(n-1, i, -1):
			if (arr[j] > arr[i]):
				break

		swapPositions(arr, i, j)
		
		strt, end = i+1, len(arr)

		arr[strt:end] = arr[strt:end][::-1]


if __name__ == "__main__":
	arr = [3,2,7,5,6,9]
	
	nextPermutation(arr)
	
	for i in arr:
		print(i, end=" ")



'''
Q4. Given a sorted array of distinct integers and a target value, return the index if the
target is found. If not, return the index where it would be if it were inserted in
order.

You must write an algorithm with O(log n) runtime complexity.
'''


def find_index(arr, n, K):
	
	for i in range(n):
		
		if arr[i] == K:
			return i
			
		elif arr[i] > K:
			return i
			
	return n

arr = [5,3,4,9,2]
n = len(arr)
K = 7
print(find_index(arr, n, K))



'''
Q5. You are given a large integer represented as an integer array digits, where each
digits[i] is the ith digit of the integer. The digits are ordered from most significant
to least significant in left-to-right order. The large integer does not contain any
leading 0's.

Increment the large integer by one and return the resulting array of digits.

'''


def AddOne(digits):
	
	index = len(digits) - 1
	
	while (index >= 0 and digits[index] == 9):
		digits[index] = 0
		index -= 1
		
	if (index < 0):
		
		digits.insert(0, 1)
		
	else:
		digits[index]+=1


digits = [2,3,4,5]

AddOne(digits)

for digit in digits:
	print(digit, end =' ')


'''
Q6. Given a non-empty array of integers nums, every element appears twice except
for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only
constant extra space.
'''


def findSingle(A, ar_size):
	
	for i in range(ar_size):
		
		count = 0
		for j in range(ar_size):
			
			if(A[i] == A[j]):
				count += 1

		if(count == 1):
			return A[i]
			
	return -1

ar = [7,8,6,5,7,8,6]
n = len(ar)
print("Element occurring once is", findSingle(ar, n))


'''
Q7. You are given an inclusive range [lower, upper] and a sorted unique integer array
nums, where all elements are within the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in
nums.

Return the shortest sorted list of ranges that exactly covers all the missing
numbers. That is, no element of nums is included in any of the ranges, and each
missing number is covered by one of the ranges.

'''

def printMissing(arr, n, low, high):
	points_of_range = [False] * (high-low+1)
	
	for i in range(n) :
		if ( low <= arr[i] and arr[i] <= high ) :
			points_of_range[arr[i]-low] = True

	for x in range(high-low+1) :
		if (points_of_range[x]==False) :
			print(low+x, end = " ")

arr = [7,3,5,9,4,1]
n = len(arr)
low, high = 1, 10
printMissing(arr, n, low, high)


'''
Q8. Given an array of meeting time intervals where intervals[i] = [starti, endi],
determine if a person could attend all meetings.
'''

class meeting:
 
    def __init__(self, start, end, pos):
 
        self.start = start
        self.end = end
        self.pos = pos
 
 
 
def maxMeeting(l, N):
 
    ans = []
 
    l.sort(key=lambda x: x.end)
 
    ans.append(l[0].pos)
 
    time_limit = l[0].end
 
    for i in range(1, N):
        if l[i].start > time_limit:
            ans.append(l[i].pos)
            time_limit = l[i].end
 
    for i in ans:
        print(i + 1, end=" ")
 
    print()
 
 
if __name__ == '__main__':
 
    s = [1, 3, 0, 5, 8, 5]
 
    f = [2, 4, 6, 7, 9, 9]
 
    N = len(s)
 
    l = []
 
    for i in range(N):
 
        l.append(meeting(s[i], f[i], i))
 
    maxMeeting(l, N)