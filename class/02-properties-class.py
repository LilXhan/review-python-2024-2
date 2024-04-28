class Dog:

    paws = 4

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'{self.name} speak: Guau!')

# property = attribute
Dog.paws = 3

my_dog = Dog('Pepe', 15)
my_dog.paws = 5
my_dog2 = Dog('Felipe', 15)
print(my_dog.paws) # 5
print(Dog.paws) # 3
print(my_dog2.paws) # 3