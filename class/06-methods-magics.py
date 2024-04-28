class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Destructor
    def __del__(self):
        print(f'bye dog {self.name}')

    def __str__(self):
        return f'class dog: {self.name}'

    def speak(self):
        print(f'{self.name} speak: Guau!')

dog = Dog('Chanchito', 15)
print(dog) # class dog: Chanchito
text = str(dog)
print(text) # class dog: Chanchito

del dog