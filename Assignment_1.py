
'''
Q1. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

def twoSum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i

nums = [2,6,7,9,4]
target = 8
print(twoSum(nums, target))


'''
Q2. Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

- Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
- Return k.
'''

def removeElement(nums, val):
    count = 0
    for i in range(len(nums)):
        if nums[i] != val :
            nums[count] = nums[i]
            count +=1
    return count
    
nums = [4,8,8,6,4]
val = 4
print(removeElement(nums, val))


'''
Q3. Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

'''

def find_index(arr, n, K):
     
    # Traverse the array
    for i in range(n):
         if arr[i] == K:
            return i
         elif arr[i] > K:
            return i
    return n
 

arr = [2, 4, 7, 9]
n = len(arr)
K = 5
print(find_index(arr, n, K))


'''
Q4. You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

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


digits = [3, 5, 6, 8]

AddOne(digits)

for digit in digits:
	print(digit, end =' ')


'''
Q5. You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

'''


def mergeArrays(arr1, arr2, n1, n2, arr3):
	i = 0
	j = 0
	k = 0

	while(i < n1):
		arr3[k] = arr1[i]
		k += 1
		i += 1

	while(j < n2):
		arr3[k] = arr2[j]
		k += 1
		j += 1

	arr3.sort()




arr1 = [1, 3, 5, 7]
n1 = len(arr1)

arr2 = [2, 4, 6, 8]
n2 = len(arr2)

arr3 = [0 for i in range(n1+n2)]
mergeArrays(arr1, arr2, n1, n2, arr3)

print("Array after merging")
for i in range(n1 + n2):
	print(arr3[i], end=" ")


'''
Q6.  Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''


def checkDuplicatesWithinK(arr, n, k):
	for i in range(n):
		j = i + 1
		range_ = k
		while (range_ > 0 and j < n):
			if (arr[i] == arr[j]):
				return True
			j += 1
			range_ -= 1

	return False


arr = [8, 4, 2, 3, 2, 5, 6]
n = len(arr)
if (checkDuplicatesWithinK(arr, n, 3) == True):
	print("Yes")
else:
	print("No")
	

'''
Q7. Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.

Note that you must do this in-place without making a copy of the array.

'''
	


def pushZerosToEnd(arr, n):
	count = 0 
	for i in range(n):
		if arr[i] != 0:
			arr[count] = arr[i]
			count+=1
	while count < n:
		arr[count] = 0
		count += 1
		
arr = [0, 5, 7, 4, 0, 0, 2, 7, 0, 1, 0, 2]
n = len(arr)
pushZerosToEnd(arr, n)
print("Array after pushing all zeros to end of array:")
print(arr)


'''
Q8. You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

'''

def findErrorNums(nums):
    N, dupe = len(nums), 0
    seen, sumN = [0] * (N+1), N * (N+1) // 2
    for num in nums:
        sumN -= num
        if seen[num]: dupe = num
        seen[num] += 1
    return [dupe, sumN + dupe]

nums = [1,2,3,3,5]
print(findErrorNums(nums))
