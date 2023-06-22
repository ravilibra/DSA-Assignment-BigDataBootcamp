
'''
Q1. Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
'''

def firstNotRepeatingCharacter(s):
    for i in s:
        if s.index(i) == s.rindex(i):
            return i
    return '_'

s = "leetcode"
print(firstNotRepeatingCharacter(s))


'''
Q2. Given a **circular integer array** `nums` of length `n`, return *the maximum possible sum of a non-empty **subarray** of* `nums`.

A **circular array** means the end of the array connects to the beginning of the array. Formally, the next element of `nums[i]` is
`nums[(i + 1) % n]` and the previous element of `nums[i]` is `nums[(i - 1 + n) % n]`.

A **subarray** may only include each element of the fixed buffer `nums` at most once. Formally, for a subarray `nums[i], nums[i + 1], ...,
nums[j]`, there does not exist `i <= k1`, `k2 <= j` with `k1 % n == k2 % n`.
'''


def maxCircularSum(a, n):
     
    if (n == 1):
        return a[0]
 
    sum = 0
    for i in range(n):
        sum += a[i]
 
    curr_max = a[0]
    max_so_far = a[0]
    curr_min = a[0]
    min_so_far = a[0]
 
    for i in range(1, n):
       
        curr_max = max(curr_max + a[i], a[i])
        max_so_far = max(max_so_far, curr_max)
 
        curr_min = min(curr_min + a[i], a[i])
        min_so_far = min(min_so_far, curr_min)
    if (min_so_far == sum):
        return max_so_far
 
    return max(max_so_far, sum - min_so_far)
 
a = [1,-2,3,-2]
n = len(a)
print("Maximum circular sum is", maxCircularSum(a, n))


'''
Q3. The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers `0` and `1` respectively.
All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a **stack**. At each step:

- If the student at the front of the queue **prefers** the sandwich on the top of the stack, they will **take it** and leave the queue.
- Otherwise, they will **leave it** and go to the queue's end.

This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays `students` and `sandwiches` where `sandwiches[i]` is the type of the `ith` sandwich in the stack (`i = 0` is
the top of the stack) and `students[j]` is the preference of the `jth` studentin the initial queue (`j = 0` is the front of the queue).
Return *the number of students that are unable to eat.*
'''


def countStudents(students, sandwiches):
    while(len(students)!=0):
        if(sandwiches[0] not in students):
            return(len(students))
        if(students[0]==sandwiches[0]):
            students.pop(0)
            sandwiches.pop(0)
        else:
            a=students.pop(0)
            students.append(a)
    return(len(students))

students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
print('No. of students that are unable to eat are', (countStudents(students,sandwiches)))



'''
Q4. You have a `RecentCounter` class which counts the number of recent requests within a certain time frame.

Implement the `RecentCounter` class:

- `RecentCounter()` Initializes the counter with zero recent requests.
- `int ping(int t)` Adds a new request at time `t`, where `t` represents some time in milliseconds, and returns the number of requests
that has happened in the past `3000` milliseconds (including the new request). Specifically, return the number of requests that have
happened in the inclusive range `[t - 3000, t]`.

It is **guaranteed** that every call to `ping` uses a strictly larger value of `t` than the previous call. 
'''

from collections import deque

class RecentCounter:

    def __init__(self):
        self.slide_window = deque()

    def ping(self, t):
        self.slide_window.append(t)

        while self.slide_window[0] < t - 3000:
            self.slide_window.popleft()

        return len(self.slide_window)

counter = RecentCounter()
print(counter.ping(1)) 
print(counter.ping(100))
print(counter.ping(3001))
print(counter.ping(3002))


'''
Q5. There are `n` friends that are playing a game. The friends are sitting in a circle and are numbered from `1` to `n` in **clockwise order**.
More formally, moving clockwise from the `ith` friend brings you to the `(i+1)th` friend for `1 <= i < n`, and moving clockwise from the `nth`
friend brings you to the `1st` friend.

The rules of the game are as follows:

1. **Start** at the `1st` friend.
2. Count the next `k` friends in the clockwise direction **including** the friend you started at. The counting wraps around the circle and
may count some friends more than once.
3. The last friend you counted leaves the circle and loses the game.
4. If there is still more than one friend in the circle, go back to step `2` **starting** from the friend **immediately clockwise** of the
friend who just lost and repeat.
5. Else, the last friend in the circle wins the game.

Given the number of friends, `n`, and an integer `k`, return *the winner of the game*.
'''


def findTheWinner(n, k):
    friends = list(range(1, n + 1))
    current_position = 0

    while len(friends) > 1:
        current_position = (current_position + k - 1) % len(friends)
        friends.pop(current_position)

    return friends[0]

n = 5
k = 2
print(findTheWinner(n, k))


'''
Q6. You are given an integer array `deck`. There is a deck of cards where every card has a unique integer. The integer on
the `ith` card is `deck[i]`.

You can order the deck in any order you want. Initially, all the cards start face down (unrevealed) in one deck.

You will do the following steps repeatedly until all cards are revealed:

1. Take the top card of the deck, reveal it, and take it out of the deck.
2. If there are still cards in the deck then put the next top card of the deck at the bottom of the deck.
3. If there are still unrevealed cards, go back to step 1. Otherwise, stop.

Return *an ordering of the deck that would reveal the cards in increasing order*.

**Note** that the first entry in the answer is considered to be the top of the deck.
'''


def deckRevealedIncreasing(deck):
    deck.sort(reverse=True)
    result = []
    
    for card in deck:
        if result:
            result.insert(0, result.pop())
        result.insert(0, card)
    
    return result


deck = [17, 13, 11, 2, 3, 5, 7]
result = deckRevealedIncreasing(deck)
print(result)


'''
Q7. Design a queue that supports `push` and `pop` operations in the front, middle, and back.

Implement the `FrontMiddleBack` class:

- `FrontMiddleBack()` Initializes the queue.
- `void pushFront(int val)` Adds `val` to the **front** of the queue.
- `void pushMiddle(int val)` Adds `val` to the **middle** of the queue.
- `void pushBack(int val)` Adds `val` to the **back** of the queue.
- `int popFront()` Removes the **front** element of the queue and returns it. If the queue is empty, return `1`.
- `int popMiddle()` Removes the **middle** element of the queue and returns it. If the queue is empty, return `1`.
- `int popBack()` Removes the **back** element of the queue and returns it. If the queue is empty, return `1`.

**Notice** that when there are **two** middle position choices, the operation is performed on the **frontmost** middle position choice.
For example:

- Pushing `6` into the middle of `[1, 2, 3, 4, 5]` results in `[1, 2, 6, 3, 4, 5]`.
- Popping the middle from `[1, 2, 3, 4, 5, 6]` returns `3` and results in `[1, 2, 4, 5, 6]`.
'''


class FrontMiddleBackQueue:
    def __init__(self):
        self.queue = []

    def pushFront(self, val: int) -> None:
        self.queue.insert(0, val)
        self.updateMiddleIndex()

    def pushMiddle(self, val: int) -> None:
        middle = len(self.queue) // 2
        self.queue.insert(middle, val)
        self.updateMiddleIndex()

    def pushBack(self, val: int) -> None:
        self.queue.append(val)
        self.updateMiddleIndex()

    def popFront(self) -> int:
        if not self.queue:
            return -1

        val = self.queue.pop(0)
        self.updateMiddleIndex()
        return val

    def popMiddle(self) -> int:
        if not self.queue:
            return -1

        middle = len(self.queue) // 2
        val = self.queue.pop(middle)
        self.updateMiddleIndex()
        return val

    def popBack(self) -> int:
        if not self.queue:
            return -1

        val = self.queue.pop()
        self.updateMiddleIndex()
        return val

    def updateMiddleIndex(self):
        self.middle = (len(self.queue) - 1) // 2


queue = FrontMiddleBackQueue()
queue.pushFront(1)
queue.pushBack(2)
queue.pushMiddle(3)
queue.pushMiddle(4)
print(queue.popFront())
print(queue.popMiddle())
print(queue.popMiddle())
print(queue.popBack())
print(queue.popFront())



'''
Q8. For a stream of integers, implement a data structure that checks if the last `k` integers parsed in the stream are **equal** to `value`.

Implement the **DataStream** class:

- `DataStream(int value, int k)` Initializes the object with an empty integer stream and the two integers `value` and `k`.
- `boolean consec(int num)` Adds `num` to the stream of integers. Returns `true` if the last `k` integers are equal to `value`,
and `false` otherwise. If there are less than `k` integers,the condition does not hold true, so returns `false`.
'''


class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.buffer = [None] * k
        self.count = 1
        self.idx = 0

    def consec(self, num: int) -> bool:
        if self.count < self.k:
            self.buffer[self.idx] = num
            self.count += 1
            self.idx = (self.idx + 1) % self.k
            return False

        self.buffer[self.idx] = num
        self.idx = (self.idx + 1) % self.k

        for i in range(self.k):
            if self.buffer[i] != self.value:
                return False

        return True

value = 4
k = 3

stream = DataStream(value, k)
print(stream.consec(4))
print(stream.consec(4))
print(stream.consec(4))
print(stream.consec(3))
