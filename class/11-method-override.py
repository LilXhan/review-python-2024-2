class Ave:

    def __init__(self):
        self.vuela = "volador"

    def fly(self):
        print('flying ave')


class Pato(Ave):
    def __init__(self):
        super().__init__()
        self.nada = "nadador"

    def fly(self):
        super().fly() # flying ave
        print('flying pato')

pato = Pato()
pato.fly()
print(pato.nada)
print(pato.vuela)