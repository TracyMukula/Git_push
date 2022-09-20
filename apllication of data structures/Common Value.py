#Write a program that returns a list that contains only the elements that are common, without duplicates
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

