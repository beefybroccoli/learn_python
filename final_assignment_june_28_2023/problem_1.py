from random import randint

def getSortedRank(a):
    # Return a list rank of the same size of a
    # rank[j] = i means that a[i] must be the j^th element in sorted order.
    # For further details see above.
    # your code here
    list_a = []
    index = -1
    for element in a:
        index += 1
        list_a.append([element,index])

    # list_a = [ (-1, 0), (5, 1), (-2, 2), (3, 3), (0, 4), (2, 5) ]
    # print('list_a =', list_a)
    # print(sorted(list_a,key=lambda x:x[0]))
    sorted_by_rank = sorted(list_a,key=lambda x:x[0])
    # print('sorted_by_rank = ', sorted_by_rank)

    rank = -1
    for element in sorted_by_rank:
        rank += 1
        element.append(rank)
    # print('sorted_by_rank = ', sorted_by_rank)
    sorted_by_rank = sorted(list_a,key=lambda x:x[1])
    # print('sorted_by_rank = ', sorted_by_rank)

    result = []
    for i in range(0,len(sorted_by_rank)):
        # print(sorted_by_rank[i])
        result.append(sorted_by_rank[i][2])
    return result

def testRankArray(a, rank):
    n = len(a)
    sarray = [None]*n
    # Use the result to create a "sorted" array
    for (i, j) in enumerate(rank):
        sarray[j] = a[i]
    assert sum(rank) == (n-1)*(n)/2
    assert sum(sarray) == sum(a)
    # check that the sorted array is really sorted
    elt0 = sarray[0]
    for elt in sarray[1:]:
        assert elt0 <= elt, 'Test failed'
        elt0 = elt
    return


print("-------------------------------------------------------------")
print(' -- Test 1 -- ')
r = getSortedRank([-1, 5, -2, 3, 0, 2])
print('assert = ', r)
assert r == [1, 5, 0, 4, 2, 3] , 'Test 1 failed'

print(' -- Test 2 --')
a1 =[-1, 6, 7, 8, 2, 3, 2, 1, 0, 5, 4, 2]
r1 = getSortedRank(a1)
print("assert = ", r1)
testRankArray(a1, r1)

print('--- Random Test 3 ---')

def makeTestArray(n):
    a = [0]*n
    for i in range(n):
        a[i] = randint(-2*n, 2*n)
    return a

a3 = makeTestArray(20)
r3 = getSortedRank(a3)
print(f'a = {a3}')
print(f'result = {r3}')
testRankArray(a3, r3)

print('--- Random Test 4 ---')

a4 = makeTestArray(200)
r4 = getSortedRank(a4)
print('array too long to print')
#print(f'a = {a4}')
#print(f'result = {r4}')
testRankArray(a4, r4)
print('passed')

print('--- Random Test 5 ---')

a5 = makeTestArray(2000)
r5 = getSortedRank(a5)
print('array too long to print')
#print(f'a = {a5}')
#print(f'result = {r5}')
testRankArray(a5, r5)
print('passed')
print('--- Random Test 6 ---')

a6 = makeTestArray(20000)
r6 = getSortedRank(a6)
print('array too long to print')
#print(f'a = {a6}')
#print(f'result = {r6}')
testRankArray(a6, r6)
print('passed')
print('All tests passed (10 points)')