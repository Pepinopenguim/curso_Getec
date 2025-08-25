
# %% [markdown]
# ## Dicionários em Python
# 
# Características:
# - Mutáveis
# - Aceitam chaves (keys) de tipos imutáveis e valores (values) de qualquer tipo
# - Não aceitam chaves repetidas
# - Indexáveis por suas chaves (não por posição numérica)
# - Ordenados por ordem de inserção (a partir do Python 3.7)

# %% Criando e acessando dicionários
# Dicionários são definidos por pares de {chave: valor}
concreto = {
    "tipo": "CA",
    "resistencia": 500,  # em MPa
    "diametro": 12,      # em mm
}

print("Dicionário completo:", concreto)
# Acessamos um valor através de sua chave correspondente
print("Resistência do concreto:", concreto["resistencia"])

# %% Modificando dicionários e suas propriedades
# Para adicionar um novo par chave-valor, basta atribuir um valor a uma nova chave
concreto["idade"] = 30  # em horas

# Para alterar um valor, basta reatribuí-lo usando a chave existente
concreto["resistencia"] -= 100
print("\\nDicionário modificado:", concreto)

# A função len() retorna o número de pares chave-valor
print("Número de propriedades:", len(concreto))

# O operador 'in' verifica se uma CHAVE existe no dicionário
print("\\nA chave 'tipo' existe?", "tipo" in concreto)
print("A chave 'CA' existe?", "CA" in concreto) # Retorna False, pois 'CA' é um valor

# %% Iterando sobre dicionários
print("\\nIterando sobre as chaves e valores:")
# Ao iterar diretamente, percorremos as chaves do dicionário
for key in concreto:
    value = concreto[key]
    print(f"{key}: {value}")

# O método .items() é muito útil para obter a chave e o valor de uma só vez
print("\\nIterando com o método .items():")
for key, value in concreto.items():
    print(f"{key} --- {value}")

# %% Estruturas de dados aninhadas e construtores
# Os valores de um dicionário podem ser de qualquer tipo, inclusive listas
concreto["dias_de_concretagem"] = ["segunda", "terça"]
print("\\nAdicionando uma lista como valor:", concreto)

# Também é possível criar dicionários usando o construtor dict()
pessoa = dict(nome="Felipe", sobrenome="Luis", idade="40")
print("\\nDicionário criado com dict():", pessoa)

# %% [markdown]
# ## Problema Prático: Contador de Palavras Únicas
# Dada uma string de texto, o objetivo é criar um programa que conte a frequência de cada palavra.

# %% Solução com dicionários
frase = "Maria Pedro Samuel Pedro Samuel Maria Maria Maria Pedro Karen José José Samuel Karen Samuel Maria Samuel Pedro Pedro José Mário Karen Emília Vítor Karen Vítor Vítor Mário Mário Karen Karen Samuel Vítor Mário Vítor Maria Maria Pedro Karen José Maria Samuel Emília Pedro José Emília Samuel Vítor Emília Mário Karen Pedro Karen Emília Mário Karen Mário Karen Pedro Maria"

# 1. Separar a string em uma lista de palavras (nomes)
lista_de_nomes = frase.split(" ")

# 2. Inicializar um dicionário vazio para armazenar a contagem
# A estrutura será {nome: numero_de_aparicoes}
contador = {}

# 3. Fazer um loop pela lista de nomes
for nome in lista_de_nomes:
    # 4. Checar se o nome já existe como chave no contador
    if nome in contador:
        # Se já existir, adicionar 1 ao seu valor (contador)
        contador[nome] += 1
    else:
        # Se não existir, adicioná-lo ao dicionário com o valor inicial 1
        contador[nome] = 1

print("\\nContagem final de nomes:")
print(contador)
