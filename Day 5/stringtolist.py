import random
a = "wassup brodda"
b = list(a)
random.shuffle(b)
c = ""
for elements in b:
    c += elements
print(c)
