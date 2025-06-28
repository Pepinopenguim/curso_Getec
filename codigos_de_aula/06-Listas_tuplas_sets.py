# %% [markdown]
# ## Listas em Python
# Características:
# - Mutáveis
# - Aceitam elementos repetidos
# - Indexáveis
# - Ordenadas

# %% Criando e acessando listas
frutas = ["maçã", "pêra", "abacaxi", "tomate", "melancia"]
print("Lista completa:", frutas)
print("Slice [:-1]:", frutas[:-1])  # Todos exceto último elemento

# %% Iterando sobre listas
print("\nÍndices e valores:")
for fruta in frutas:
    print(f"{fruta}: {frutas.index(fruta)}")  # Mostra índice de cada fruta

# %% Métodos de listas
frutas.append("abacate")  # Adiciona ao final
frutas.insert(2, "limão")  # Insere na posição 2
frutas.extend(["uva", "kiwi"])  # Adiciona múltiplos elementos
print("\nLista modificada:", frutas)

# %% [markdown]
# ## Tuplas em Python
# Características:
# - Imutáveis
# - Aceitam elementos repetidos
# - Indexáveis
# - Ordenadas

# %% Trabalhando com tuplas
coord1 = (1, -3, 2)
coord2 = (0, 2, 2)
print("\nCoordenada 1:", coord1)
print("Soma das primeiras coordenadas:", coord1[0] + coord2[0])

# %% [markdown]
# ## Sets (Conjuntos) em Python
# Características:
# - Mutáveis
# - Não aceitam elementos repetidos
# - Não indexáveis
# - Não ordenados

# %% Criando e manipulando sets
frutas_repetidas = ["maçã", "pêra", "abacaxi", "tomate", "melancia", "abacaxi", "tomate"]
frutas_set = set(frutas_repetidas)
print("\nSet de frutas (sem repetições):", frutas_set)

letras = set("abcdefg")
print("Set original de letras:", letras)

# %% Operações com sets
letra_qualquer = "e"
print(f"\nA letra '{letra_qualquer}' está no set?", letra_qualquer in letras)

print("\nRemovendo letras:")
for letra in "kdjvfargiojjkçljçoearig":
    if letra in letras:
        letras.remove(letra)
        print(f"'{letra}' removida - Set atual:", letras)
    else:
        print(f"'{letra}' não encontrada")

print("\nSet final:", letras)