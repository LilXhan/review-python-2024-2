import json 
from pathlib import Path


# write json

products = [
    { "id": 1, "name": "Toyota"},
    { "id": 2, "name": "KIA"},
    { "id": 3, "name": "Chevrolet"}
]

data = json.dumps(products)
Path("./data.json").write_text(data)


# read

data2 = Path("./data.json").read_text(encoding="utf-8")
products = json.loads(data2)

# modified json

products[0]["name"] = "chanchito feliz"
Path("./data.json").write_text(json.dumps(products))