# Função que calcula o IMC de uma pessoa
def calc_imc(peso, altura):
    return peso / altura ** 2

# p = 85
# a = 1.72
# imc = calc_imc(p, a)

# print(imc)

print(calc_imc(85, 1.72))

################################################################

from math import pi

"""
FUNÇÃO CALCULA A ÁREA DE UMA FIGURA GEOMÉTRICA PLANA (o nome disso é docstring)
"""
def calc_area(base, altura, tipo):
    resultado = None     #valor não existente

    if tipo == "R":     #retângulo
        resultado = base * altura              
    elif tipo == "T":      #triângulo
         resultado = base * altura / 2
    elif tipo == "E":  #elipse
        resultado = (base / 2) * (altura / 2) * pi

    return resultado 
    
print("Retângulo 20x30: ", calc_area(20, 30, "R"))
print("Triângulo 45x32: ", calc_area(45, 32, "T"))
print("Elipse 10x15: ", calc_area(10, 15, "E"))
print("DESCONHECIDO 12x16: ", calc_area(12, 16, "X"))