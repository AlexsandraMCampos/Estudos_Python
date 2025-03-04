# Faça um programa que leia um número inteiro e diga se ele é ou não primo

n = int(input('Informe um número: ')) # solicita um número
total = 0 # variavel para agrupar os mulplos

for i in range(1, n+1): # intervalo do laço do 1 ao numero +1, para entrar o número digitado
    if n % i == 0: # checagem se o número é divisivel
        print('\33[34m', end= '') # atribuindo cor ao divisivel
        total += 1 # adicionando os divisiveis dentro da variavel
    else:
        print('\33[31m', end= '') # atribuindo cor aos não divisiveis
    print('{}'.format(i) , end=" ") # apresentando todos os números divisiveis e não divisiveis

print(f'\n\033[mO número {n} foi divisível por {total} valores,')
if total == 2: # condição para ser primo
    print("e por isso ele é primo.")
else:
    print("e por isso ele não é primo.")

    
       
