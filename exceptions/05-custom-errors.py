class MyError(Exception):
    "this class represent my error"

    def __init__(self, message, code):
        self.message = message
        self.code = code

    def __str__(self):
        return f'{self.message} - code: {self.code}'

def division(n = 0):
    if n == 0:
        raise MyError('Error', 404)
    
try:
    division()
except MyError as e:
    print(e)
