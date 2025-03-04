# Desenvolva um programa que leia o primeiro termo e a razão de uma P.A. 
# No final, mostre os 10 primeiros termos dessa progressão.

lst = [26, 31, 36, 41]

a1 = 0
an= 0
r= 0
termo = 0
an = int(input('Informe o termo que você quer identificar: '))

for i in lst:   
    a1 = lst[0]
    r = lst[1] -lst[0]
    termo = (a1 +(an -1)*r) 
print(f'A razão dessa função é {r}.')
print(f'O primeiro termo dessa função é {a1}.')
print(f'E o {an}º termo dessa função é {termo}.')
    