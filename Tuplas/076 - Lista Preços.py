# Criar um programa que apresente uma listagem de preços

produtos = ("Esmalte", "4,75", "Acetona", "8,99", "Lixa de Unha","2,50","Algodão","15,50","Fortalecedor de Unhas", "23,50")
print("_"*40) # linha tracejada 
print(f'{"LISTA DE PREÇOS":^40}') # rotulo da tabela  ^40 indica que o texto será centalizado dentro do espaço de 40
print("_"*40)
for p in range(0, len(produtos)): #percorrer a tupla até o seu final (len(produtos))
    if p %2 == 0: # selecionar os objetos com indice par
        print(f'{produtos[p]:.<30}', end=" ") #alinhar esses objetos a direita .<30 (essa função alinha o objeto a esquerda e cria uma linha pontilhada com 30 caracteres)
    else:
        print(f'R${produtos[p]:.>6}') # agora o alinhamento é a direita para os elementos com indice impar
print("_"*40)
