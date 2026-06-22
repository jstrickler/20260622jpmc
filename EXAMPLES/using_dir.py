class Dog:
    def bark(self):
        print("woof! woof!")
    
    def wag(self):
        print("wag wag wag wag wag")

dog = Dog()

all_attributes = dir(dog)
print("All attributes")
print(all_attributes)

public_attributes = [name for name in dir(dog) if not name.startswith('_')]
print(f"Public attributes")
print(public_attributes)


