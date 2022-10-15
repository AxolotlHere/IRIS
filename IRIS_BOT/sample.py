import pandas as pd


data_poke = pd.read_excel("Pokedex.xlsx")
poke_names = list(data_poke.Pokemon)
print(len(poke_names))

print(poke_names.index("Malamar"))