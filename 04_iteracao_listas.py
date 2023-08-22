#lista de frutas
frutas = ["laranja", "maçã", "uva", "pêra", "mamão", "abacate", "amora"]

#para percorrer uma lista e exibir apenas seus elementos,
#usamosw a estrutura for...in, como já visto no arquivo nº2 (iter em latin, significa caminho)

for f in frutas:
    print(f)

print('x' * 40)

#imprimindo uma lista de trás para a frente: reversed()

for x in reversed(frutas):
    print(x)

print(' ' * 40)
print('x' * 40)
print(' ' * 40)

#No entanto, frequentemente precisamos exibir, além do
#valor do elemento, também sua posição. Nesse caso, devemos 
#usar a estrutura for... in combinada com as funções range() e len()

for pos in range(len(frutas)):
    #print(frutas[pos], ":", pos)
    #print("A fruta ", frutas[pos], " está na posição", pos, ".")
    print(f"A fruta {frutas[pos]} está na posição {pos}.")

print(' ' * 40)
print('x' * 40)
print(' ' * 40)

#Às vezes é necessário percorrer a lista de trás pra frente,
# mas tendo acesso também à posição dos elementos. Para isso, 
# usamos a estrutura for...in, range() com três parâmetros e len()

for i in range(len(frutas) -1, -1, -1): 
    print(f"A fruta {frutas[i]} está na posição {i}.")

print(' ' * 40)
print('x' * 40)
print(' ' * 40)

