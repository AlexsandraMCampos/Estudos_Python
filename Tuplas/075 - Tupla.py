# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
# a) quantas vezes  apreceu o valor 9.
# b) em que posição foi digitado o primeiro valor 3
# c) quais foram os números pares

numeros =tuple(int(input("Digite um número:")) for n in range(6))
print(f'Você digitou os números {numeros}.')
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1} posição.')
else:
    print(f"O valor 3 não foi digitado em nenhuma posição.")
print(f'Os valores pares digitados foram: ')

for n in numeros:
    if n%2 == 0:
        print(n, end=" ")
    



