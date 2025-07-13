# %% [markdown]
# ---

# ## Trabalhando com Strings no Python

# %% [markdown]
# ---

# **Strings básicas e f-strings**
# Formas de declarar e formatar strings

# %% Declaração e formatação
nome = "Felipe"
sobrenome = 'Márcio'

# f-string (formatação moderna)
frase = f"Nome: {nome}, Sobrenome: {sobrenome}"
print(frase)

# %% [markdown]
# ---

# **Operações com strings**
# Concatenação e repetição

# %% Operadores
print("/" * 20)  # Repetição

inicio, fim = "aba", "cate"
print(inicio + fim)  # Concatenação

# %% [markdown]
# ---

# **Strings multilinha**
# Como quebrar strings em múltiplas linhas

# %% Multilinha
paragrafo = "\n"
texto = "Linha 1" + paragrafo + \
        "Linha 2" + paragrafo + \
        "Linha 3"
print(texto)

# %% [markdown]
# ---

# **Strings como arrays**
# Acessando caracteres e slices

# %% Indexação
alfabeto = "abcdefghijklmnopqrstuvwxyz"

print(alfabeto[4:])  # Slice
print("e" in alfabeto)  # Verificação

# Iteração
for letra in alfabeto:
    print(letra, end=" ")  # Imprime com espaço

# %% [markdown]
# ---

# **Métodos úteis**
# Operações comuns com strings

# %% Métodos
print(f"\nTamanho: {len(alfabeto)}")  # Length
print("A" in "Abacate")  # Busca (case sensitive)

# %% [markdown]
# ---

# **Exemplo prático**
# Demonstração simples

# %% Exemplo
vegetal = "abacate"
print(f"Substring 'cate' em {vegetal}: {'cate' in vegetal}")

# Repetição controlada
for _ in range(5):
    print("olá")