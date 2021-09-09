# CONJUMTOS (União/Intersecção/Diferença/Diferença Simétrica/Remoção de duplicidades de listas)
# .add() - adiciona.
# .union() - une dois conjuntos.
# .intersection() - intersecção.
# .difference() - exclui o que tem em um e não tem no outro.
# {} .format() - imprime.
# .symmetric_difference() - exclui apenas o que há entre os dois conjs.
# pertinência : .issuperset() = superconjunto, .issubset() = subconjunto.
# list - converte para lista.
# set - convert para conjunto.

EX:2

conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2)
print(conjunto_uniao)
conjunto_interseccao = conjunto.intersection(conjunto2)
print(conjunto_interseccao)
conjunto_diferenca1 = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca1))
print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca2))
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença simétrica: {}'.format(conjunto_diff_simetrica))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_b.issubset(conjunto_a)
print ('A é um subconjunto de b: {}'.format(conjunto_subset))
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é um superconjunto de A: {}'.format(conjunto_superset))

lista = ['cachorro' 'cachorro', 'gato', 'gato', 'elefante']
print(lista)
conjunto_animais = set(lista) #converte lista/conjunto
print(conjunto-animais)
lista_animais = list(conjunto_animais) #converte conjunto/lista
print(lista_animais)

EX:1

conjunto = {1, 2, 3, 4, 4, 2}
conjunto.add(5)
conjunto.discard(2)
print(conjunto)