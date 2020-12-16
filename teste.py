import json
with open("models/respostas.json", "r") as p:
    palavra = json.load(p)

preco = 1200
print(palavra['Etapa2'].format('tv',preco))