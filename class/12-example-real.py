from abc import ABC, abstractmethod

class Model(ABC):

    @property
    @abstractmethod
    def table(self):
        pass
    
    @abstractmethod
    def save(self):
        pass

    @classmethod
    def find_id(self, _id):
        print(f'buscando por id: {_id} en la tabla {self.table}')

class User(Model):
    table = 'User'

    def save(self):
        print('guardando')

usuario = User()
usuario.save()
User.find_id(1)