# Desafio 97 - Escreva uma função que receba um texto e mostra a mensagem com tamanho adaptável

texto =input("Digite um texto ou palavra: ")

def escreva(texto):  
    return texto +"\n" +"_"*len(texto)

texto_sublinhado = escreva(texto)
print(texto_sublinhado)

