
def returnAllCommonElements(list_of_lists):
    # list_of_lists = [ [ 1, 5, 8, -3, 4, 1, 3], [2, 5, 10, -8, 4, 3, 2] ]
    my_dict = dict()
    for index in range(0,len(list_of_lists)):
        print(list_of_lists[index])
        my_set = set(list_of_lists[index])
        for element in my_set:
            # print(element)
            if element in my_dict.keys():
                count = my_dict[element]
                my_dict[element]=count+1
            else:
                my_dict[element]=1

    # print(my_dict.items())
    list_key = list(my_dict.items())
    # print(list_key)

    sorted_list_key = sorted(list_key,key=lambda x:x[1])
    # print(sorted_list_key)

    max = sorted_list_key[len(sorted_list_key)-1][1]
    # print('max = ', max)

    filter_sorted_list_key = list(filter(lambda element: (element[1]==max and element[1] == len(list_of_lists)), sorted_list_key))
    # print(filter_sorted_list_key)

    result = list(map(lambda element: (element[0]), filter_sorted_list_key))
    # print('result = ', result)
    
    return result

print(' -- Test 1 --')
list1 = [ [ 1, 5, 8, -3, 4, 1, 3], [2, 5, 10, -8, 4, 3, 2] ]
out1 = returnAllCommonElements(list1)
print(out1)
assert len(out1) == 3
assert 5 in out1
assert 4 in out1
assert 3 in out1
print('passed')
print(' -- Test 2 --')
list2 = [ [1, 3, 5], [5, 4, 7], [8, 1, 5], [-4, 3, 5], [1, 1, 5], [1, 5, 5] ]
out2 = returnAllCommonElements(list2)
print(out2)
assert len(out2)== 1
assert 5 in out2
print('passed')

print('-- Test 3 --')
list3 = [[1, -5, 4, -2, -1], [2, -3, 1, -2, 4, 6, 1, 5, -2], [4, 5, 6, 7, 8, 1, 3, -2]]
out3 = returnAllCommonElements(list3)
print(out3)
assert len(out3) == 3
assert 1 in out3
assert 4 in out3
assert -2 in out3
print('passed')

print('-- Test 4 --')
list4 = [ [1, 2, 4, 7, 2, 6, 3, 6, 7], [8, 9,  3, 4, 8, 9], [1, 4, 56, 12, 67, 8, 0, 18], [0, 1, 7, 8, 0, 1, 3, 5, 6, 0, 19]]
out4= returnAllCommonElements(list4)
print(out4)
assert len(out4) == 0

print('All Tests Passed: 15 points')