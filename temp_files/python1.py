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

#=====================