#Sets&Lists
# a = [11,2,3,5,8,13,21,34,55,89]
# b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# #converting to sets
# A= set(a)
# B= set(b)
# #common members
# print(B.intersection(A))

# import random
# A = random.sample(range(10, 50), 9)
# B = random.sample(range(20, 75), 13)
# print(A)
# print(B)

# common_list = [c for c in A if c in B]
# print(common_list)

import random
def common(a, b, c):
    if c in a or b:
        print(c)
    else:
        print("None")
a = random.sample(range(10, 50), 9)
b = random.sample(range(20, 75), 13)
c = [c for c in a if c in b]
print(a, b)
common(a, b, c)


