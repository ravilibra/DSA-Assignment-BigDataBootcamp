
'''
Q1. Given an integer `n`, return *`true` if it is a power of three. Otherwise, return `false`*.

An integer `n` is a power of three, if there exists an integer `x` such that `n == 3x`.
'''

def isPower_of_Three(n):

	if (n <= 0):
		return False
	if (n % 3 == 0):
		return isPower_of_Three(n // 3)
	if (n == 1):
		return True
	return False


n = 27
if (isPower_of_Three(n)):
	print("True")
else:
	print("False")
	

'''
Q2. You have a list `arr` of all integers in the range `[1, n]` sorted in a strictly increasing order. Apply the following algorithm on `arr`:

- Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
- Repeat the previous step again, but this time from right to left, remove the rightmost number and every other number from the remaining numbers.
- Keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Given the integer `n`, return *the last number that remains in* `arr`.
'''

def lastRemaining(n):
    left = True
    remaining = n
    step = 1
    head = 1
    while remaining > 1:
        if left or remaining % 2 == 1:
            head += step
        step *= 2
        remaining //= 2
        left = not left

    return head
    
n = 9
print(lastRemaining(n))


'''
Q3. Given a set represented as a string, write a recursive code to print all subsets of it. The subsets can be printed in any order.
'''

def powerSet(str1, index, curr):
	n = len(str1)

	if (index == n):
		return

	print(curr)
	for i in range(index + 1, n):
		curr += str1[i]
		powerSet(str1, i, curr)
		curr = curr.replace(curr[len(curr) - 1], "")

	return


str = "abc"
index = 0
curr = ""
powerSet(str, -1, "")


'''
Q4. Given a string calculate length of the string using recursion.
'''

def string_length(str) :
    if str == '':
        return 0
    else :
        return 1 + string_length(str[1:])
     

str = "abcd"
print (string_length(str))


'''
Q5. We are given a string S, we need to find count of all contiguous substrings starting and ending with same character.
'''

def countSubstringWithEqualEnds(s):
 
    result = 0;
    n = len(s);
 
    for i in range(n):
        for j in range(i, n):
            if (s[i] == s[j]):
                result = result + 1
 
    return result
 
s = "abcab"
print(countSubstringWithEqualEnds(s))


'''
Q6. The tower of Hanoi is a famous puzzle where we have three rods and N disks. The objective of the puzzle is to move the entire
stack to another rod. You are given the number of discs N. Initially, these discs are in the rod 1. You need to print all the
steps of discs movement so that all the discs reach the 3rd rod. Also, you need to find the total moves.Note: The discs are arranged
such that the top disc is numbered 1 and the bottom-most disc is numbered N. Also, all the discs have different sizes and a bigger
disc cannot be put on the top of a smaller disc.
'''

def move(disks, source=1, auxiliary=2, target=3):
 
    if disks > 0:
        move(disks - 1, source, target, auxiliary)
        print(f'Move disk {disks} from {source} —> {target}')
        move(disks - 1, auxiliary, source, target)
 
n = 3
print(move(n))


'''
Q7. Given a string str, the task is to print all the permutations of str. A permutation is an arrangement of all or part of a set of objects,
with regard to the order of the arrangement. For instance, the words ‘bat’ and ‘tab’ represents two distinct permutation (or arrangements)
of a similar three letter word.
'''

# Function to find permutations of a given string
from itertools import permutations

def allPermutations(str):
	
	permList = permutations(str)

	for perm in list(permList):
		print (''.join(perm))
	
str = 'ABC'
print(allPermutations(str))


'''
Q8. Given a string, count total number of consonants in it. A consonant is an English alphabet character that is not vowel (a, e, i, o and u).
Examples of constants are b, c, d, f, and g.
'''

def Consonant(ch):
      
    ch = ch.upper()
  
    return not (ch == 'A' or ch == 'E' or 
                ch == 'I' or ch == 'O' or 
                ch == 'U') and ord(ch) >= 65 and ord(ch) <= 90
  
def totalConsonants(string):
      
    count = 0
      
    for i in range(len(string)):
        if (Consonant(string[i])):
            count += 1
              
    return count
  
string = "abcde"
print(totalConsonants(string))