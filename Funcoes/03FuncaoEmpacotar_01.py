def contador(*num): # (*num) isso vai desempacotar os parâmetros informados e adicionar em num
    tam =len(num)
    print(f'Recebi os valor {num} e são ao todo {tam} números.')


contador(5,7,6,3,14) # criará as tuplas com os elementos informados em cada contador
contador(2,3,4,8)
contador(1,8)