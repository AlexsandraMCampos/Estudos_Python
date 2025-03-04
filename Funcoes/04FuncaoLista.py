
valores =[7,2,5,0,4]    
novos_valores = [2,4,6,8,10]

def dobra_valores(lst):
    pos = 0 # declarei a variavel para a lista que irá receber os valores dobrados
    while pos < len(lst): # enquanto a lista por for menor que o tamanho da lista
        lst[pos]*= 2 #multiplico cada valor por 2
        pos += 1 # vou par o próximo elemento
   
dobra_valores(valores) # chamei a função com o parâmetro(lista que irá receber)
print(valores) #pedi para mostrar a lista depois de receber a função

dobra_valores(novos_valores)# chamei a função com o parâmetro(lista que irá receber)
print(novos_valores) #pedi para mostrar a lista depois de receber a função
