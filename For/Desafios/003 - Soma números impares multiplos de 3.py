# Crie um programa que some todos os números ímpares que são multiplos de 3 de 1 a 500 e apresente o resultado.

multiplo_tres = 0 # variavel que irá receber os números ímpares e multiplos de 3

for i in range(1,31,2): #contagem dos números ímpares
    if i % 3 == 0: #checagem se os números são multiplos de 3
        print(i, end=', ') # apresentação dos números que atendem os requisitos (na mesma linha e com vírgulas separandos os números)
        multiplo_tres += i  # soma dos números que atendem os requisitos
print()    #para pular uma linha entre os números e o print
print(f"A soma dos números ímpares multiplos de 3 neste intervalo é {multiplo_tres}.")