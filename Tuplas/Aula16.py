# Tupla () / # Lista [] / # Dicionario {}

# Estudo de Tuplas => elas são imultaveis

# lanche = ('Hamburger', 'Suco','Pizza','Pudim')
# print(lanche)

# # Tuplas podem ser escritas com ou sem parenteses na versão atual do Python
lanche = 'Hamburger', 'Suco','Pizza','Pudim'
# print(lanche)

# # Fatiamentos
# print(lanche[-3]) 

# # Outra maneira de coletar o mesmo dado
# print(lanche[1])

# # apresenta os elementos de indice 0 a 1
# print(lanche[:2])

# lanche[1] = 'Refrigerante'
# print(lanche[1]) # retorna um erro por que as TUPLAS SÃO IMUTÁVEIS

# for comida in lanche:
#     print(f'Eu vou comer {comida}.')
# print('Comi para caramba!')

# Outra maneira de apresentar o mesmo resultado
# nesta opção o lanche[cont] pega a posição do elemento e apresenta o que contem
# for cont in range(0,len(lanche)):
#     print(f"Eu vou comer {lanche[cont]}.") 

for pos, comida in enumerate(lanche): # enumerate() indica a posição do elemento
        print(f"Eu vou comer {comida} na posição {pos}.") 