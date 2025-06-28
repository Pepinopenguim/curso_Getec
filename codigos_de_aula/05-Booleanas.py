# %% [markdown]
# ## Booleanos e Operadores Lógicos

# %% Booleanos básicos
python_eh_bom = True
Estruturas_melhor_area = True
florestal_eh_engenharia = False  # Não fazem C1

# %% [markdown]
# **Operadores de comparação**
# AND, OR e NOT

# %% Comparadores lógicos
print("AND:", True and False)
print("OR:", False or 3 > 4)
print("NOT:", not True)

# %% [markdown]
# **Comparação de valores vs identidade**
# == vs is

# %% Igualdade vs Identidade
v1 = [1, 2, 1]
v2 = [1, 2, 1]
print("Valores iguais?", v1 == v2)  # Compara conteúdo
print("Mesmo objeto?", v1 is v2)    # Compara identidade

# %% [markdown]
# **Operadores relacionais**
# >, <, >=, <=, !=

# %% Relacionais
print("Maior que:", 2 > 1)
print("Diferente:", 3 != 2 + 1)

# %% [markdown]
# ## Controle de Fluxo

# %% [markdown]
# **Estrutura condicional if-elif-else**

# %% If-elif-else
var = 5
if var > 0:
    print(f"{var} é positivo")
elif var > -5:
    print(f"{var} está entre -5 e 0")
else:
    print(f"{var} é menor que -5")

# %% [markdown]
# **Estrutura match-case (Python 3.10+)**
# Similar ao switch-case

# %% Match-case
var = 3
match var:
    case 0: print("zero")
    case 1: print("um")
    case 2: print("dois")
    case 3: print("três")
    case _: print("outro valor")

# %% [markdown]
# ## Loops

# %% [markdown]
# **Loop for**

# %% For loop
alphabeto = "abcdefghijklmnopqrstuvwxyz"
for letra in alphabeto[:5]:  # Primeiras 5 letras
    print(letra, end=" ")

# %% For com range
import time
for i in range(0, 5):
    time.sleep(0.5)
    print(i)

# %% [markdown]
# **Loop while**

# %% While básico
i = 0
while i <= 5:
    print(i)
    i += 1

# %% [markdown]
# **Controle de loops**
# break e continue

# %% Break e Continue
import random as rdm

# Exemplo com break
text = ""
while True:
    text += rdm.choice(alphabeto)
    if len(text) > 10:  # Para após 10 caracteres
        print("\nTexto gerado:", text)
        break

# Exemplo com continue
print("\nNúmeros pares:")
i = 0
while i <= 10:
    i += 1
    if i % 2 != 0:  # Pula ímpares
        continue
    print(i, end=" ")