class Dog:
    def __init__(self, name):
        self.__name = name
    
    @property # solo funciona con getters
    def name(self):
        print('pasando por getter')
        return self.__name
        
    @name.setter
    def name(self, name):
        print('pasando por setter')
        if name.strip():
            self.__name = name
        return

    
dog = Dog('Choclo')
print(dog.name)