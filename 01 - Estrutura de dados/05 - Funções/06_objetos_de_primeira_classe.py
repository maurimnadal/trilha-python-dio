def somar(a, b):
    return a + b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")


exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20

def multiplicar(c, d):
    return c * d

def exibir_resultado2(c, d, funcao1, operacao):
    resultado1 = funcao1(c, d)
    operacao = "multiplicação"
    print(f"O resultado da {operacao} de {c} * {d} é = {resultado1}")

exibir_resultado2(2, 5, multiplicar, "multiplicação")