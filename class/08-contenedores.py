class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'Product: {self.name} -  Price: {self.price}'

class Category:

    products = []

    def __init__(self, name, products):
        self.name = name
        self.products = products
    
    def add(self, product):
        self.products.append(product)

    def print_products(self):
        for product in self.products:
            print(product)

kayac = Product('Kayac', 1000)
car = Product('Car', 1500)
surfboard = Product('Surfboard', 1505)

deports = Category('Deports', [kayac, car])
deports.add(surfboard)
deports.print_products()