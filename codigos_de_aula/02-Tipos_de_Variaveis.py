# %% [markdown]
# ### Tipos de dados básicos no Python

# %% [markdown]
# **Booleanos (True/False)**
# Representam valores lógicos (verdadeiro ou falso)

# %% Booleans
n = 2
is_even = True  # Verifica se é par
is_odd = not is_even  # Inverte o valor
print(n % 2 == 0)  # Testa se é par

# %% [markdown]
# **Strings (texto)**
# Sequências de caracteres entre aspas

# %% Strings
texto = "Exemplo de string"
multilinha = '''Texto
com múltiplas
linhas'''

# %% [markdown]
# **NoneType (valor nulo)**
# Representa a ausência de valor

# %% None
var = None
print(var is None)  # Verifica se é None

# %% [markdown]
# **Inteiros (int)**
# Números sem parte decimal

# %% Inteiros
idade = 25
quantidade = 100

# %% [markdown]
# **Números decimais (float)**
# Números com ponto flutuante

# %% Floats
preco = 29.99
pi = 3.14159
print(pi * idade)  # Operação entre tipos

# %% [markdown]
# **Números complexos (complex)**
# Números com parte real e imaginária

# %% Complexos
z1 = 2 + 3j
z2 = complex("4-2j")
print(z1 * z2)  # Multiplicação complexa

# %% [markdown]
# **Verificação de tipos**
# Usando type() para checar o tipo

# %% Type checking
print(type(3.0))  # Mostra o tipo float