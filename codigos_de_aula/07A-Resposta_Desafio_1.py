# %% Variáveis

n = 100533267
eh_primo = None

# %% Resposta

if isinstance(n, int): # n é inteiro
    if n == 2 or n == 3:
        eh_primo = True
    elif n == 4:
        eh_primo = False
    else:
        for i in range(2, int(n / 2) + 1): # também pode usar int(n ** .5)
            if n % i == 0: # é divisível
                eh_primo = False
                break # não faz sentigo seguir o loop, já sabemos que é primo
                
        if eh_primo is None: # nenhum foi divisível
            eh_primo = True

    print(f"Para n={n}, eh_primo={eh_primo}")


else: # n não é inteiro
    print(f"Cuidado! n não é inteiro, é um {type(n)}")



