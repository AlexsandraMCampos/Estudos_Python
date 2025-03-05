# Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos.

pesos = []

for i in range(5):
    p = float(input(f"Informe seu peso:  "))
    pesos.append(p)
print(f'A lista dos pessoas é :{pesos}') 

maior_peso = max(pesos)
menor_peso = min(pesos)
print(f'O maior peso é {maior_peso}Kg e o menor {menor_peso}kg.')

