def busca_sequencial(lista, val): #as aspas triplas significam "docstring" e tem a finalidade de gerar documentação.
    """ 
        Função que realiza uma busca sequencial em uma lista
        procurando por val.
        Se val for encontrado, retorna a posição de val na lista.
        Caso contrário, retorna o valor convencional -1.    
    """
# Percorre a lista de início ao fim usando range() e len()
# (precisamos ter acesso às posições dos elementos)
    for pos in range(len(lista)):
    # Encontru val; retorna a posição onde esta foi encontrada
        if val == lista[pos]: return pos 
    #<---- CUIDADO COM A INDENTAÇÃO AQUI
    #Percorreu toda a lista e não encontrou val: retorna -1
    return -1

###################################################################

# Para a busca sequencial, a lista NÃO PRECISA ESTAR ORDENADA

nums = [9, 21, 33, 12, 0, 18, -3, 30, -15, 6, 3, 27]

#TESTES

pos30 = busca_sequencial(nums, 30)
pos_menos3 = busca_sequencial(nums, -3)
pos19 = busca_sequencial(nums, 19)

print(" " * 40)
print(nums)
print(" " * 40)
print(f"Elemento 30 encontrado na posição {pos30}.")
print(" " * 40)
print(f"Elemento -3 encontrado na posição {pos_menos3}.")
print(" " * 40)
print(f"Elemento 19 encontrado na posição {pos19}.")
print(" " * 40)


