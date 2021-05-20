#() = Tupla - TUPLAS SÃO IMUTÁVEIS!
#[] = Lista
#{} = Dicionário

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[3]) #Mostre dos lanches o número 3 = pudim
print(lanche[1:3]) #Mostre dos lanches o Suco e Pudim
print(lanche[1:]) #Mostre dos lanches Suco até Pudim

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi para caramba')

for cont in range(0, len(lanche)):
    print(lanche[cont])

#Concatenar tuplas
a= (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a #Concatenar
print(c)