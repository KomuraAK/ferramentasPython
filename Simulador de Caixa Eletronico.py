lista = [100, 50, 20, 10, 5, 2, 1]
valor = int(input('Insira o valor que desaja sacar R$ '))
cont = 0
while True:
    if valor >= lista[cont]:
        nota = valor // lista[cont]
        print(f'Total de {nota} notas de R$ {lista[cont]}')
        valor = valor % lista[cont]
    cont += 1
    if valor == 0:
        break
print('\nVolte sempre ao Banco do Cev! Tenha um bom dia!')