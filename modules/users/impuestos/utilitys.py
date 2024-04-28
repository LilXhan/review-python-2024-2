
if __name__ != "__main__":

    from ..gestion.crud import save

    print(__name__)

    def pay():
        print('paying')
        save()

if __name__ == "__main__":
    print("work of manteinment")