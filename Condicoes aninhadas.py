#Estrutura condicional aninhada
nome = str(input('Qual seu nome? '))

if nome == 'Anthony' or 'anthony':
   print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem comum no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
  print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))