# Sets

# Sets have NO ORDER. They are random. They are also mutable
# Every item in a set HAS to be UNIQUE
# they are really good for printing/using unique values in a list

pokemon = {"Bulbasaur", "Squirtle", "Charmander"}

print(pokemon, type(pokemon))

pokemon.add("Pikachu")
print(pokemon, type(pokemon))
pokemon.discard("Bulbasaur")
print(pokemon, type(pokemon))

l = [1,2,3,4,5,6,7,8,9,0,6,54,3,4,5,7,8,]

print(l)
print(set(l))

# Frozen set
# Frozen sets are IMMUTABLE

x = frozenset(["let", "it", "go"])
print(x)

