# Faça um programa que mostre a contagem regressiva para estouro de fogo de artifício 
# de 10 a 0 com pausa de 1 segundo entre a contagem.

import time
from time import sleep


for contagem in range(11,0,-1):
    time.sleep(1) # solicitando que o código faça a contagem de 1 em 1 segundo
    print(contagem)
print('Booooooooooommmmmmmmmmm !')