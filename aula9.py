#Gere, copie, mova, escreva e leia informações em arquivos externos.
# open - gera arquivo novo
# .write - escreve
# \n - espaço 'enter'
# .close - fecha o arquivo
# w - de write (escrita)
# a - atualizar
# r - read (leitura)

def escrever_arquivo(texto):
     diretorio = 'C:/Users/Pipo/PycharmProjets/app_python/test.txt'
     arquivo = open('diretorio', 'w')
     arquivo.write(texto)
     arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
     arquivo = open(nome_arquivo, 'a')
     arquivo.write(texto)
     arquivo.close()

def ler_arquivo():
     arquivo = open(nome_arquivo, 'r')
     texto = arquivo.read()
     print(texto)

def media_nota(nome_arquivo):
     arquivo = open(nome_arquivo, 'r')
     aluno_nota = arquivo.read()
     #print(aluno_nota)
     aluno_nota = aluno_nota.split('\n')
     #print(aluno_nota)
     lista_media = []
     for x in aluno_nota:
          lista_nota = x.split(',')
          aluno = lista_nota[0]
          print(aluno)
          print(lista_nota)
          media = lambda notas: sum{[int(i) for i in notas]} / 4
          print(media(lista_nota)
          lista_nota.append({aluno:madia(lista_nota)})
     return lista_media

if __name__ == '__main__':
     #escrever_arquivo('primeira linha.\n')
     aluno = '\nFelipe, 10, 10, 5, 5'
     atualizar_arquivo('notas.txt', aluno)
     #ler_arquivo('teste.txt')