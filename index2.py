import json
def ler_dados():
    with open("teste.json") as file:
        data = json.load(file)
        return data


def gravar_dados(data):
    with open("teste.json",'w') as file:
        json.dump(data,file,indent=3)

a = ler_dados()
print(a)

a["nome"] = "Aranha"
a["moradia_propia"] = False

gravar_dados(a)

b = ler_dados()
print(b)

