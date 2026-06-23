class Dog:
    def bark(self):
        print("woof! woof!")
    
    def wag(self):
        print("wag wag wag wag wag")


    # def __dir__(self):
    #     return ['spam', 'ham']

dog = Dog()

all_attributes = dir(dog)
print("All attributes")
print(all_attributes)

public_attributes = [name for name in dir(dog) if not name.startswith('_')]
print(f"Public attributes")
print(public_attributes)


for attr_name in public_attributes:
    attr_value = getattr(dog, attr_name)
    attr_value()

# getattr() hasattr() setattr() delattr()

setattr(Dog, 'lick', lambda self: print("lick lick lick"))

dog.lick()

delattr(Dog, 'wag')

d2 = Dog()
d2.lick()