
'''
Q1. Given two strings s and t, *determine if they are isomorphic*.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
'''

def isIsomorphic(s, t):
        
    mapping_s_t = {}
    mapping_t_s = {}
        
    for c1, c2 in zip(s, t):
            
        if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
            mapping_s_t[c1] = c2
            mapping_t_s[c2] = c1
                    
        elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
            return False
            
    return True

s = "egg"
t = "add"
print(isIsomorphic(s, t))


'''
Q2. Given a string num which represents an integer, return true *if* num *is a **strobogrammatic number***.

A **strobogrammatic number** is a number that looks the same when rotated 180 degrees (looked at upside down).
'''

def isStrobogrammatic(num):
      
    maps = {("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")}
    i,j = 0, len(num) - 1
    while i <= j:
        if (num[i], num[j]) not in maps:
            return False
        i += 1
        j -= 1
    return True

num = "69"
print(isStrobogrammatic(num))


'''
Q3. Given two non-negative integers, num1 and num2 represented as string, return *the sum of* num1 *and* num2 *as a string*.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.
'''


def addStrings(num1, num2):
    return str(int(num1)+int(num2))

num1 = "11"
num2 = "123"
print(addStrings(num1, num2))
        

'''
Q4. Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
'''

def print_words(s):
	word = ""

	iss = s.split()

	for i in iss:
		word = i[::-1]
		print(word, end=" ")


s = "Let's take LeetCode contest"
print_words(s)


'''
Q5. Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.
'''

def reverseStr(s, k):
    a = list(s)
    for i in range(0, len(a), 2*k):
        a[i:i+k] = reversed(a[i:i+k])
    return "".join(a)

s = "abcdefg"
k = 2
print(reverseStr(s, k))


'''
Q6. Given two strings s and goal, return true *if and only if* s *can become* goal *after some number of **shifts** on* s.

A **shift** on s consists of moving the leftmost character of s to the rightmost position.

- For example, if s = "abcde", then it will be "bcdea" after one shift.
'''


def areRotations(string1, string2):
    size1 = len(string1)
    size2 = len(string2)
    temp = ''
 
    if size1 != size2:
        return 0
 
    temp = string1 + string1
 
    if (temp.count(string2) > 0):
        return 1
    else:
        return 0
 
 
string1 = "AACD"
string2 = "ACDA"
 
if areRotations(string1, string2):
    print("Strings are rotations of each other")
else:
    print("Strings are not rotations of each other")


'''
Q7. Given two strings s and t, return true *if they are equal when both are typed into empty text editors*. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
'''

def backspaceCompare(S, T):
    def build(S):
        ans = []
        for c in S:
            if c != '#':
                ans.append(c)
            elif ans:
                ans.pop()
        return "".join(ans)
    return True

S = "ab#c"
T = "ad#c"
print(backspaceCompare(S, T))


'''
Q8. You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
    Check if these points make a straight line in the XY plane.
'''

def checkStraightLine(coordinates):
    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]

    for i in range(2, len(coordinates)):
        x, y = coordinates[i]
        if (x - x0) * (y1 - y0) != (y - y0) * (x1 - x0):
            return False

    return True

coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
print(checkStraightLine(coordinates))