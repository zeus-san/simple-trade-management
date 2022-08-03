import json
class config:
    def ler_dados():
        with open("config.json") as file:
            data = json.load(file)
            return data

    def gravar_dados(data):
        with open("config.json",'w') as file:
            json.dump(data,file,indent=3)

COLUNAS = config.ler_dados()['campos']

CATEGORIAS = ["Alimento","Limpeza","Frios","Bebidas","Cigarro"]

DICIONARIO = {
       'id':'Id',
       'nome':'Nome',
       'valor_venda':'Valor de Venda',
       'quantidade':'Quantidade',
       'genero':'Genero',
       'categoria':'Categoria',
       'cod':'Codig Barra',
       'valor_compra':'Valor de Custo'
}
