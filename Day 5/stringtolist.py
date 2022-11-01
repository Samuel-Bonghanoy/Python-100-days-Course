import random
a = "superman is gay as hell brodda"
b = list(a)
random.shuffle(b)
c = ""
for elements in b:
    c += elements
print(c)
