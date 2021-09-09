# listas - (list) em Python é uma sequência ou coleção ordenada de valores.
# tuplas - funciona de modo semelhante a uma lista, imutável; não é possível adicionar, alterar ou remover seus elementos.
# na TUPLA ao invés de chaves, usa parênteses.
# tuple -
# len - informa quantos elementos tem na lista.
# sum - somatória de mesmo tipo
# max - maior valor da lista.
# min - menor valor da lista.
#.append () - acrescenta a uma lista.
#.pop () - sem parametro retira o ultimo da lista; com, retira da posição informada.
# .sort() - ordena a lista

EX:2 TUPLAS

lista = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante']

lista_animal[0]='macaco'
print(lista_animal)

tupla = (1, 10, 12, 14)
print(tupla)
print(len(tupla))
print(len(lista_animal))
tupla_animal = tuple(lista_animal) # converter a lista n tupla
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
print(type(lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)

EX:1 LISTAS

lista = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante']
#print(lista_animal[1])

lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal)

soma = 0
for x in lista:
    print(x)
    soma += x
print(soma)

print (sum(lista))
print (max(lista))
print (min(lista))
#print (min(lista_animal))

nova_lista = lista_animal * 3
print(nova_lista)

if 'lobo' in lista_animal:
    print('existe um lobo na lista')
else:
    print('não existe um lobo na lista')
    lista_animal.append('lobo')
    print(lista_animal)

#lista_animal.pop(1)
#print(lista_animal)

lista_animal.remove('elefante')
print(lista_animal)


