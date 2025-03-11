# Faça um programa que tenha um função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

# Etapas:
# - receber vários números
# - armazenar esses números
# - checar o maior número entre os números armazenados
# - checar o tamanho da lista dos números recebidos
# - apresentar o valor do maior número
# - apresentar a quantidade de números recebidos

def maior(*numeros):
    if not numeros:
        print("Nenhum número foi informado.") # caso não seja informado número
        return

    maior_numero = max(numeros) # obter o maior número da sequência
    qtd = len(numeros) # obter quantos números foram informados

    print(f"Foram informados {qtd} números: {numeros}.")
    print(f" O maior número é {maior_numero}.")

#Solicitar os números ao usuário
lista_numeros =[]

while True:
        n =input("Digite um número inteiro ou 'sair' para finalizar: ") 
        if n.lower() == 'sair': # condição para o programa ser finalizado
            break
        try:
            lista_numeros.append(int(n)) # checagem se o número é inteiro e adicionar na lista
        except ValueError:
            print("Por favor, digite um número válido.") # informação caso o usuário informe um valor errado

maior(*lista_numeros)
