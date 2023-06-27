# print('hello world')

# a = 8
# p = 31

# for i in range(1,31):
#     # print(i)
#     # a * i mod p = 1
#     # a =8, p = 31
#     if( ((a * i) % p) == 1 ):
#         print(i)


# print (((a * 4) % p))

# print("---------------------")

# a = 8
# p = 11

# for i in range(1,11):
#     # print(i)
#     # a * i mod p = 7
#     # a =8, p = 31
#     if( ((a * i) % p) == 7 ):
#         print(i)

# print (((a * 5) % p))

# print("test")

list_a = [-1, 5, 2, 3, 4, 8, 9, 14, 10, 23]
k = 4
left = list_a[:k]
right = list_a[k+1:]
pivot = list_a[k]
print(left)
print(right)

print(True if len(left) == 0 else max(left) <= pivot)
print(True if len(right) == 0 else pivot < min(right))

# print(max(left))
# print(min(right))
# print(pivot)

# print(list_a[:0])
# print(list_a[0+1:])
# print(max(list_a[:0]))

last_index = len(list_a) -1
for j in range(0, last_index):
    print(list_a[j])


# [1, 3, 6, 1, 5, 4, 1, 1, 2, 3, 3, 1, 3, 5, 2, 2, 4]
# [1, 5, 6, 1, 3, 4, 1, 1, 2, 3, 3, 1, 3, 5, 2, 2, 4]
list_a.index(4)

print('=====================')

def dot_product(lst_a, lst_b):
    and_list = [elt_a * elt_b for (elt_a, elt_b) in zip(lst_a, lst_b)]
    return 0 if sum(and_list)% 2 == 0 else 1

H = [[0,1,0,1],[1,0,0,0],[1,0,1,1]]

J = [1,1,1,0]

temp_1 = dot_product([0,1,0,1],J)
print(temp_1)

for element_list in H:
    print(dot_product(element_list, J))

print ([dot_product(element_list, J) for element_list in H])
# A1 = [[0,1,0,1],[1,0,0,0],[1,0,1,1]]
# b1 = [1,1,1,0]
# temp_1 = dot_product(A1,b1)
# print(temp_1)

print("===========================")

print((-1+3)/2)
print((3+2)/2)
print((2+1)/2)
print((7+9)/2)