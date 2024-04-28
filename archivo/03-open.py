from io import open

# write
text = "hello world"

archivo = open("archivo/hola-mundo.txt", "w")
archivo.write(text)
archivo.close()

# read
archivo = open("archivo/hola-mundo.txt", "r")
read_text = archivo.read()
archivo.close()
print(read_text)


# read to list []
archivo = open("archivo/hola-mundo.txt", "r")
read_text_list = archivo.readlines()
archivo.close()
print(read_text_list)


#######################

# with y seek

with open("archivo/hola-mundo.txt", "r") as archivo:
    print(archivo.readlines())
    archivo.seek(0)
    for line in archivo:
        print(line)

# add

archivo = open("archivo/hola-mundo.txt", "a+")
archivo.write("chao mundo")
archivo.close()


# lectura y escritura
with open("archivo/hola-mundo.txt", "r+") as archivo:
    text = archivo.readlines()
    archivo.seek(0)
    text[0] = "chanchito happy"
    archivo.writelines(text)