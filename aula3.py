# OPERADORES:
# if -  para verificar uma expressão e executar um bloco de código caso a condição definida seja verdadeira.
# else - que seria o senão; quer dizer que vamos primeiramente testar a informação do IF e se ela não for verdadeira nós vamos para essa opção.
# elif - que seria basicamente a junção de um ELSE + IF.
# and - E lógico.
# or - OU lógico.
# not - Negação.
# No python o fim de um bloco e a identação.

EX:5
a = int(input('Primeiro bimestre: '))
if a > 10:
    a = int(input('Você digito errado. Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
if b > 10:
    b = int(input('Você digito errado. Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
if c > 10:
    c = int(input('Você digito errado. Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
if d > 10:
    d = int(input('Você digito errado. Quarto bimestre: '))
media = (a + b + c + d) / 4
print('media: {}'.format(media))


EX:4
a = int(input('Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))

media = (a + b + c + d) / 4
if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('media: {}'.format(media))
else:
    print('foi informada alguma nota errada.')

EX:3
a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
resto_a = a % 2
resto_b = a % 2
if resto_a == 0 or resto_b == 0:
    print('foi digitado número par')
else:
    print('nenhum número par foi digitado')


EX:2
a = int(input('Entre com o valor: '))
b = int(input('Entre com o valor: '))
resto = a % 2
if resto == 0:
    print('Número é par')
else:
    print('Número é impar')


EX:1
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

if a > b and a > c:
    print('o maior número é {}'.format(a))
#else:
#    print('o maior número é {}'.format(b))
elif b > a and b > c:
    print('o maior número é {}'.format(b))
else:
    print('o maior número é {}'.format(c))

print('Final do programa.')