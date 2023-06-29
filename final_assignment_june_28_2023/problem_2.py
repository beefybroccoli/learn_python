def findMinAbsDiff(a):
    # you must return a tuple (i,j) -- see instructions above.
    assert (len(a) > 2)
    # your code here
    
    list_a = []
    index = -1
    for element in a:
        index += 1
        list_a.append([element,index])
    
    # print(list_a)

    sorted_by_value = sorted(list_a,key=lambda x:x[0])

    # print(sorted_by_value)

    low = 0
    high = 0
    diff = max(a)
    for i in range (0, len(a)-1):
        # print(sorted_by_value[i], sorted_by_value[i+1])
        if abs(sorted_by_value[i+1][0] - sorted_by_value[i][0]) < diff:
            low = sorted_by_value[i][1]
            high = sorted_by_value[i+1][1]
            diff = abs(sorted_by_value[i+1][0] - sorted_by_value[i][0])
    # print((high,low))
    return (high,low)

#================================================================
from random import shuffle

print(' -- Test 1 -- ')
(i, j) = findMinAbsDiff([ 1, 9, 18,  14, 17, 11])
print(f'i={i}, j={j}')
assert i == 2 and j == 4, 'Test 1 failed'
print('passed')

print('-- Test 2 --')
a1 = [1, 5, 9, 11, 2, 15, 25, 12, 18]
(i1, j1) = findMinAbsDiff(a1)
print(f'i={i1}, j={j1}')
assert abs(a1[i1] - a1[j1]) == 1, f'Test 2 failed: Minimmum difference must be 1 your code produces {abs(a1[i1] - a1[j1])}'
print('passed')

print('-- Test 3 --')
a2 = list(range(-10, 10, 3))
a2.append(3)
(i2, j2) = findMinAbsDiff(a2)
print(f'i={i2}, j={j2}')
assert abs(a2[i2] - a2[j2]) == 1, f'Test 2 failed: Minimmum difference must be 1 your code produces {abs(a2[i2] - a2[j2])}'
print('passed')

print('-- Test 4 --')
a3 = list(range(-100, 100, 3))
a3.append(11)
shuffle(a3)
(i3, j3) = findMinAbsDiff(a3)
print(f'i={i3}, j={j3}')
assert abs(a3[i3] - a3[j3]) == 0, f'Test 4 failed: Minimmum difference must be 0 your code produces {abs(a3[i3] - a3[j3])}'
print('passed')



print('-- Test 5 --')
a4 = list(range(-100, 100000, 3))
a4.append(12)
shuffle(a4)
(i4, j4) = findMinAbsDiff(a4)
print(f'i={i4}, j={j4}')
assert abs(a4[i4] - a4[j4]) == 1, f'Test 5 failed: Minimmum difference must be 1 your code produces {abs(a4[i4] - a4[j4])}'
print('passed')

print('All tests passed (15 points)!')