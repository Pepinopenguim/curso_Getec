# %% [markdown]
# ---

# ## Trabalhando com Números no Python

# %% [markdown]
# ---

# **Tipos numéricos básicos**
# Inteiros (int) e operações aritméticas

# %% Inteiros e operadores básicos
i1, i2 = 32, 23
print(f"Soma: {i1 + i2}")
print(f"Subtração: {i1 - i2}")
print(f"Multiplicação: {i1 * i2}")
print(f"Divisão: {i1 / i2}")

# %% [markdown]
# ---

# **Operadores especiais**
# Resto, divisão inteira e exponenciação

# %% Operadores avançados
print(f"Resto da divisão: {23 % 12}")
print(f"Divisão inteira: {234 // 3}")
print(f"Exponenciação: {2**3}")

# %% [markdown]
# ---

# **Ordem de operações**
# Parenteses → Expoentes → Mult/Div → Add/Sub

# %% Precedência de operadores
print(f"Exemplo: {2 + 3 * 5**2}")  # 2 + (3 * (5²))

# %% [markdown]
# ---

# **Números decimais (float)**
# Conversão e operações

# %% Floats e conversão
f1, f2 = 3245252.9787549823, 2.0
print(f"Convertido para int: {int(f1)}")

# %% [markdown]
# ---

# **Números complexos**
# Representação e operações

# %% Números complexos
c1 = 2 + 3j
c2 = complex(10, -4)
print(f"Número complexo: {c2}")

# %% [markdown]
# ---

# **Sistemas numéricos**
# Hexadecimal e binário

# %% Hex e Binário
h1, h2 = 0x100, 0x2fd
print(f"Hex concatenado: {hex(h2)}{hex(h1)}")

b1 = 0b101010101
print(f"Binário de 203: {bin(203)}")

# %% [markdown]
# ---

# **Verificação de tipos**
# Usando type() e isinstance()

# %% Checagem de tipos
print(f"Tipo de b1: {type(b1)}")
print(f"É complexo?: {isinstance(c1, complex)}")

# %% [markdown]
# ---

# **Formatação de números**
# Arredondamento e exibição

# %% Formatação
num = 23489.26924
print(f"Arredondado: {num:.3f}")  # 3 casas decimais
print(f"Round padrão: {round(num)}")

# %% [markdown]
# ---

# **Bibliotecas úteis**
# Funções matemáticas e aleatórias

# %% Math e Random
import random as rdm
from math import sqrt, ceil, floor, pi, e
from numpy import pi as pi_numpy

print(f"Dado: {rdm.randint(1, 6)}")
print(f"Raiz quadrada: {sqrt(2347)}")
print(f"Teto: {ceil(34.001)}, Piso: {floor(34.993)}")
print(f"Pi (math): {pi}, Pi (numpy): {pi_numpy}")
print(f"Constante e: {e}")