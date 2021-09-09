# aula 2 (variáveis, manipulação de variáveis, conversão, poradores aritiméticos,strings, interação com usuário).
# str - string
# int - inteiro
# %   - quisermos exibir só o resto da divisão
# \n  - espaço com um ENTER; para quebra de linhas.
# type() - Para saber o tipo de um objeto ou variável.

#.format - o método format() em python serve basicamente para criar uma string que contém campos entre chaves que
# são substituidos pelos argumentos de format. Portanto, repare que os campos de substituição na string que estão
# entre chaves '{}' estão associadas aos parâmetros do método format(). ex: print('Soma: {} '.format(soma))

# input - Esta função lê a entrada que o usuário digitou e armazena o valor em uma variável.

# a = 10
# b = 6
a = int(input('Entre com o primeiro  valor: '))
b = int(input('Entre com o segundo valor: '))
print(type(a)) # mostra o tipo
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

# print('Soma: {} '.format(soma)) # melhor forma de fazer o primt
# print('Soma: ' + str(soma))
# print(subtracao)
# print(multiplicacao)
# print(int(divisao)) # para arredondar usa-se o int.
# print(resto)

# Melhor forma de representar o acima

resultado = ('Soma: {soma}. \nSubtraçãoo: {subtracao}. '
      '\nMultiplicação: {multiplicacao}. '
      '\nDivisão: {divisao}.'
      '\nResto: {resto}'.format(soma=soma,
                                subtracao=subtracao,
                                multiplicacao=multiplicacao,
                                divisao=divisao,
                                resto=resto))

print(resultado)


# x = '1'
# soma2 = int(x) + 1
# print(soma2)