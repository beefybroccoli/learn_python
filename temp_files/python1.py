print('hello world')

a = 8
p = 31

for i in range(1,31):
    # print(i)
    # a * i mod p = 1
    # a =8, p = 31
    if( ((a * i) % p) == 1 ):
        print(i)


print (((a * 4) % p))

print("---------------------")

a = 8
p = 11

for i in range(1,11):
    # print(i)
    # a * i mod p = 7
    # a =8, p = 31
    if( ((a * i) % p) == 7 ):
        print(i)

print (((a * 5) % p))

print("test")