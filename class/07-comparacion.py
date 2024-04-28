class Coordinates:
    def __init__(self, lat, len):
        self.lat = lat
        self.len = len

    # equal

    def __eq__(self, other):
        return self.lat == other.lat and self.len == other.len
    
    # not equal

    def __ne__(self, other):
        return self.lat != other.lat or self.len != other.len

    # mayor o menor

    def __lt__(self, other):
        return self.lat + self.len < other.lat + other.len


    # mayor o menos y igual

    def __le__(self, other):
        return self.lat + self.len <= other.lat + other.len

coords = Coordinates(45, 27)
coords2 = Coordinates(45, 27)
print(coords == coords2) # True
print(coords != coords2) # False
print(coords > coords2) # False
print(coords >= coords2) # True