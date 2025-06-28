# %% [markdown]
# ## Dicionários em Python
# Estruturas chave-valor mutáveis e indexadas por chaves

# %% Criando e acessando dicionários
concreto = {
    "tipo": "CA",
    "resistencia": 500,  # MPa
    "diametro": 12,  # mm
}

print("Resistência do concreto:", concreto["resistencia"])

# %% [markdown]
# ### Modificando dicionários existentes

# %% Adicionando e alterando valores
concreto["idade"] = 30  # horas
concreto["resistencia"] -= 100  # Reduz a resistência
print("Dicionário atualizado:", concreto)

# %% [markdown]
# ### Operações úteis com dicionários

# %% Tamanho e verificação de chaves
print("Número de propriedades:", len(concreto))
print("'CA' é uma chave?", "CA" in concreto)  # Verifica apenas chaves

# %% [markdown]
# ### Iterando sobre dicionários

# %% Percorrendo itens do dicionário
print("\nPropriedades do concreto:")
for chave, valor in concreto.items():
    print(f"{chave}: {valor}")

# %% [markdown]
# ### Valores podem ser de qualquer tipo

# %% Valores complexos
concreto["dias_de_concretagem"] = ["segunda", "terça"]
print("\nDicionário com lista:", concreto)

# %% [markdown]
# ### Alternativas para criar dicionários

# %% Usando dict()
pessoa = dict(nome="Felipe", sobrenome="Luis", idade="40")
print("\nDicionário criado com dict():", pessoa)

# %% [markdown]
# ## Aplicação Prática: Contador de Palavras

# %% Problema: Contador de palavras únicas
frase = """Maria Pedro Samuel Pedro Samuel Maria Maria Maria Pedro Karen José José Samuel Karen Samuel Maria Samuel Pedro Pedro José Mário Karen Emília Vítor Karen Vítor Vítor Mário Mário Karen Karen Samuel Vítor Mário Vítor Maria Maria Pedro Karen José Maria Samuel Emília Pedro José Emília Samuel Vítor Emília Mário Karen Pedro Karen Emília Mário Karen Mário Karen Pedro Maria"""

# %% Implementação do contador
lista_de_nomes = frase.split(" ")
contador = {}

for nome in lista_de_nomes:
    if nome in contador:
        contador[nome] += 1
    else:
        contador[nome] = 1

print("\nContagem de nomes:")
for nome, quantidade in sorted(contador.items()):
    print(f"{nome}: {quantidade}")