#  96 Desafio funções: Crie um programa que receba os comprimentos de base e altura e calcule a área do tereno:

a = int(input('Informe a largura do terreno (m): '))
b = int(input('Informe o comprimento do terreno (m): '))

def area(a,b):
    area = a * b
    print(f'A área do terreno de {a} m x {b} m é {area} m2.')

area(a,b)




