#%% [markdown]
# ---
# ## Decoradores
# 
# - Decoradores **'alteram'** funções
# - Podemos montar nossos próprios decoradores

# #### Introdução a Decoradores
#%% [markdown]
# ---
# #### Vamos tentar decorar uma função manualmente:

#%%

def decorador(func):
    def wrapper():
        print("Olá ", end="")
        func()
        print("Meu nome é Vítor")
    return wrapper

def imprimir_nome():
    print("Maria")

imprimir_nome = decorador(imprimir_nome)

imprimir_nome()
# %% [markdown]
# ---
# #### Agora vamos decorar essa função de uma maneira mais 'pythônica'

# %%

# def decorador(func):
#     def wrapper(*args, **kwargs):
#         print("Olá ", end="")
#         func(*args, **kwargs)
#         print("Meu nome é Vítor")
#     return wrapper

def repetidor(n):
    def decorador(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
    
        return wrapper
    return decorador


@repetidor(100)
def imprimir_nome(nome):
    print(nome)

# É o mesmo que
# imprimir_nome = decorador(imprimir_nome)(nome)

imprimir_nome("João")

#%% [markdown]
# ---
# #### Agora vamos observar decoradores de classe: 
# ---
# #### `@property`
# - Também conhecido como `getter`
# - Faz com que um método seja tratado como uma propriedade

#%%

class Funcionario():
    def __init__(self, nome, sobrenome, funcao, anos_na_empresa=0):
        self.nome = nome
        self.sobrenome = sobrenome
        self.funcao = funcao
        self._anos_na_empresa = anos_na_empresa

    @property
    def anos_na_empresa(self):
        if self._anos_na_empresa > 20:
            return f"{self.nome} está há mais de 20 anos na empresa"
        return f"{self.nome} está há {self._anos_na_empresa} na empresa"

funcionario_1 = Funcionario("Maria", "Alves", "CEO", 25)
funcionario_2 = Funcionario("Jorge", "Albuquerque", "Zelador", 19)
print(funcionario_1.anos_na_empresa)
print(funcionario_2.anos_na_empresa)


#%% [markdown]
# ---
# #### `@____.setter`
# - É usado juntamente com @property
# - É usado para adicionar raciocínio ao tentar alterar o valor de uma propriedade
#%%

class Funcionario():
    def __init__(self, nome, sobrenome, funcao, anos_na_empresa=0):
        self.nome = nome
        self.sobrenome = sobrenome
        self.funcao = funcao
        self._anos_na_empresa = anos_na_empresa

    @property
    def anos_na_empresa(self):
        if self._anos_na_empresa > 20:
            return f"{self.nome} está há mais de 20 anos na empresa"
        return f"{self.nome} está há {self._anos_na_empresa} na empresa"

    
    @anos_na_empresa.setter
    def anos_na_empresa(self, novo_valor):
        if not isinstance(novo_valor, int):
            print("Valor não alterado. O valor precisa ser 'int'")
            return
        if novo_valor < 0:
            print("Valor não alterado. O valor precisa ser >= 0")
            return
        self._anos_na_empresa = novo_valor



funcionario_1 = Funcionario("Maria", "Alves", "CEO", 19)
funcionario_1.anos_na_empresa = 10  
print(funcionario_1.anos_na_empresa)

#%% [markdown]
# ---
# #### `@staticmethod`
# - Um **método estático** não depende de um objeto ser criado para ser invocado
# - Usado para métodos que podem ser úteis externamente ao objeto, como cálculos simples

#%%
import numpy as np

class CalculadoraVetores:
    @staticmethod
    def soma(vetor1, vetor2):
        return np.add(np.array(vetor1), np.array(vetor2))
    
    @staticmethod
    def subtracao(vetor1, vetor2):
        return np.subtract(np.array(vetor1), np.array(vetor2))
    
    @staticmethod
    def produto_escalar(vetor1, vetor2):
        return np.dot(np.array(vetor1), np.array(vetor2))

v1 = [1,2,3]
v2 = [0,2,0]

print(CalculadoraVetores.soma(v1, v2))
print(CalculadoraVetores.subtracao(v1, v2))
print(CalculadoraVetores.produto_escalar(v1, v2))

#%% [markdown]
# ---
# #### `@classmethod`
# - Atua como um construtor alternativo
# - Agora o primeiro argumento é 'cls' que representa a
#   classe em si, e não sua instância
#%%
from datetime import datetime


class Funcionario():
    def __init__(self, nome, sobrenome, funcao, anos_na_empresa=0):
        self.nome = nome
        self.sobrenome = sobrenome
        self.funcao = funcao
        self._anos_na_empresa = anos_na_empresa

    @property
    def anos_na_empresa(self):
        if self._anos_na_empresa > 20:
            return "Há mais de 20 anos"
        return self._anos_na_empresa
    
    @anos_na_empresa.setter
    def anos_na_empresa(self, novo_valor):
        if not isinstance(novo_valor, int):
            print("Valor não alterado. O valor precisa ser 'int'")
            return
        if novo_valor < 0:
            print("Valor não alterado. O valor precisa ser >= 0")
            return
        self._anos_na_empresa = novo_valor

    @classmethod
    def criar_pelo_ano_que_entrou(cls, nome, sobrenome, funcao, ano_que_entrou):
        if isinstance(ano_que_entrou, str):
            raise ValueError
        if ano_que_entrou < 1970: # ano de criação da empresa
            raise ValueError
        ano_atual = datetime.now().year
        anos_na_empresa = ano_atual - ano_que_entrou
        return cls(nome, sobrenome, funcao, anos_na_empresa)

func1 = Funcionario.criar_pelo_ano_que_entrou("Carlos", "Alberto", "Gerente", 1960)
print(func1.anos_na_empresa)
