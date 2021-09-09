# ESTRUTURAS DE REPETIÇÃO (laços)
# for - vai repetir uma ação de acordo com o que o usuário informar.
# while - cria um loop (?); repetição até conseguir o resultado.
# range - retorna um conjunto de números sequenciais.
# += - concatena agregando 1.

#EX:4 WHILE
a = int(input('Primeiro bimestre: '))
while a > 10:
    a = int(input('Você digito errado. Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
while b > 10:
    b = int(input('Você digito errado. Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
while c > 10:
    c = int(input('Você digito errado. Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
while d > 10:
    d = int(input('Você digito errado. Quarto bimestre: '))
media = (a + b + c + d) / 4
print('media: {}'.format(media))



# nota = int(input('Entra com a nota: '))
# while nota > 10:
#     nota = int(input('Nota invalida. Entre com a nota correta: '))

# a = 0
# while a <= 10:
#     print(a)
#     a += 1



EX:3 FOR
for num in range(101):
    div = 0
    for x in range(1, num+1):
        resto = num % x
       # print(x, resto)
        if resto == 0:
            div += 1

    if div == 2:
        print(num)


EX:2 números primos
a = int(input('Entre com o número: '))

div = 0
for x in range(1, a+1):
    resto = a % x
    print(a, resto)
    if resto == 0:
        #div = div +
        div += 1

# if div == 2:
#     print('O número {} é primo'.format(a))
# else:
#     print('Número {} não é primo'.format(a))


EX:1  sequência de 0 a 100
for x in range(101):
    print(x)