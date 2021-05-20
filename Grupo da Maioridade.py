from datetime import date
menor = 0
maior = 0
for pess in range(1, 8):
    anonasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = date.today().year - anonasc
    if idade < 18:
        menor = menor + 1
    else:
        maior = maior + 1
print('{} pessoas são de menor.'.format(menor))
print('{} pessoas são de maior.'.format(maior))