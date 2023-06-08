
'''
Q1. Given an integer `n`, return *`true` if it is a power of two. Otherwise, return `false`*.

An integer `n` is a power of two, if there exists an integer `x` such that `n == 2x`.
'''

def isPowerOfTwo(n):
    if (n == 0):
        return False
    while (n != 1):
        if (n % 2 != 0):
            return False
        n = n // 2
 
    return True
 
n = 16

if __name__ == "__main__":
 
    if(isPowerOfTwo(n)):
        print('Yes')
    else:
        print('No')


'''
Q2. Given a number n, find the sum of the first natural numbers.
'''

def findSum(n):
	sum = 0
	x = 1
	while x <= n:
		sum = sum + x
		x = x + 1
	return sum


n = 5
print ("Sum of first", n, "natural number is", findSum(n))

# OR

def findSums(n):
     n = n * (n+1)/2
     return n


n = 5
print("Sum of first", n, "natural number is", findSums(n))


'''
Q3. Given a positive integer, N. Find the factorial of N.
'''


def factorial(n):
	
	if n == 0:
		return 1
	
	return n * factorial(n-1)

num = 5
print("factorial of", num, "is", factorial(num))


'''
Q4. Given a number N and a power P, the task is to find the exponent of this number raised to the given power, i.e. N^P.
'''

def power(N, P):
    if P == 0:
        return 1
    return (N*power(N, P-1))

N = 4
P = 3
print(N, "to the power", P, "is", power(N, P))


'''
Q5. Given an array of integers arr, the task is to find maximum element of that array using recursion.
'''

def findMax(A, n):
    if (n == 1):
        return A[0]
    return max(A[n - 1], findMax(A, n - 1))
 
A = [1, 4, 3, -5, -4, 8, 6]
n = len(A)
print(findMax(A, n))


'''
Q6. Given first term (a), common difference (d) and a integer N of the Arithmetic Progression series,
the task is to find Nth term of the series.
'''

def Nth_of_AP(a, d, N) :
    return (a + (N - 1) * d)
      
  
a = 2
d = 1
N = 5
  
print( "The ", N ,"th term of the series is : ", Nth_of_AP(a, d, N))


'''
Q7. Given a string S, the task is to write a program to print all permutations of a given string.
'''

def toString(List):
    return ''.join(List)
 
 
def permute(a, l, r):
    if l == r:
        print(toString(a))
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]
 
 
string = "ABC"
n = len(string)
a = list(string)
 
print(permute(a, 0, n))


'''
Q8. Given an array, find a product of all array elements.
'''


def product(arr, n):
  
    result = 1
    for i in range(0, n):
        result = result * arr[i]
    return result
  
  
arr = [ 1, 2, 3, 4, 5 ]
n = len(arr)
  
print(product(arr, n))