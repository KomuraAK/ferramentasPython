from time import sleep
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
menu = False
while not menu:
    print('[1] Somar\n'
          '[2] Multiplicar\n'
          '[3] Maior\n'
          '[4] Novos números\n'
          '[5] Sair do programa')
    opção = int(input('Qual é a sua opção? '))
    if opção == 1:
        print(f'A soma entre {num1} + {num2} é {num1+num2}')
    elif opção == 2:
        print(f'O resultado de {num1} x {num2} é {num1*num2}')
    elif opção == 3:
        if num1 > num2:
            print(f'Entre {num1} e {num2} o maior valor é {num1}')
        else:
            print(f'Entre {num1} e {num2} o maior valor é {num2}  ')
    elif opção == 4:
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opção == 5:
        menu = True
    elif opção == 0 or opção > 6:
        print('Opção inválida. Tente novamente!')
    print('=-'*15)
    sleep(2)
