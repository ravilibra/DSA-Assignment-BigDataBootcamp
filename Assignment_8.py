
'''
Q1. Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.
'''

def minimumDeleteSum(s1, s2):
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    for i in range(len(s1) - 1, -1, -1):
        dp[i][len(s2)] = dp[i+1][len(s2)] + ord(s1[i])
    for j in range(len(s2) - 1, -1, -1):
        dp[len(s1)][j] = dp[len(s1)][j+1] + ord(s2[j])

    for i in range(len(s1) - 1, -1, -1):
        for j in range(len(s2) - 1, -1, -1):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i+1][j+1]
            else:
                dp[i][j] = min(dp[i+1][j] + ord(s1[i]),
                                dp[i][j+1] + ord(s2[j]))

    return dp[0][0]

s1 = "sea"
s2 = "eat"
print(minimumDeleteSum(s1, s2))


'''
Q2. Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
'''


def checkValidString(s):
    if not s: return True
    LEFTY, RIGHTY = '(*', ')*'

    n = len(s)
    dp = [[False] * n for _ in s]
    for i in range(n):
        if s[i] == '*':
            dp[i][i] = True
        if i < n-1 and s[i] in LEFTY and s[i+1] in RIGHTY:
            dp[i][i+1] = True

    for size in range(2, n):
        for i in range(n - size):
            if s[i] == '*' and dp[i+1][i+size]:
                dp[i][i+size] = True
            elif s[i] in LEFTY:
                for k in range(i+1, i+size+1):
                    if (s[k] in RIGHTY and
                            (k == i+1 or dp[i+1][k-1]) and
                            (k == i+size or dp[k+1][i+size])):
                        dp[i][i+size] = True

    return dp[0][-1]
s = "()"
print(checkValidString(s))


'''
Q3. Given two strings word1 and word2, return *the minimum number of **steps** required to make* word1 *and* word2 *the same*.

In one **step**, you can delete exactly one character in either string.
'''



def editDistance(str1, str2, m, n):

	if m == 0:
		return n

	if n == 0:
		return m

	if str1[m-1] == str2[n-1]:
		return editDistance(str1, str2, m-1, n-1)

	return 1 + min(editDistance(str1, str2, m, n-1),
				editDistance(str1, str2, m-1, n),
				editDistance(str1, str2, m-1, n-1)
				)


str1 = "sea"
str2 = "eat"
print (editDistance(str1, str2, len(str1), len(str2)))


'''
Q4. You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.
You always start to construct the **left** child node of the parent first if it exists.
'''


class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def preOrder(node):
	if (node == None):
		return
	print(node.data, end=' ')
	preOrder(node.left)
	preOrder(node.right)



def findIndex(Str, si, ei):
	if (si > ei):
		return -1

	s = []
	for i in range(si, ei + 1):

		if (Str[i] == '('):
			s.append(Str[i])

		elif (Str[i] == ')'):
			if (s[-1] == '('):
				s.pop(-1)

				if len(s) == 0:
					return i

	return -1



def treeFromString(Str, si, ei):

	if (si > ei):
		return None

	root = newNode(ord(Str[si]) - ord('0'))
	index = -1

	if (si + 1 <= ei and Str[si + 1] == '('):
		index = findIndex(Str, si + 1, ei)

	if (index != -1):

		root.left = treeFromString(Str, si + 2,
								index - 1)

		root.right = treeFromString(Str, index + 2,
									ei - 1)
	return root


if __name__ == '__main__':
	Str = "4(2(3)(1))(6(5))"
	root = treeFromString(Str, 0, len(Str) - 1)
	preOrder(root)


'''
Q5. Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of **consecutive repeating characters** in chars:

- If the group's length is 1, append the character to s.
- Otherwise, append the character followed by the group's length.

The compressed string s **should not be returned separately**, but instead, be stored **in the input character array chars**. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done **modifying the input array,** return *the new length of the array*.

You must write an algorithm that uses only constant extra space.
'''

def compress(chars):
    i = 0
    res = 0
    while i < len(chars):
        group_length = 1
        while (i + group_length < len(chars)
                and chars[i + group_length] == chars[i]):
            group_length += 1
        chars[res] = chars[i]
        res += 1
        if group_length > 1:
            str_repr = str(group_length)
            chars[res:res+len(str_repr)] = list(str_repr)
            res += len(str_repr)
        i += group_length
    return res

chars = ["a","a","b","b","c","c","c"]
print(compress(chars))


'''
Q6. Given two strings s and p, return *an array of all the start indices of* p*'s anagrams in* s.
You may return the answer in **any order**.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
'''

def findAnagrams(s, p):
    window = len(p)
    mapper = {}
    def __mapper():
        nonlocal mapper
        for i in p:
            if i in mapper.keys(): mapper[i] += 1
            else: mapper[i] = 1
    __mapper()
    ans = []
    st = 0
    ed = 0
    while ed < len(s):
        if s[ed] in mapper.keys():
            mapper[s[ed]] -= 1
            if mapper[s[ed]] == 0:
                del mapper[s[ed]]
            if not bool(mapper):
                ans.append(st)
                mapper[s[st]] = 1
                st += 1
            ed += 1
        else:
            if st == ed:
                st = ed = ed + 1
            else:
                if s[st] in mapper.keys():
                    mapper[s[st]] += 1
                else:
                    mapper[s[st]] = 1
                st += 1
    return ans           

s = "cbaebabacd"
p = "abc"
print(findAnagrams(s, p))


'''
Q7. Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.
'''


def decodeString(s):
    st = []
    num = 0
    res = ''

    for ch in s:
        if ch.isnumeric():
            num = num * 10 + int(ch)
        elif ch == '[':
            st.append(res)
            st.append(num)
            res = ''
            num = 0
        elif ch == ']':
            cnt = st.pop()
            prev = st.pop()
            res = prev + cnt * res
        else:
            res += ch
    return res
    
s = "3[a]2[bc]"
print(decodeString(s))


'''
Q8. Given two strings s and goal, return true *if you can swap two letters in* s *so the result is equal to* goal*, otherwise, return* false*.*

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

- For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
'''

def buddyStrings(s, goal):
    if len(s) != len(goal):
        return False

    if s == goal:

        frequency = [0] * 26
        for ch in s:
            frequency[ord(ch) - ord('a')] += 1
            if frequency[ord(ch) - ord('a')] == 2:
                return True

        return False

    firstIndex = -1
    secondIndex = -1

    for i in range(len(s)):
        if s[i] != goal[i]:
            if firstIndex == -1:
                firstIndex = i
            elif secondIndex == -1:
                secondIndex = i
            else:

                return False

    if secondIndex == -1:
        return False

    return s[firstIndex] == goal[secondIndex] and s[secondIndex] == goal[firstIndex]

s = "ab"
goal = "ba"
print(buddyStrings(s, goal))