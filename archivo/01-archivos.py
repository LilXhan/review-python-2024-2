from pathlib import Path
from time import ctime

archivo = Path("archivo/archivo-prueba.txt")
# archivo.exists()
# archivo.rename()
# archivo.unlink()

print("acceso", ctime(archivo.stat().st_atime))
print("creacion", ctime(archivo.stat().st_ctime))
print("modificacion", ctime(archivo.stat().st_mtime))
