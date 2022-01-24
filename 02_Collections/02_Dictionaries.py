# Dictionaries

# Key-Value pairs

my_dict = {"key": "value"}

table = {"name": "The Table", "colour": "Light brown", "height": 125, "length": 200, "price": "$450"}

# target something in a dictionary
# print(table["name"])  # DICTIONARY NAME [ KEY ]

table.update({"price": "$600", "height": 140})  # updates the dictionary
# print(table.get("price"))  # returns specified value for the chosen key
# print(table)

print(table.get("bogus", "default value"))  # accepts a default value
print(table["price"])  # if the key doesn't exist, it will throw a key error

car_table = {
    "brand": "Toyota",
    "model": "Aristo",
    "year": 2001,
    "size": {
        "length": "480cm",
        "width": "180cm",
        "height": "143cm"
    }
}

print(car_table.get("size").get("width"))
print(car_table.keys())
print(car_table.values())
print(car_table.items())
