
# instance = CLASS()
colors = list()
names = list()
values = list()
colors.append('red')
values.insert(0, 25)

cities =  []  # same as list()

x = 5    #  x = int(5)
name = "John"  # name = str("John")

class Dog:
    def __init__(self):
        print("Creating a Dog")

    def bark(self):
        print(f"{id(self) = }") 
        print("woof woof")

d1 = Dog()
d2 = Dog()
print(f"{d1 = }")
print(f"{d2 = }")
d1.bark()  # self is d1
print(f"{id(d1) = }")
d2.bark()  # self is d2



