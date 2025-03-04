i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)
print('Código apresenta o caminho do laço.')

# Resultado: Digitando i =1, f=11, p= 2, o resultado será 1,3,5,7,9,11