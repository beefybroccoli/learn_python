#problem_1
from operator import itemgetter
a = [-1, 5, -2, 3, 0, 2]
list_a = []
index = -1
for element in a:
    index += 1
    list_a.append([element,index])


# list_a = [ (-1, 0), (5, 1), (-2, 2), (3, 3), (0, 4), (2, 5) ]
print('list_a =', list_a)
print(sorted(list_a,key=lambda x:x[0]))
sorted_by_rank = sorted(list_a,key=lambda x:x[0])
print('sorted_by_rank = ', sorted_by_rank)

rank = -1
for element in sorted_by_rank:
    rank += 1
    element.append(rank)
print('sorted_by_rank = ', sorted_by_rank)
sorted_by_rank = sorted(list_a,key=lambda x:x[1])
print('sorted_by_rank = ', sorted_by_rank)

result = []
for i in range(0,len(sorted_by_rank)):
    print(sorted_by_rank[i])
    result.append(sorted_by_rank[i][2])
    
print('result = ', result)





=================================================

list2 = [ [1, 3, 5], [4, 5, 7], [1,  5, 8], [-4, 3, 5], [1, 1, 5], [1, 5, 5] ]




























