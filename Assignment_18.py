
'''
Q1. Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the
non-overlapping intervals that cover all the intervals in the input.
'''


def mergeIntervals(intervals):

    intervals.sort()
    stack = []
    
    stack.append(intervals[0])
    for i in intervals[1:]:
        if stack[-1][0] <= i[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], i[-1])
        else:
            stack.append(i)
 
    print("The Merged Intervals are :", end=" ")
    for i in range(len(stack)):
        print(stack[i], end=" ")
 
 
arr = [[1,3],[2,6],[8,10],[15,18]]
mergeIntervals(arr)


'''
Q2. Given an array `nums` with `n` objects colored red, white, or blue, sort them so that objects of the same color are adjacent,
with the colors in the order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
'''


def sortColors(nums):

    if len(nums)==1:
        return nums
    m0=nums.count(0)
    m1=m0+nums.count(1)
    m2=m1+nums.count(2)
    j=0
    while(j<len(nums)):
        if j<m0:
            nums[j]=0
        elif j<m1:
            nums[j]=1
        elif j<m2:
            nums[j]=2
        j=j+1
    return nums

nums = [2,0,2,1,1,0]
print(sortColors(nums))


'''
Q3. You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails
the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API `bool isBadVersion(version)` which returns whether `version` is bad. Implement a function to find the first bad version.
You should minimize the number of calls to the API.
'''


class Solution:
    def firstBadVersion(n):
        first = 0
        last = n
        while first <= last:
            mid = (first+last)//2
            if isBadVersion(mid):
                if not isBadVersion(mid-1):
                    return mid
                else:
                    last = mid - 1
            else:
                first = mid + 1
        
        return -1
    

'''
Q4. Given an integer array `nums`, return *the maximum difference between two successive elements in its sorted form*.
If the array contains less than two elements, return `0`.

You must write an algorithm that runs in linear time and uses linear extra space.
'''

def maxSortedAdjacentDiff(arr, n):
 
    maxVal, minVal = arr[0], arr[0]
    for i in range(1, n):
        maxVal = max(maxVal, arr[i])
        minVal = min(minVal, arr[i])
 
    maxBucket = [INT_MIN] * (n - 1)
    minBucket = [INT_MAX] * (n - 1)
     
    delta = (maxVal - minVal) // (n - 1)
 
    for i in range(0, n):
        if arr[i] == maxVal or arr[i] == minVal:
            continue
 
        index = (arr[i] - minVal) // delta
 
        if maxBucket[index] == INT_MIN:
            maxBucket[index] = arr[i]
        else:
            maxBucket[index] = max(maxBucket[index], arr[i])
 
        if minBucket[index] == INT_MAX:
            minBucket[index] = arr[i]
        else:
            minBucket[index] = min(minBucket[index],
                                             arr[i])
     
    prev_val, max_gap = minVal, 0
     
    for i in range(0, n - 1):
        if minBucket[i] == INT_MAX:
            continue
             
        max_gap = max(max_gap,
                      minBucket[i] - prev_val)
        prev_val = maxBucket[i]
     
    max_gap = max(max_gap, maxVal - prev_val)
 
    return max_gap
 
if __name__ == "__main__":
 
    arr = [3,6,9,1]
    n = len(arr)
    INT_MIN, INT_MAX = float('-inf'), float('inf')
     
    print(maxSortedAdjacentDiff(arr, n))


'''
Q5. Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

def findDup(nums):
    List = []
    for i in (nums):
        if i in List:
            return True
        else:
            List.append(i)
        
nums = [1,2,3,1]
print(findDup(nums))


'''
Q6. There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer
array `points` where `points[i] = [xstart, xend]` denotes a balloon whose **horizontal diameter** stretches between `xstart` and `xend`.
You do not know the exact y-coordinates of the balloons.

Arrows can be shot up **directly vertically** (in the positive y-direction) from different points along the x-axis. A balloon with `xstart`
and `xend` is **burst** by an arrow shot at `x` if `xstart <= x <= xend`. There is **no limit** to the number of arrows that can be shot.
A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array `points`, return *the **minimum** number of arrows that must be shot to burst all balloons*.
'''


def findMinArrowShots(points):
    points.sort(key=lambda x: x[1])
        
    arrows = 0
    last_end = float('-inf')
        
    for start, end in points:
        if start > last_end:
            arrows += 1
            last_end = end
        
    return arrows

points = [[10,16],[2,8],[1,6],[7,12]]
print(findMinArrowShots(points))


'''
Q7. Given an integer array `nums`, return *the length of the longest **strictly increasing***

***subsequence***
'''

def lengthOfLIS(nums):
    if nums == None or len(nums) == 0:
        return 0
        
    length = len(nums)
    dp = [1] * length
    maximum = 1
        
    for i in range(length):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        maximum = max(maximum, dp[i])
            
    return maximum

nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))


'''
Q8. Given an array of `n` integers `nums`, a **132 pattern** is a subsequence of three integers `nums[i]`, `nums[j]` and `nums[k]` such that
`i < j < k` and `nums[i] < nums[k] < nums[j]`.

Return `true` *if there is a **132 pattern** in* `nums`*, otherwise, return* `false`*.*
'''


def recreationalSpot(arr, n) :
 
    small = []
    min1 = arr[0]
    for i in range(n) :
        if (min1 >= arr[i]) :
            min1 = arr[i]
            small.append(-1)
             
        else :
 
            small.append(min1)
    s = []
    for i in range(n - 1, 0, -1) :
        while (len(s) != 0 and s[-1] <= small[i]) :
            s.pop()
 
        if (len(s) != 0 and small[i] != -1 and s[-1] < arr[i]) :
            return True
             
        s.append(arr[i])
 
    return False
 
if __name__ == "__main__" :
 
    arr = [1,2,3,4]
    N = len(arr)
 
    # Function Call
    if (recreationalSpot(arr, N)) :
        print("True")
    else :
        print("False")