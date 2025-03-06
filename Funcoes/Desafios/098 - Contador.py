print("Contagem de 1 até 10 de um em um: ") 
def cont(inicio,fim):
    for i in range(inicio,fim +1):      
        print(i, end=" ") 
    return list(range(inicio,fim +1))
resultado = cont(1,10)

print("\nContagem de 10 até 0 de 2 em 2: ") 

def cont1(inicio, fim,passo):
    for j in range(inicio, fim -1, passo):      
        print(j, end=" ") 
    return list(range(inicio, fim -1, passo))
resultado1 = cont1(10,0,-2)

print("\nSua vez de personalizar a contagem!") 

def cont2():
    e = int(input("Informe a entrada:"))
    s = int(input("Informe a saída:"))
    p = int(input("Informe o passo:"))

    if e > s and p >0 :
        p = -p
    for z in range(e,s,p):      
        print(z, end=" ") 
    return list(range(e,s,p))
resultado2 = cont2()

