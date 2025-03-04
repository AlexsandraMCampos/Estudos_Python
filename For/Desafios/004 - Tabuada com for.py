# Crie um programa que solicite um número e faça a tabuada de 1 a 10 deste número

n = int(input('Escolha um número para tabuada: '))

for i in range(0,10):
    i+=1
    tabuada = n * i
    print(f'{n}x {i} = {tabuada}')