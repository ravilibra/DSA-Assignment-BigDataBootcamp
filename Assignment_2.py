'''
Q1. Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2),..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

'''


def arrayPairSum(nums):

    nums.sort()
    result = 0
    numsLen = len(nums)
    for i in range(0, numsLen - 1, 2):
        result += nums[i]
    return result

nums = [2,4,3,5]
print(arrayPairSum(nums))


'''
Q2. Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor. 

The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice. 

Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.
'''


def distributeCandies(candyType):
    return min(len(candyType) >> 1, len(set(candyType)))

candyType = [2,3,3,7,9,7]
print(distributeCandies(candyType))


'''
Q3. We define a harmonious array as an array where the difference between its maximum value
and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence
among all its possible subsequences.

A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

'''

def findLHS(nums):
    numsLen, result = len(nums), 0
    counts = {}
    for val in nums:
        if val in counts:
            counts[val] += 1
        else:
            counts[val] = 1
        inc = val + 1
        dec = val - 1
        if dec in counts:
            result = max(result, counts[val] + counts[dec])
        if inc in counts:
            result = max(result, counts[val] + counts[inc])
    return result

nums = [2,4,6,7,5,4,5,6]
print(findLHS(nums))


'''
Q4. You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
'''

def canPlaceFlowers(flowerbed, n):
    result = 0
    flowerbed = [0] + flowerbed + [0]
    size = len(flowerbed)
    for i in range(1, size-1):
        if flowerbed[i]:
            continue
        elif flowerbed[i - 1] == flowerbed[i + 1] == 0:
            result = result +1
            flowerbed[i] = 1
            if n == result:return True
    return False

nums = [1,0,1,0,1]
n = 1
print(canPlaceFlowers(nums,n))


'''
Q5. Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
'''


import sys
def maxProduct(nums, n):
    if n < 3:
        return -1
    max_product = -(sys.maxsize - 1)
     
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                max_product = max(
                    max_product, nums[i]
                    * nums[j] * nums[k])
 
    return max_product
nums = [5,9,12,6,8]
n = len(nums)
 
max = maxProduct(nums, n)
 
if max == -1:
    print("No Triplet Exits")
else:
    print("Maximum product is", max)


'''
Q6. Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise,
return -1.
'''


def binary_search(nums, target):
	low = 0
	high = len(nums) - 1
	
	while low <= high:
		mid = low + ((high - low) // 2)
		if nums[mid] == target:
			return mid
		elif target < nums[mid]:
			high = mid - 1
		elif target > nums[mid]:
			low = mid + 1	
	return -1

nums = [1,10,20,47,59,63,75,88,99]
target = 70
print(binary_search(nums, target))


'''
Q7. An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is
monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.
'''


def check(nums):
    N = len(nums)
    inc = True
    dec = True
     
    for i in range(0, N-1):
        if nums[i] > nums[i+1]:
            inc = False
    for i in range(0, N-1):
        if nums[i] < nums[i+1]:
            dec = False
    return inc or dec

nums = [4, 5, 5, 6]
ans = check(nums)
if ans == True:
    print("True")
else:
    print("False")


'''
Q8. You are given an integer array nums and an integer k.

In one operation, you can choose any index i where 0 <= i < nums.length and change nums[i] to nums[i] + x where x is an integer from the range [-k, k]. You can apply this operation at most once for each index i.

The score of nums is the difference between the maximum and minimum elements in nums.

Return the minimum score of nums after applying the mentioned operation at most once for each index in it.
'''


def morethanNbyK(nums, n, k):
    x = n // k
 
    freq = {}
 
    for i in range(n):
        if nums[i] in freq:
            freq[nums[i]] += 1
        else:
            freq[nums[i]] = 1
 
    for i in freq:
        if (freq[i] > x):
            print(i)

nums = [9, 8, 7, 9, 2, 9, 7]
n = len(nums)
k = 3
     
print(morethanNbyK(nums, n, k))