# Exercício Python 72: Crie um programa que tenha uma dupla totalmente 
# preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.


cont = ('zero','um','dois','três','quatro','cinco','seis','sete','oito',
'nove','dez','onze', 'doze','treze','quatorze', 'quinze', 'dezesseis', 
'dezessete','dezoito', 'dezenove', 'vinte')

while True:  # Loop externo para repetir o programa
    while True:  # Loop para validar a entrada do número
        num = int(input("Escreva um número entre 0 e 20: "))
        if 0 <= num <= 20:
            break
        print("Tente novamente.", end=' ')
    
    print(f'Você digitou o número {cont[num]}.')

    # Perguntar ao usuário se deseja continuar
    while True:
        resposta = input("Deseja continuar? [S/N]: ").strip().lower()
        if resposta in ('s', 'n'):
            break
        print("Resposta inválida! Digite 'S' para sim ou 'N' para não.")

    if resposta == 'n':  # Se o usuário disser "não", sair do loop externo
        print("Encerrando o programa. Até mais!")
        break

    



    