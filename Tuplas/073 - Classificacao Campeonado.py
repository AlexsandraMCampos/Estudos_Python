# Crie uma tupla preenchida com os 10 primeiros colocados da Tabela de um Campeonato qualquer,
#  na ordem de colocação. Depois mostre:
#  a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em qual time está em 7ºlugar.


times= ('Palmeiras','Atletico','São Paulo','Corinthians','Curitiba','Bota Fogo',
'Chapecoense','15 de Piracicaba','Bola Branca','Barra Funda')

print("_"*30)
print(f"Os 5 primeiros times são:{times[0:5]}.") # apresentar os 5 primeiros times
print(f"Os 4 últimos times colocados são:{times[-4:]}.") #  apresentar do -4 até o final
print(f'Times em ordem alfabetica: {sorted(times)}') # apresentar o resultado em ordem alfabética, 
# não altera a tupla apenas apresenta a ordem alfabetica
print(f'O Chapecoense está na {times.index("Chapecoense")+1}º posição.') # posição na qual o Chapeoense se encontra. 
#Obs: adicionamos +1 por que o índice no python começa do zero
print("_"*30)