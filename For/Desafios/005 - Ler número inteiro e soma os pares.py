# Crie um programa que receba 6 números, verifique se estes são pares, os some e apresente o resultado dessa soma.
s = 0
for i in range(0,6):
    n= int(input("Informe um número: "))
    if n % 2 == 0:  
        s += n
# print()
print(f'A soma dos pares entre os números digitados é {s}.')