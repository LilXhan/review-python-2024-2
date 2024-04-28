class Dog:

    paws = 4

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # factory method -> create objects of my class
    # en comun de todas nuestras instancias
    @classmethod
    def speak(cls):
        print('Guau!')

    @classmethod
    def factory(cls):
        return cls("Pig happy", 4)

Dog.speak()

dog1 = Dog('Felipe', 20)
dog1 = Dog('Pig', 15)
dog3 = Dog.factory()
print(dog3.age, dog3.name)


