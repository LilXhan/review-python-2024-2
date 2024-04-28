class Animal:
    def eat(self):
        print("eating")

    def walk(self):
        print('walk to animal')

class Dog:
    def walk(self):
        print("walkend")

class Pedrito(Dog, Animal):
    def programming(self):
        print("programming")

dog = Pedrito()
dog.walk() # walkend