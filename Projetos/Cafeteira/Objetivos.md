# Projeto: Simulador de Máquina de Café em Python

Bem-vindo ao projeto da Máquina de Café! O objetivo é aplicar seus conhecimentos sobre Programação Orientada a Objetos (POO), especialmente o uso de classes, para simular o funcionamento de uma máquina de café.

---

## Objetivos de Aprendizagem

* Entender e aplicar os conceitos de classes e objetos.
* Trabalhar com atributos e métodos de uma classe.
* Estruturar um programa de forma modular e organizada.
* Manipular dicionários e outras estruturas de dados.
* Implementar a lógica de um programa a partir de requisitos.

---

## Requisitos da Máquina de Café

Sua máquina de café virtual deverá ser capaz de:

1.  **Receber Pedidos:** Perguntar ao usuário o que ele gostaria de beber (`espresso`, `latte`, `cappuccino`, `mocha`).
2.  **Desligar:** O usuário deve poder desligar a máquina digitando `off`.
3.  **Imprimir Relatório:** O usuário deve poder ver os recursos restantes (`água`, `leite`, `café`, `chocolate`) e o dinheiro no caixa digitando `report`.
4.  **Verificar Recursos:** Antes de preparar uma bebida, a máquina deve verificar se há ingredientes suficientes.
5.  **Processar Moedas:** A máquina deve aceitar moedas de R$ 1.00, R$ 0.50, R$ 0.25 e R$ 0.10.
6.  **Verificar Transação:** Após o usuário inserir as moedas, a máquina deve verificar se o valor é suficiente para a bebida escolhida.
7.  **Preparar a Bebida:** Se a transação for bem-sucedida e houver ingredientes, a máquina deve "preparar" a bebida, deduzindo os ingredientes do estoque.
8.  **Calcular Troco:** Se o usuário pagar a mais, a máquina deve devolver o troco.

---

## Estrutura do Projeto: A Classe `CoffeeMachine`

Você implementará toda a lógica dentro da classe `CoffeeMachine`. Abaixo está um esqueleto da classe com os métodos que você precisará desenvolver.

### Atributos (a serem definidos no `__init__`)

* `water` (em ml)
* `milk` (em ml)
* `coffee` (em g)
* `chocolate` (em g)
* `money` (em R$)

### Métodos (a serem implementados)

1.  `__init__(self)`
    * Este é o construtor da classe. Ele deve inicializar os atributos da máquina com valores iniciais (ex: 500ml de água, 300ml de leite, etc.).

2.  `report(self)`
    * Este método deve imprimir o estado atual de todos os recursos, formatado de maneira clara.

3.  `check_resources(self, drink_ingredients)`
    * Recebe um dicionário com os ingredientes necessários para uma bebida.
    * Retorna `True` se todos os ingredientes forem suficientes, e `False` caso contrário, informando qual ingrediente está faltando.

4.  `process_coins(self)`
    * Solicita ao usuário que insira a quantidade de cada moeda (R$1, R$0.50, R$0.25, R$0.10).
    * Calcula e retorna o valor total inserido em R$.

5.  `check_transaction(self, money_received, drink_cost)`
    * Recebe o dinheiro do usuário e o custo da bebida.
    * Retorna `True` se o dinheiro for suficiente, ou `False` se for insuficiente.
    * Se o pagamento for maior que o custo, calcula e exibe o troco.

6.  `make_coffee(self, drink_name, drink_ingredients)`
    * Recebe o nome da bebida e o dicionário de ingredientes.
    * Deduz a quantidade de ingredientes usados dos recursos da máquina.
    * Imprime uma mensagem de sucesso, como "Aqui está o seu {drink_name}. Aproveite!".

7.  `run(self)`
    * Este será o método principal que executa a máquina.
    * Ele deve conter um loop `while` que continua perguntando ao usuário o que ele quer, até que a entrada seja `off`.
    * Dentro do loop, ele deve chamar os outros métodos na ordem correta para processar um pedido.

---

Use os dicionários `COFFEE_PRICES` e `COFFEE_RECIPES` fornecidos para obter os preços e as receitas de cada bebida. Boa sorte!