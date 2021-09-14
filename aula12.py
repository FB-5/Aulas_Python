# Via CEP
# requisições http - raspagem de código
# Virtualenv - ambiente virtual . Create Project (no Pycharm) > New environment using . Virtualenv > Location . nomear projeto > Create > Nova Janela

import requests

def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    print(response.json())
    dados_cep = response.json()>
    print(dados_cep['logradouro'])
    print(dados_cep['complemento'])
    return dados_cep

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__' :
    response = retorna_response('https://globallabs.academy/')
    #retorna_dados_cep('01001000')
    #dados_pokemon = retorna_dados_pokemon('pikachu')
    #print(dados_pokemon['sprites']['front_shiny'])
    print(response)
