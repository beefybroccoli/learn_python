#Using the findCommonSorted function that finds all common elements in two lists, implement an algorithm for finding common elements in k sorted lists : list_of_lists but 

#assume that each individual list aj is sorted.

def findAllCommonElementsSorted(list_of_lists):

    # your code here
    result = []

    list1 = [ [-3, 1, 3, 4, 5, 8], [-8, 2, 2, 3, 4, 5, 10] ]

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
        # print('i = ', i)
        # print('j = ', j)
        # print("========")
    print('resullt = ', result)
    return result


print(' -- Test 1 --')
list1 = [ [-3, 1, 3, 4, 5, 8], [-8, 2, 2, 3, 4, 5, 10] ]
out1 = findAllCommonElementsSorted(list1)
print(out1)
assert(out1 == [3, 4, 5])
print('passed')
print(' -- Test 2 --')
list2 = [ [1, 3, 5], [4, 5, 7], [1,  5, 8], [-4, 3, 5], [1, 1, 5], [1, 5, 5] ]
out2 = findAllCommonElementsSorted(list2)
print(out2)
assert len(out2)== 1
assert 5 in out2
print('passed')

print('-- Test 3 --')
list3 = [[ -5, -2, -1, 1, 4], [-3, -2, -2,  1, 1, 2, 4, 5, 6], [-2, 1, 3, 4, 5, 6, 7, 8]]
out3 = findAllCommonElementsSorted(list3)
print(out3)
assert out3 == [-2, 1, 4]
print('passed')
print('-- Test 4 --')
list4 = [ [1, 2, 2, 3, 4,  6,  6, 7,  7], [3, 4, 8, 8, 9, 9], [0, 1, 4, 8, 12,18,  56, 67], [0, 0, 0, 1, 1, 3, 5, 6,  7, 8]]
out4= findAllCommonElementsSorted(list4)
print(out4)
assert len(out4) == 0
print('All Tests Passed: 5 points')