print('-' * 30)
print("Maior número\n")
print('-' * 30)

pnum = float(input('Primeiro número: '))
snum = float(input('Segundo número: '))

if (pnum > snum):
    print('O PRIMEIRO número é maior')
elif (pnum < snum):
    print('O SEGUNDO número é maior')
elif (pnum == snum):
    print('AMBOS os números são IGUAIS')
