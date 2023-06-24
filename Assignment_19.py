
'''
Q1. You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

*Merge all the linked-lists into one sorted linked-list and return it.*
'''


class Node:
  
    def __init__(self, x):
  
        self.data = x
        self.next = None
  
  
  
def printList(node):
  
    while (node != None):
        print(node.data,
              end=" ")
        node = node.next
  
  
  
def mergeKLists(arr, last):
  
    for i in range(1, last + 1):
        while (True):
            head_0 = arr[0]
            head_i = arr[i]
  
            if (head_i == None):
                break
  
            if (head_0.data >=
                    head_i.data):
                arr[i] = head_i.next
                head_i.next = head_0
                arr[0] = head_i
            else:
                while (head_0.next != None):
                    if (head_0.next.data >=
                            head_i.data):
                        arr[i] = head_i.next
                        head_i.next = head_0.next
                        head_0.next = head_i
                        break
                    head_0 = head_0.next
                    if (head_0.next == None):
                        arr[i] = head_i.next
                        head_i.next = None
                        head_0.next = head_i
                        head_0.next.next = None
                        break
    return arr[0]
  
  
if __name__ == '__main__':
  
    k = 3
  
    n = 4
  
    arr = [None for i in range(k)]
  
    arr[0] = Node(1)
    arr[0].next = Node(4)
    arr[0].next.next = Node(5)
  
    arr[1] = Node(1)
    arr[1].next = Node(3)
    arr[1].next.next = Node(4)
  
    arr[2] = Node(2)
    arr[2].next = Node(6)
  
    head = mergeKLists(arr, k - 1)
  
    printList(head)


'''
Q2. Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].
'''

def constructLowerArray(arr, countSmaller, n):

	for i in range(n):
		countSmaller[i] = 0

	for i in range(n):
		for j in range(i + 1, n):
			if (arr[j] < arr[i]):
				countSmaller[i] += 1


def printArray(arr, size):
	for i in range(size):
		print(arr[i], end=" ")
	print()


arr = [5,2,6,1]
n = len(arr)
low = [0]*n
constructLowerArray(arr, low, n)
printArray(low, n)


'''
Q3. Given an array of integers `nums`, sort the array in ascending order and return it.

You must solve the problem **without using any built-in** functions in `O(nlog(n))` time complexity and with the smallest space complexity
possible.
'''

class Solution:
    def sortArray(nums):
        temp_arr = [0] * len(nums)
        def merge(left: int, mid: int, right: int):
            start1 = left
            start2 = mid + 1
            n1 = mid - left + 1
            n2 = right - mid

            for i in range(n1):
                temp_arr[start1 + i] = nums[start1 + i]
            for i in range(n2):
                temp_arr[start2 + i] = nums[start2 + i]

            i, j, k = 0, 0, left
            while i < n1 and j < n2:
                if temp_arr[start1 + i] <= temp_arr[start2 + j]:
                    nums[k] = temp_arr[start1 + i]
                    i += 1
                else:
                    nums[k] = temp_arr[start2 + j]
                    j += 1
                k += 1

            while i < n1:
                nums[k] = temp_arr[start1 + i]
                i += 1
                k += 1
            while j < n2:
                nums[k] = temp_arr[start2 + j]
                j += 1
                k += 1

        def merge_sort(left: int, right: int):
            if left >= right:
                return
            mid = (left + right) // 2
            merge_sort(left, mid)
            merge_sort(mid + 1, right)
            merge(left, mid, right)
    
        merge_sort(0, len(nums) - 1)
        return nums
     
     
nums = [5,1,1,2,0,0]
     
print(Solution.sortArray(nums))



'''
Q3. Given an array of random numbers, Push all the zero’s of a given array to the end of the array. For example, if the given arrays is 
{1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, it should be changed to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}. The order of all otherelements should be same. 
Expected time complexity is O(n) and extra space is O(1).
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
         
arr = [1, 2, 0, 4, 3, 0, 5, 0]
n = len(arr)
pushZerosToEnd(arr, n)
print(arr)


'''
Q5. Given an array of positive and negative numbers, arrange them in an alternate fashion such that every positive number is followed by a
negative and vice-versa maintaining the order of appearance. The number of positive and negative numbers need not be equal. If there are more
positive numbers they appear at the end of the array. If there are more negative numbers, they too appear at the end of the array.
'''

def rightRotate(arr, n, outOfPlace, cur):
    temp = arr[cur]
    for i in range(cur, outOfPlace, -1):
        arr[i] = arr[i - 1]
    arr[outOfPlace] = temp
    return arr
 
 
def rearrange(arr, n):
    outOfPlace = -1
    for index in range(n):
        if(outOfPlace >= 0):
            if((arr[index] >= 0 and arr[outOfPlace] < 0) or
               (arr[index] < 0 and arr[outOfPlace] >= 0)):
                arr = rightRotate(arr, n, outOfPlace, index)
                if(index-outOfPlace > 2):
                    outOfPlace += 2
                else:
                    outOfPlace = - 1
 
        if(outOfPlace == -1):
            if((arr[index] >= 0 and index % 2 == 0) or
               (arr[index] < 0 and index % 2 == 1)):
                outOfPlace = index
    return arr
 
 
arr = [1, 2, 3, -4, -1, 4]

print(rearrange(arr, len(arr)))


'''
Q6. Given two sorted arrays, the task is to merge them in a sorted manner.

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
Q7. Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you
may return the result in any order.
'''


def uniqueElement(nums1, nums2):
    element = []
    for i in nums1:
         if i not in element:
              element.append(i)
    for j in nums2:
         if j not in element:
              element.append(j)

    return element

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print(uniqueElement(nums1, nums2))



'''
Q8. Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times
as it shows in both arrays and you may return the result in any order.
'''


def intersection(nums1, nums2):
     elements = []
     for i in nums1:
          if i in nums2:
               elements.append(i)
     for j in nums2:
          if j in nums1:
               elements.append(j)
     return elements

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersection(nums1, nums2))