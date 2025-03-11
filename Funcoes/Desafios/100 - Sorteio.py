# Crie um programa que sorteie 5 números,
# some os números pares deste sorteio e apresente a lista de números sorteados e a soma dos números pares do sorteiro


from random import randint
from time import sleep

def sorteio(lista):
    print("Sorteio: ", end=" ")
    for i in range(5):  # Não precisa (0,5), só (5) já é suficiente
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.3)
    print("- Sorteio Finalizado.")

def somar_par(lista):  # Nome correto da função
    soma = sum(valor for valor in lista if valor % 2 == 0)  # Usando list comprehension para somar os pares
    print(f"Somando os valores pares de {lista}, temos: {soma}")

# Criando a lista de números
numeros = []
sorteio(numeros)
somar_par(numeros)  # Chamada corrigida
