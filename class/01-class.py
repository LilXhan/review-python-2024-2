class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'{self.name} speak: Guau!')

# self = object or instance

my_dog = Dog('Pepito', 15)
my_dog.speak()
