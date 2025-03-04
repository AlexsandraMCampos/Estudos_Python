def soma(a,b):
    s = a + b
    print(f'A soma de {a} + {b} = {s}.')


# Programa principal, recebe os parâmetros de a e b.
soma(5,6) # se eu não identifico o parâmetro o programa entende que o primeiro é o a e o segundo é o b.
soma(b=7, a=9) # se eu informo quem é quem ele realiza a função
# soma(4) ou soma(4,5,6) seu eu dou parametros de mais ou de menos o código também identifica erro e não funciona