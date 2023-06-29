def findCommonSorted(list1, list2):
    # your code here
    result = []
    i = 0
    j = 0
    while (i < len(list1) and j < len(list2)):
        if list1[i] < list2[j]:
            i += 1
        elif list2[j] < list1[i]:
            j += 1
        elif list1[i] == list2[j]:
            result.append(list1[i])
            j += 1
            i += 1
    return result

print('--Test 1--')
list1 = [ -2, 3, 5, 10, 12,  15, 18]
list2 = [-10, -5, -2, 1, 4, 5, 11, 18]
out12 = findCommonSorted(list1, list2)
print(out12)
assert out12 == [-2, 5, 18]
print('passed')

print('--Test 2--')
list3 = [-1, 0, 2, 5, 7, 19, 22, 26, 29, 32, 36]
list4 = [-10, -4, -2, 0, 5, 7, 12, 18, 20, 21, 25, 29, 36]
out34 = findCommonSorted(list3, list4)
print(out34)
assert out34 == [0, 5, 7, 29, 36]
print('passed')

print('--Test 3--')
list5 = list(range(0, 100000,2))
list6 = list(range(1, 100001, 2))
out56 = findCommonSorted(list5, list6)
assert len(out56) ==0
print('passed')

print('All tests passed: 5 points!')