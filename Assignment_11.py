
'''
Q1. Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.
'''


def Sqrt(x):
    if (x == 0 or x == 1):
        return x
    n = 1
    result = 1
    while (result <= x):
 
        n += 1
        result = n * n
 
    return n - 1
 
 
x = 625
print(Sqrt(x))


'''
Q2. A peak element is an element that is strictly greater than its neighbors.

Given a **0-indexed** integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks,
return the index to **any of the peaks**.

You may imagine that `nums[-1] = nums[n] = -∞`. In other words, an element is always considered to be strictly greater than a neighbor
that is outside the array.

You must write an algorithm that runs in `O(log n)` time.
'''


def findPeak (arr, n):
    for i in range (n):
        if arr[i-1] and arr[i+1] < arr[i]:
            return i
        

arr = [1,2,1,3,5,6,4]
n = len(arr)
print("Index of a peak point is", findPeak(arr, n))
        

'''
Q3. Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
'''

def missingNumber (arr, n):
    arr.sort()
    for i in range (n):
        if arr[i+1] - arr[i] != 1:
            return arr[i] + 1
        
arr = [3,0,1]
n = len(arr)
print(missingNumber(arr, n))


'''
Q4. Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only **one repeated number** in `nums`, return *this repeated number*.

You must solve the problem **without** modifying the array `nums` and uses only constant extra space.
'''

def findDuplicate(nums):
    newList = []
    dupList = []
    for i in nums:
        if i not in newList:
            newList.append(i)
        else:
            dupList.append(i)
    return dupList
    
nums = [7,3,4,2,2]
print(findDuplicate(nums))


'''
Q5. Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result mustbe unique and
you may return the result in any order.
'''

def numsIntersection(nums1, nums2):
    intersected = []
    for i in nums1:
        if i in nums2:
            if i not in intersected:
                intersected.append(i)
    return intersected

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(numsIntersection(nums1, nums2))


'''
Q6. Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

- `[4,5,6,7,0,1,2]` if it was rotated `4` times.
- `[0,1,2,4,5,6,7]` if it was rotated `7` times.

Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of **unique** elements, return *the minimum element of this array*.

You must write an algorithm that runs in `O(log n) time.`
'''


def findMin(nums):
    if len(nums) == 1:
        return nums[0]

    left = 0
    right = len(nums) - 1

    if nums[right] > nums[0]:
        return nums[0]

    while right >= left:
        mid = left + (right - left) // 2
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        if nums[mid - 1] > nums[mid]:
            return nums[mid]
        if nums[mid] > nums[0]:
            left = mid + 1
        else:
            right = mid - 1

nums = [3,4,5,1,2]
print(findMin(nums))


'''
Q7. Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.
'''

def target_First_Last_Positions(nums, n, target):
    duplicate = []
    for i in range(n):
        if nums[i] == target:
            duplicate.append(i)
    return duplicate


nums = [5,7,7,8,8,10]
n = len(nums)
target = 8
print(target_First_Last_Positions(nums, n, target))
        

'''
Q8. Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it
shows in both arrays and you may return the result in any order.
'''

def numsIntersection(nums1, nums2):
    intersected = []
    for i in nums1:
        if i in nums2:
            intersected.append(i)
    return intersected

nums1 = [4,9,4,5,9,7]
nums2 = [9,4,9,8,4,6]
print(numsIntersection(nums1, nums2))