# %% [markdown]
# ## Funções em Python
# Blocos de código reutilizáveis que realizam tarefas específicas

# %% [markdown]
# ### Introdução às Funções

# %% Função básica sem parâmetros
temp_farenheit = 100

def converter_fahrenheit_para_celsius():
    """Converte temperatura de Fahrenheit para Celsius"""
    C = (temp_farenheit - 32) / 1.8
    print(f"Temperatura em Celsius: {C}")
    print(f"Quadrado da temperatura: {C**2}")

# Chamando a função
converter_fahrenheit_para_celsius()

# %% [markdown]
# ### Funções com Argumentos

# %% Função com parâmetros posicionais e nomeados
def apresentador(nome, curso):
    """Apresenta uma pessoa e seu curso"""
    print(f"Olá, meu nome é {nome}, estou fazendo {curso} na UnB")

# Diferentes formas de chamar a função
apresentador(curso="Engenharia Civil", nome="Vitor")
apresentador("José", curso="Medicina")
apresentador("Maria", "Artes Visuais")

# %% [markdown]
# ### Retorno de Valores

# %% Função com múltiplos retornos
z = 10  # Variável global

def funcao_quadratica(x):
    """Calcula função quadrática usando variável global z"""
    y = x**2 + 2*x - z
    return x, y  # Retorna tupla com múltiplos valores

# Testando a função para vários valores
print("\nResultados da função quadrática:")
for i in range(11):
    x, y = funcao_quadratica(i)
    print(f"f({x}) = {y}")

# %% [markdown]
# ### Parâmetros Padrão

# %% Função com parâmetros opcionais
def funcao_quadratica_parametrizada(x, a=1, b=1, c=1):
    """Calcula função quadrática com coeficientes ajustáveis"""
    y = a*x**2 + b*x + c
    return x, y

# Testando com diferentes parâmetros
print("\nFunção quadrática personalizada:")
print(f"Padrão: {funcao_quadratica_parametrizada(2)}")
print(f"Customizada: {funcao_quadratica_parametrizada(2, a=3, b=-5, c=2)}")

# %% [markdown]
# ### Argumentos Arbitrários (*args)

# %% Função com número variável de argumentos
def somar(*numeros):
    """Soma quantidades arbitrárias de números"""
    total = sum(numeros)
    return total, len(numeros)

# Chamando com vários argumentos
resultado, qtd_numeros = somar(1, 22, 4, 3, 56, 4, 3)
print(f"\nSoma de {qtd_numeros} números: {resultado}")

# %% [markdown]
# ### Argumentos Nomeados Arbitrários (**kwargs)

# %% Função com argumentos nomeados variáveis
def gerar_emails(sufixo="", **domínios):
    """Gera emails a partir de domínios e listas de nomes"""
    lista_emails = []
    for domínio, nomes in domínios.items():
        for nome in nomes:
            lista_emails.append(f"{nome}@{domínio}.com{sufixo}")
    return lista_emails

# Exemplo de uso
emails_gerados = gerar_emails(
    sufixo=".br",
    gmail=["vitorcosta", "mariaelizabet36"],
    hotmail=["gustavinho35"],
    yahoo=["robloxgratis", "seu_erivaldo"]
)

print("\nLista de emails gerados:")
for email in emails_gerados:
    print(email)

# %% [markdown]
# ### Funções Lambda (Anônimas)

# %% Função lambda equivalente
funcao_lambda = lambda x, a, b, c: a*x**2 + b*x + c

print("\nResultado com função lambda:")
print(f"f(2) = {funcao_lambda(2, 3, -5, 2)}")