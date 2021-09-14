# Lançar exceções genérica
# Exceções específicas
# Encadeamento de exceões
# Else e Finally
# Criando exceções customsadas

# try: except - tudo que estiver no 'try' entrará no tratamento de exceção
# ZeroDivisionError: é um builtin do Python
# IndexError:
# BaseException: - é o pai de todas a exceções


# Forçando erro

lista = [1, 10]
arquivo = open('test.txt', 'r')

try:
    texto = arquivo.read()
    divisao = 10/0
    numero = lista[1]
    print('fechando o arquivo')
    arquivo.close()

#except:
#    print('Erro desconhecido')
except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritimética')
except IndexError:
    print('Erro ao acessar um índice inválido la lista')
except Exception as ex:
    print('erro desconhacido. Erro: {}'.format(ex))
else:
    print('Executa quando não ocorre exceção')
finally:
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()
