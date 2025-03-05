# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
# a média de idade do grupo
# qual o nome do homem mais velho
# quantas mulheres tem menos de 20 anos.abs

pessoas = [] # cria uma lista vazia que receberá os dicionários de cada pessoa

for i in range(4):
    pessoa = {} # dicionário de pessoas
    pessoa["nome"] = input("Qual seu nome: ")
    pessoa["idade"] = int(input("Informe sua idade: ")) 
    pessoa["sexo"] = input("Informe seu sexo (F) ou (M): ").upper()
    pessoas.append(pessoa) # inclusão dos dicionários na lista pessoas

print(pessoas)

# Cálculo da média do grupo
total_idade = sum(pessoa['idade'] for pessoa in pessoas) 
media_idade = total_idade/4

# Checagem do homem mais velho
homens = [pessoa for pessoa in pessoas if pessoa['sexo'] == "M"]
homem_mais_velho = max(homens, key=lambda p:p['idade'], default={"nome":"nenhum"})

#Checaagem das mulheres menores de 20 anos

mulher_menor_20 = sum(1 for pessoa in pessoas if pessoa["sexo"] == "F" and pessoa["idade"] <20)

# Apresentação dos resultados
print(f'A média da idade do grupo é {media_idade} anos.')
print(f'O homem mais velho tem {homem_mais_velho} anos. ')
print(f'A quantidade de mulheres com menos de 20 anos é {mulher_menor_20}.')





