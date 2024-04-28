from pathlib import Path

Path(r'C:\Archivos de Programa\Minecraft')
Path('/usr/bin') # ruta absoluta
Path()
Path.home()
Path("one/__init__.py") # ruta relativa

path = Path("hello-mundo/this-ruta-relative.py")
path.is_file()
path.is_dir()
path.exists()

print(
    path.name,
    path.stem,
    path.suffix,
    path.parent,
    path.absolute()
)

p = path.with_name("chanchito.exe")
print(p)
p = path.with_suffix(".bat")
print(p)
p = path.with_stem("feliz")
print(p)