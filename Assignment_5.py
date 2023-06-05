
'''
Q1. You are given a **0-indexed** 1-dimensional (1D) integer array original, and two integers, m and n. You are tasked with creating a 2-dimensional (2D) array with  m rows and n columns using **all** the elements from original.

The elements from indices 0 to n - 1 (**inclusive**) of original should form the first row of the constructed 2D array, the elements from indices n to 2 * n - 1 (**inclusive**) should form the second row of the constructed 2D array, and so on.

Return *an* m x n *2D array constructed according to the above procedure, or an empty 2D array if it is impossible*.
'''

def construct2DArray(original, m, n):
    if m*n != len(original):
        return []
    ans = []
    for i in range(m):
        ans.append([])
        for j in range(n):
            ans[i].append(original.pop(0))
    return ans  

original = [1,2,3,4]
m = 2
n = 2
print(construct2DArray(original, m, n))


'''
Q2. You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase **may be** incomplete.

Given the integer n, return *the number of **complete rows** of the staircase you will build*.
'''

def stairCaseCoin(n):
    j = 0
    while (n > j):
        j = j + 1
        n = n - j
    return j

n = 8
print(stairCaseCoin(n))


'''
Q3.Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
'''

def sortSquare(nums,n):
    for i in range(n):
        nums[i] = nums[i] * nums[i]
    nums.sort()

nums  = [-5, -4, -2, 0, 1]
n = len(nums)
sortSquare(nums, n)
for i in range(n):
    print(nums[i], end = " ")


'''
Q4. Given two **0-indexed** integer arrays nums1 and nums2, return *a list* answer *of size* 2 *where:*

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
Q5.Given two integer arrays arr1 and arr2, and the integer d, *return the distance value between the two arrays*.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.
'''

def findTheDistanceValue(arr1, arr2, d):
    arr2.sort()
    distance = len(arr1)
    for num in arr1:
        start = 0
        end = len(arr2) - 1
        while start <= end:
            mid = (start+end)//2
            if abs(num- arr2[mid]) <= d:
                distance -= 1
                break
            elif arr2[mid] > num :
                end = mid-1
            elif arr2[mid] < num :
                start = mid+1
    return distance

arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 2
print(findTheDistanceValue(arr1, arr2, d))


'''
Q6. Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears **once** or **twice**, return *an array of all the integers that appears **twice***.

You must write an algorithm that runs in O(n) time and uses only constant extra space.
'''

def findDuplicates(nums):
    res = []
    hm = {}

    for i, v in enumerate(nums):
        if v not in hm:
            hm[v] = 1
        else:
            hm[v] += 1

    for key, value in hm.items():
        if value > 1:
            res.append(key)
    return res

nums =  [4,3,2,7,8,2,3,1]
print(findDuplicates(nums))


'''
Q7. Suppose an array of length n sorted in ascending order is **rotated** between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

- [4,5,6,7,0,1,2] if it was rotated 4 times.
- [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that **rotating** an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of **unique** elements, return *the minimum element of this array*.

You must write an algorithm that runs in O(log n) time.
'''

def findMin(arr, N):
     
    min_ele = arr[0];
 
    for i in range(N) :
        if arr[i] < min_ele :
            min_ele = arr[i]
 
    return min_ele;
 
arr = [3,4,5,1,2]
N = len(arr)
 
print(findMin(arr,N))

'''
Q8. An integer array original is transformed into a **doubled** array changed by appending **twice the value** of every element in original,
    and then randomly **shuffling** the resulting array.

Given an array changed, return original *if* changed *is a **doubled** array. If* changed *is not a **doubled** array,
return an empty array. The elements in* original *may be returned in **any** order*.
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