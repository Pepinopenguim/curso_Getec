

# Dicionário com os preços das bebidas em Reais (R$)
COFFEE_PRICES = {
    "espresso": 1.00,
    "latte": 2.25,
    "cappuccino": 3.00,
    "mocha": 4.10,
}

# Dicionário com as receitas de cada bebida
COFFEE_RECIPES = {
    "espresso": {
        "water": 50,      # ml
        "coffee": 18,     # g
    },
    "latte": {
        "water": 200,     # ml
        "milk": 150,      # ml
        "coffee": 24,     # g
    },
    "cappuccino": {
        "water": 250,     # ml
        "milk": 100,      # ml
        "coffee": 24,     # g
    },
    "mocha": {
        "water": 250,     # ml
        "milk": 100,      # ml
        "coffee": 24,     # g
        "chocolate": 20,  # g
    }
}


class CoffeeMachine:
    """
    Uma classe para simular uma máquina de café. Os alunos devem preencher
    a lógica de cada método.
    """
    def __init__(self):
        """
        Inicializa a máquina com os recursos padrão.
        Dica: Crie atributos aqui para água, leite, café, etc.
        """
        # definir ingredientes
        # maneira 1 (utilizado)
        self.ingredientes = {
            "water":2000,      #ml
            "milk":1500,       #ml
            "coffee":2000,     #g
            "chocolate":1500,  #g
        }

        self.dinheiro = 0



        # maneira 2 (menos eficiente)
        self.water = 2000      # ml
        self.milk = 1500       # ml
        self.coffee = 2000     # g
        self.chocolate = 1500  # g

    def report(self):
        """
        Imprime um relatório dos recursos atuais.
        """
        result = (
            "=== Ingredientes ===\n"
            f"Água: {self.ingredientes["water"]} ml\n"
            f"Leite: {self.ingredientes["milk"]} ml\n"
            f"Café: {self.ingredientes["coffee"]} g\n"
            f"Chocolate: {self.ingredientes["chocolate"]} g\n"
            f"Dinheiro na máquina: R${self.dinheiro:.2f}"
        )

        print(result)


    def checar_ingredientes(self, drink_ingredients):
        """
        Verifica se há recursos suficientes para fazer a bebida.
        Retorna True se houver, False caso contrário.
        """
        for ingrediente, quantidade in drink_ingredients.items():
            quantidade_na_maquina = self.ingredientes[ingrediente]

            if quantidade_na_maquina < quantidade:
                return False
        
        return True



    def processar_moedas(self):
        """
        Solicita ao usuário para inserir moedas e retorna o valor total.
        """

        ask = (
            "Por favor insira uma moeda:\n"
            "Digite 100 - R$ 1,00\n"
            "Digite 50 - R$ 0,50\n"
            "Digite 25 - R$ 0,25\n"
            "Digite 10 - R$ 0,10\n"
            "Aperte enter ao finalizar\n"
            "> "
        )

        pergunta = input(ask)
        valor_inserido = 0 # centavos

        while pergunta != "":
            if pergunta not in ("100", "50", "25", "10"):
                print("Moeda inválida!")
                pergunta = input(ask)
                continue
            
            valor_inserido += int(pergunta) # em centavos
            pergunta = input("> ")
        
        return valor_inserido

    def checar_transacao(self, valor_recebido, custo_da_bebida):
        """
        Verifica se o pagamento é suficiente. Retorna False caso contrário.
        Se suficiente, retorna o troco necessário, em moedas
        """
        if valor_recebido < custo_da_bebida:
            return False

        self.dinheiro += custo_da_bebida / 100

        moedas_do_troco = {
            "1 real":0,
            "50 centavos":0,
            "25 centavos":0,
            "10 centavos":0,
        }

        troco = valor_recebido - custo_da_bebida

        while troco >= 100:
            troco -= 100
            moedas_do_troco["1 real"] += 1

        while troco >= 50:
            troco -= 50 
            moedas_do_troco["50 centavos"] += 1
        
        while troco >= 25:
            troco -= 25 
            moedas_do_troco["25 centavos"] += 1

        while troco >= 10:
            troco -= 10 
            moedas_do_troco["10 centavos"] += 1
        
        return moedas_do_troco



    def fazer_cafe(self, nome_da_bebida):
        """
        Deduz os ingredientes necessários dos recursos e "prepara" o café.
        """

        ingredientes_da_bebida = COFFEE_RECIPES[nome_da_bebida]

        for ingrediente, quantidade in ingredientes_da_bebida.items():
            self.ingredientes[ingrediente] -= quantidade

        print(
            "Aqui está sua bebida!\n"
            f"Aproveite seu {nome_da_bebida}"
        )

    def entregar_troco(self, moedas_do_troco):
        """
        Devolve as moedas ao usuário
        """
        if all((i==0 for i in moedas_do_troco.values())):
            return
        print("Troco devolvido:")
        for nome, quantidade in moedas_do_troco.items():
            if quantidade > 0:
                print(f"{nome}: {quantidade}")

    def run(self):
        """
        Executa o loop principal da máquina de café, processando os comandos
        do usuário.
        """
        # Iniciar a máquina com um loop
        print("Bem vinda à máquina de café do Python!!!")
        ask = "Escolha uma bebida:\n"
        for drink, price in COFFEE_PRICES.items():
            ask += f" - {drink}: R${price:.2f}\n"
        ask += "> "
        bebida_escolhida = input(ask).lower()

        while bebida_escolhida != "fim":
            # checar se escolha foi válida
            if bebida_escolhida not in COFFEE_PRICES.keys():
                if "rep" in bebida_escolhida:
                    self.report()
                    bebida_escolhida = input(ask).lower()
                    continue

                print(
                    "Insira uma bebida válida!\n"
                    f"{bebida_escolhida} não é uma bebida válida!"
                )
                bebida_escolhida = input(ask).lower()
                continue
            
            # a máquina deve checar os ingredientes
            # 1. pegar os ingredientes da escolha
            ingredientes:dict = COFFEE_RECIPES[bebida_escolhida]
            
            tem_ingredientes:bool = self.checar_ingredientes(ingredientes)

            if not tem_ingredientes:
                print("Não há ingredientes para essa bebida :/")
                bebida_escolhida = input(ask).lower()
                continue

            # o usuário deve inserir moedas
            valor_inserido = self.processar_moedas()

            # a máquina deve contar essas moedas
            # a máquina deve processar o troco

            moedas_do_troco = self.checar_transacao(
                valor_recebido=valor_inserido, # em centavos
                custo_da_bebida=COFFEE_PRICES[bebida_escolhida] * 100
            )

            if moedas_do_troco == False:
                print("Valor insuficiente")
                bebida_escolhida = input(ask).lower()
                continue

            # a máquina deve atualizar a quantidade de ingredientes
            # 'fazer o café'
            self.fazer_cafe(bebida_escolhida)

            # a máquina deve entregar o troco
            self.entregar_troco(moedas_do_troco)
            
            bebida_escolhida = input(ask).lower()
        



# ----- Ponto de Partida para os Alunos -----

# 1. Imprima os objetivos para o aluno ver as instruções.
#print(project_objectives)

# 2. Crie uma instância (objeto) da sua classe.
maquina_de_cafe = CoffeeMachine()

# 3. Chame o método 'run' para iniciar a máquina.
maquina_de_cafe.run()