import math

f = lambda x: math.tan(x) ** 5
a = 0
b = math.pi / 3
n = 10

def resolver_integral(f, a, b, n):


    # calcular a integral de f(x) entre 0 e 100, para n iterações

    def A(h, xj, xi):
        # onde xj é o valor i - 1
        # xi é o valor i

        return h / 2 * (f(xj) + f (xi))



    # definir o h:
    h = (b - a) / n

    xj, xi = a, a + h
    I = 0

    while xi < b:

        I += A(h=h, xj=xj, xi=xi)

        xj += h
        xi += h

    return I

erro_baixo = resolver_integral(f, 0, 1, 10000)
erro_alto = resolver_integral(f, 0, 1, 10)

print(erro_alto, erro_baixo, erro_alto - erro_baixo, sep=" - ")