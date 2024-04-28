from pathlib import Path

path = Path() # current path
paths = [p for p in path.iterdir() if p.is_dir()]

dependecies = {
    'db': 'data base',
    'api': 'this is a api',
    'graphql': 'graphql'
}

def load(p):
    package = __import__(str(p).replace('/', '.'))
    try:
        package.init(**dependecies)
    except:
        print('package not has method init')


list(map(load, paths))