def soma(*valores): # desempacotamento
    s = 0 
    for n in valores:
        s += n
    print(f'Somando os valores {valores} temos o resultado {s}. ')    

soma(3,4,5)
soma(2,9,20)