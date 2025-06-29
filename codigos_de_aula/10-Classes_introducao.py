# %% [markdown]
# ## Classes :D
# - Classes funcionam como um **projeto**
# - São o 'guia' para criar um objeto
# - Objetos possuem **'métodos'** e **'Parametros'**

# ### É por meio das classes que o Python se define como uma linguagem OOP  
# #### -> OOP - Object Oriented Programming

# %% [markdown]
# ## Criando uma classe e Método init
# - O método init **inicializa** a sua classe
# - É o método init que recebe os **argumentos**
# %%

class Carro():
    def __init__(self, marca, cor, ano):
        # Atributos básicos do carro
        self.marca = marca  # Armazena a marca do carro
        self.cor = cor      # Armazena a cor do carro
        self.ano = ano      # Armazena o ano de fabricação

# Criando instâncias da classe Carro
meu_carro = Carro("Ford", "Azul", 1985)
outro_carro = Carro("Renault", "Branco", 2011)

# Função que exibe informações do carro
def f(carro):
    print(f"Um carro tem cor {carro.cor}")
    print(f"Ele é da marca {carro.marca}")
    print(f"Ele foi fabricado em {carro.ano}")

# Modificando atributo após criação
outro_carro.cor = "Vermelho"  # Alterando a cor do segundo carro

# Exibindo informações dos carros
f(meu_carro)
print("-------")
f(outro_carro)

# %% [markdown]
# ## Definindo Métodos

# - São as 'funções' de uma 'classe'
# - Métodos podem alterar as propriedades de uma classe e realizar objetivos
# - No exemplo abaixo, o método **'acelerar'** altera a propriedade **'velocidade'** da classe
# %%

class Carro():
    def __init__(self, marca, cor, ano):
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.velocidade = 0  # Velocidade inicial sempre zero
    
    def atualizacao_velocidade(self):
        # Exibe a velocidade atual
        print(f"Agora carro está a {self.velocidade} km/h")

    def acelerar(self, v=1):
        # Aumenta a velocidade e exibe atualização
        self.velocidade += v
        self.atualizacao_velocidade()
    
    def desacelerar(self, v=1):
        # Diminui a velocidade (não permite negativa)
        if self.velocidade == 0:
            return
        self.velocidade -= v
        print(f"Agora carro está a {self.velocidade} km/h")

    def atualizacao(self):
        # Exibe todas as informações do carro
        print(f"Um carro tem cor {self.cor}")
        print(f"Ele é da marca {self.marca}")
        print(f"Ele foi fabricado em {self.ano}")
        print(f"Ele está a {self.velocidade} km/h")

# Testando os métodos
meu_carro = Carro("Ford", "Azul", 1985)

# Acelerando o carro 10 vezes
for i in range(10):
    meu_carro.acelerar(4)
meu_carro.atualizacao()

# Desacelerando o carro 5 vezes
for i in range(5):
    meu_carro.desacelerar()
meu_carro.atualizacao()

# %% [markdown]
# ## Heranças
# - Herança é a habilidade de uma classe tem de **herdar** as propriedades de outra classe 
# - Para Herdarmos essas propriedades, usamos a função ***super()***
# %%

# Classe base para todos os veículos
class Veiculo():
    def __init__(self, marca, cor, ano, tipo):
        self.tipo = tipo    # Tipo genérico do veículo
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.velocidade = 0
    
    def atualizacao_velocidade(self):
        # Método genérico para velocidade
        print(f"Agora {self.tipo} está a {self.velocidade} km/h")

    def acelerar(self, v=1):
        # Método genérico para acelerar
        self.velocidade += v
        self.atualizacao_velocidade()
    
    def desacelerar(self, v=1):
        # Método genérico para frear
        if self.velocidade == 0:
            return
        self.velocidade -= v
        print(f"Agora {self.tipo} está a {self.velocidade} km/h")

    def atualizacao(self):
        # Exibe informações genéricas do veículo
        print(f"Um {self.tipo} tem cor {self.cor}")
        print(f"Ele é da marca {self.marca}")
        print(f"Ele foi fabricado em {self.ano}")
        print(f"Ele está a {self.velocidade} km/h")

# Classe específica para carros
class Carro(Veiculo):
    def __init__(self, marca, cor, ano):
        # Herda tudo de Veiculo e define tipo como "Carro"
        super().__init__(marca, cor, ano, "Carro")

# Classe específica para caminhões (com atributo adicional)
class Caminhao(Veiculo):
    def __init__(self, marca, cor, ano, tamanho_da_carreta=0):
        super().__init__(marca, cor, ano, tipo="Caminhão")
        self.tamanho_da_carreta = tamanho_da_carreta  # Atributo exclusivo
    
    def atualizacao(self):
        # Chama o método da classe pai e adiciona info extra
        super().atualizacao()
        print(f"{self.tipo} possui {self.tamanho_da_carreta} metros de carreta")

# Testando a classe Caminhao
meu_caminhao = Caminhao("Mercedez", "azul", 2015, tamanho_da_carreta=9)
meu_caminhao.acelerar(20)
meu_caminhao.desacelerar(7)
meu_caminhao.atualizacao()