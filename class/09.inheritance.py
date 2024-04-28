class Animal:
    def eat(self):
        print("eating")

class Dog(Animal):
    def walk(self):
        print("walkend")

class Pedrito(Dog):
    def programming(self):
        print("programming")


dog = Pedrito()
dog.eat()
dog.walk()
dog.programming()
