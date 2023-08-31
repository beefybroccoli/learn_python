"""
In this assignment, we would like you to solve this problem in $\Theta(n)$ time. I.e, your algorithm should be able to compute the result by just iterating through the array and keeping track of some quantities.

Let `[a0, a1,....,ak]` be a python array (list) of size k + 1.
Here is the idea:
  - As we iterate index i from 0 to k (inclusive), track a quantity `minSoFar` that is the minimum of the array so far from 0 to i-1. Initialize `minSoFar` to +infinity (In python you can say `float('inf')` to get a number that represents $\infty$).
  - Consider the difference `a[i] - minSoFar`. Calculate the __maximum__ such difference when iterating over the entire array.
  
Convince yourself that this will yield the overall solution to the max subarray problem with a complexity of $\Theta(n)$.
"""

def maxSubArray(a):
    n = len(a)
    if n == 1:
        return 0
    else:
        minSoFar = float('inf')
        maxSoFar = float('-inf')
        for i in range(len(a)):
            # print(f'array[{i}] = {a[i]}')
            # - As we iterate index i from 0 to k (inclusive), track a quantity `minSoFar` that is the minimum of the array so far from index 0 to index i-1.
            minSoFar = a[i] if a[i] < minSoFar else minSoFar
            # print(f'minSoFar = {minSoFar}')

            # - Consider the difference `a[i] - minSoFar`. Calculate the __maximum__ such difference when iterating over the entire array.
            temp_difference = a[i] - minSoFar
            # print(f'temp_difference = {temp_difference}')
            maxSoFar = temp_difference if temp_difference > maxSoFar else maxSoFar
        return maxSoFar


from random import randint

# temp_result = maxSubArray([100, -2, 5, 10, 11, -4, 15, 9, 18, -2, 21, -11])
# print(f'temp_result = {temp_result}')
# print("")
# temp_result = maxSubArray([-5, 1, 10, 4, 11, 4, 15, 9, 18, 0, 21, -11])
# print(f'temp_result = {temp_result}')
# print("")
# temp_result = maxSubArray([26, 0, 5, 18, 11, -1, 15, 9, 13, 5, 16, -11])
# print(f'temp_result = {temp_result}')
# print("")

assert(maxSubArray([100, -2, 5, 10, 11, -4, 15, 9, 18, -2, 21, -11]) == 25), 'Test 1 failed'
assert(maxSubArray([-5, 1, 10, 4, 11, 4, 15, 9, 18, 0, 21, -11]) == 26), 'Test 2 failed'
assert(maxSubArray([26, 0, 5, 18, 11, -1, 15, 9, 13, 5, 16, -11]) == 18), 'Test 3 failed'

def get_random_array(n):
    assert(n > 100)
    lst = [randint(0, 25) for j in range(n)]
    lst[0] = 1000
    lst[10] = -15
    lst[25] = 40
    lst[n-10] = 60
    lst[n-3]= -40
    return lst
assert(maxSubArray(get_random_array(50000)) == 75), 'Test on large random array 50000 failed'
assert(maxSubArray(get_random_array(500000)) == 75), 'Test on large random array of size 500000 failed'
print('All tests passed (10 points!)')