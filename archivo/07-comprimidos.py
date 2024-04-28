from pathlib import Path
from zipfile import ZipFile

with ZipFile("archivo/comprimidos.zip", "w") as zip:
    for path in Path().rglob("*.*"):
        print(path)
        if str(path) != "archivo/comprimidos.zip":
            zip.write(path)


with ZipFile("archivo/comprimidos.zip") as zip:
    print(zip.namelist())

    info = zip.getinfo("archivo/07-comprimidos.py")
    print(info.file_size)
    print(info.compress_size)

    zip.extractall("archivo/descomprimidos") # extract archives