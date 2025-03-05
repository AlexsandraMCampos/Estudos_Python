# Crie um programa que leio o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.


from datetime import datetime

anos = []
ano_atual = datetime.now().year
maior = 0
menor = 0
for i in range(3):
    ano = int(input("Informe seu ano de nascimento: "))
    anos.append(ano)
print("\nLista de anos informado: ",anos)
for j in anos:
    idade = ano_atual - j
    if idade >=18:
        maior +=1
        print(f'Ano de nascimento {j}: Maior de idade ({idade} anos).')
       
    else:
        menor +=1
        print(f'Ano de nascimento {j}: Menor de idade ({idade} anos).')
print(f'{maior} pessoas são maiores.')        
print(f'{menor} pessoas são menores.')


   


