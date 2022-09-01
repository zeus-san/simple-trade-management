from produto import Produto



class Item:#item referentea= a lista de compra
    def __init__(self,produto,unidades = 1):
        self.produto = produto
        self.unidades = unidades # unidades do produto
        self.fracionado()
        self.valor_total = self.calcular_valor()
    def fracionado(self):
        if self.produto.categoria == 'Frios':
            self.quantidade = self.produto.quantidade_vendida
        else:
            self.quantidade = 1
    def calcular_valor(self):
        print(self.produto.valor_venda)
        if self.produto.categoria == 'Frios':
            valor = self.quantidade * (self.produto.valor_venda/1000)
        else:
            valor = self.unidades * self.produto.valor_venda
        return valor
    def __str__(self):
        return self.produto.nome
    
            

    
    
    



# a = Produto(nome='Mortadela',valor_venda = 13,categoria='Frios')
# a1 = Produto(nome = 'Suco',valor_venda = 1)
# b = Item(a,quantidade_vendida = 385)
# b1 = Item(a1,unidades=3)
# print(b.calcular_valor())
# print(b1.calcular_valor())