from pathlib import Path

path = Path('paths')
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename('chanchito-feliz')


archivos = [p for p in path.iterdir() if not p.is_dir()]
archivos = [p for p in path.glob("*.py")] # .py
archivos = [p for p in path.glob("**/*.py")]
archivos = [p for p in path.rglob("*.py")]
print(archivos)