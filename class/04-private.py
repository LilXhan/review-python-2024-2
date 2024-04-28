class Dog:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def speak(self):
        print(f'{self.__name} dice: Guau')

    @classmethod
    def factory(cls):
        return Dog('Pepe', 15)


my_dog = Dog.factory()
my_dog.speak()

# no hacer

my_dog._Dog__name = "Hackeado"
print(my_dog.get_name())