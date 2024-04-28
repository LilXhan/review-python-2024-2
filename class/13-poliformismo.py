from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def save(self):
        pass


class User(Model):
    def save(self):
        print('guardando en BBDD')

class Sesion(Model):
    def save(self):
        print('save in archive')


def save(entitys):
    for entity in entitys:
        entity.save()

user = User()
sesion = Sesion()

save([sesion, user])