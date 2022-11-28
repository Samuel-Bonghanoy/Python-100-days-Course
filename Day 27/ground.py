def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)


add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 12, 12, 12)

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]


calculate(add=3, multiply =5) #makes a dictionary out of the keywords and values (keyword: value)


class Car:

    def __init__(self, **kw):
        self.make = kw.get["make"]
        self.model = kw.get["model"]

my_car = Car(make="Nissan", model="tamron")