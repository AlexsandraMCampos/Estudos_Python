# Crie um programa que vair gerar 5 números aleatórios e coloca-los em uma tupla. 
# Depois, mostre a listagem dos  números geradose indique o menor e o mairo valor desta tupla.

from random import randint #importar biblioteca que escolhe números aleatoriamente
from time import sleep #importar biblioteca que faz contagem com pausa

print("Início do sorteio")
print("Os valores sorteados são: ")

numeros = tuple(randint(1,100) for _ in range(5)) # escolher aleatoriamente 5 números e adicionar na tupla
for n in numeros:
    print(n, end=" ", flush=True) # imprime os número entre espaços e o flush True apresenta o número no instante que ele é sorteado
    sleep(0.5) # intervalo de 0.5 s entre o sorteio dos números

maior= max(numeros) # criação de variavél para armazenar o maior e menor valor gerado
menor= min(numeros)

print(f"O maior número sorteado foi {maior} e o menor foi {menor}.")