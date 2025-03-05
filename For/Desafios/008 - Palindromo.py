
# Crie um programa que leia uma frase ou palavra qualquer e verifique se ela é um palíndromo, desconsidere os espaços.
# Exemplos de palindromo: apos a sopa, a sacada da casa, a torre da derrrota, o olobo ama o bolo, 
frase = input("Digite uma palavra ou uma frase: ")

def palindromo(frase):
    try:
        # Remove espaços e converte para minúsculas para comparação consistente
        frase_limpa = frase.replace(" ", "").lower() 
        
        # Inverte a frase usando slice reverso
        inverso = frase_limpa[::-1]
        
        # Compara a frase original com sua versão invertida
        if inverso == frase_limpa:
            print(f'A "{frase}" é um palíndromo.')
        else:
            print(f'A "{frase}" não é um palíndromo.')
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
 
# Solicitar entrada do usuário

palindromo(frase)



       