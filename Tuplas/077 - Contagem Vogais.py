# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).. 
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ("amor", "amora", "paz", "confiança","amizade", "esperança","determinação") # tupla de palavras

for p in palavras: # percorro toda a tupla
    print(f'\nNa palavra {p.upper()} temos as seguintes vogais', end=" ") # apresento a frase com a palavra da tupla em letra maiuscula
    for letra in p:
        if letra.lower() in "aáâãeéêeiíoóôõuú": #verifico se a palavra tem vogais
            print(letra, end= " ")

