# %% Variáveis

lista_nomes = ["samuel moises:)", "#pedro henrique", "Emilly Mariane!", "vítor luís"]
nomedaempresa = "getec"
caracteres_proibidos = "#!&%$*@áéíóúâêîôû;.,:()[]{}"

# %% Resposta

nomedaempresa = nomedaempresa.lower()

for nome in lista_nomes:
    # remover caracteres proibidos
    for char_proibido in caracteres_proibidos:
        if char_proibido in nome:
            nome = nome.replace(char_proibido, "")
    
    # separar nome e sobrenome
    nome, sobrenome = nome.split(" ")

    nome, sobrenome = nome.lower(), sobrenome.lower()


    print(f"{sobrenome}.{nome}@{nomedaempresa}.com.br")


