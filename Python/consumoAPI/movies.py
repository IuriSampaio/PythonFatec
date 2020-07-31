import requests
import json

titulo = input("Digite o nome de um filme: ")

filme = requests.get(f'http://www.omdbapi.com/?t={titulo}&apikey=87ade605')

filmeJSON = json.loads(filme.text)

if filmeJSON['Response'] != 'False' :
    print(
        f'\n===={filmeJSON["Title"]}====\n\nLacado em: {filmeJSON["Released"]} \nTempo de filme: {filmeJSON["Runtime"]} \nGenero: {filmeJSON["Genre"]} \nDiretor: {filmeJSON["Director"]}\nAtores: {filmeJSON["Actors"]}\nEscritor: {filmeJSON["Writer"]}\nSinopse: {filmeJSON["Plot"]}')
else:
    print("ESSE FILME NÂO EXISTE")
