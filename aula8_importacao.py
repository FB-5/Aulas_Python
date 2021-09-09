#Módulo,importação de classes, métodos e construção de funçoes anônimas (lambda)

from aula7_televisao import Televisao
from aula7_calculadora1 import Calculadora
from aula8_contado_letras import contador_letras

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora(5, 10)
    print(calculadora.soma())
    lista = ['cachorro', 'gato', 'elefante']
    print(contador_letras(lista))
    print('total de letras por palavra de lista: ()'.format(total_letras))
    print(test())