class Produto:
    def __init__(self,id=0,nome='None',valor_venda=0,quantidade=0,genero='None',categoria='None',cod='None',valor_compra=0):
        self.nome = nome
        self.valor_venda = valor_venda
        self.quantidade = quantidade
        self.genero = genero
        self.categoria = categoria
        self.cod = cod
        self.valor_compra = valor_compra
        self.id = id
    def validar(self):
        pass
    def dadosfront(self) -> str:
        return {
                'id':self.id,
                'nome':self.nome,
                'valor_venda':self.valor_venda,
                'quantidade':self.quantidade,
                'genero':self.genero,
                'categoria':self.categoria,
                'cod':self.cod,
                'valor_compra':self.valor_compra
                }
    def dadosback(self) -> str:
        return {'id':self.id,
                'nome':self.nome,
                'valor_venda':self.valor_venda * 100,
                'quantidade':self.quantidade ,
                'genero':self.genero,
                'categoria':self.categoria,
                'cod':self.cod,
                'valor_compra':self.valor_compra * 100
                }
    def preencher_dados(self,dados):
        self.id = dados[0]
        self.nome = dados[1]
        self.valor_venda = dados[2] / 100
        self.quantidade = dados[3]
        self.genero = dados[4]
        self.categoria = dados[5]
        self.cod = dados[6]
        self.valor_compra = dados[7] / 100
    def __str__(self) -> str:
        return self.nome
    