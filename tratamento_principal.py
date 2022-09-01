from copy import copy
from historico import historico
import Estoque
from produto import Produto
from item import Item
import copy
import Menu_pesquisa


class principal:
    def __init__(self):
        #inicalização
        self.lista_compra = []
    def iniciar(self,janela,evento,valores,colunas):
        #definicoes dos atributos
        self.window = janela
        self.evento = evento
        self.valores = valores
        self.estoque = Estoque.Estoque()
        self.elemento_lista_pesquisa = self.window.Element('-LISTA_PESQUISA-')
        self.elemento_lista_compras = self.window.Element('-LISTA_COMPRA-')
        self.colunas = colunas
        self.tem_separador = "*" in self.valores['pesquisa']
        self.valor = 0
        self.tratar()
    def tratar(self):
        #Tratamentos dos eventos
        todos_eventos = {
            'pesquisa':self.pesquisa,
            '-LISTA_PESQUISA-': self.adcionar_a_compra,
            'Deletar':self.deletar,
            'Limpa':self.limpar,
            'Vender':self.vender,
            'Cancelar::lista_compra_rig_click_menu':self.limpar_selecao_lista_compra,
            'Apagar::lista_compra_rig_click_menu':self.deletar,
        }
        print(self.evento,self.valores)
        if self.evento in todos_eventos:
            todos_eventos[self.evento]()
    def limpar_selecao_lista_compra(self):
        self.elemento_lista_compras.update(select_rows=[])

    def pesquisa(self):
        #Acoes referente a barra de pesquisa

        if self.tem_separador:
            self.preencher_lista_pesquisa(nome = self.valores['pesquisa'][self.valores['pesquisa'].index('*')+1:].strip())
            #numero=self.validar_numero(self.valores['pesquisa'][:self.valores['pesquisa'].index('*')])

        else:
            self.preencher_lista_pesquisa(nome = self.valores['pesquisa'])

    def preencher_lista_pesquisa(self,nome=None,id=0):

        if (not bool(nome)) and (not bool(id)):
            self.elemento_lista_pesquisa.update(self.produto_linha(self.estoque.consulta_todos_produtos()))
        if nome:
            res1 = self.estoque.consulta_nome(nome)
            res2 = self.produto_linha(res1)
            self.elemento_lista_pesquisa.update(res2)
            
        
    def adcionar_a_compra(self):
        if self.valores['-LISTA_PESQUISA-']:
            self.preencher_lista_compra()

    def preencher_lista_compra(self):
        indice_do_produto_escolhido = self.valores['-LISTA_PESQUISA-'][0]
        produto_escolhido = self.elemento_lista_pesquisa.get()[indice_do_produto_escolhido]
        print(produto_escolhido)
        unidades_pdt = self.definir_unidades_do_produto() #recolher as unidades da barra de pesquisa se especificadas
        item = Item(produto_escolhido[1],unidades_pdt)
        item_para_lista_compra = [item.produto.id, item.unidades, item.quantidade, item, item.valor_total]
        self.lista_compra.append(item_para_lista_compra)
        self.elemento_lista_compras.update(self.lista_compra)
        self.atualizar_total()
        self.preencher_lista_pesquisa()
    def definir_unidades_do_produto(self):
        if self.tem_separador:
            possivel_numero = self.validar_numero_int(self.valores['pesquisa'][:self.valores['pesquisa'].index('*')])
            if possivel_numero:
                return possivel_numero
            else:
                return 1
        else:
            return 1
    def nao_esta_na_lista_compra(self,produto):
        nao_esta2 = True
        for row in self.lista_compra: 
            if produto[0] in row:
                nao_esta2 = False
        return nao_esta2

    def produto_linha(self,lista_produtos,colunas=None):
        if not colunas:
            colunas = self.colunas
        lista_produtos_linha = []
        for row in lista_produtos:
            produto_linha = []
            itens_colunas = {
                   'id':row.id,
                   'nome':row,
                   'valor_venda':row.valor_venda,
                   'quantidade':row.quantidade,
                   'genero':row.genero,
                   'categoria':row.categoria,
                   'cod':row.cod,
                   'valor_compra':row.valor_compra
            }
            for coluna in colunas:
                produto_linha.append(itens_colunas[coluna])
            lista_produtos_linha.append(produto_linha)
        return lista_produtos_linha
    def deletar(self):
        self.deletar_item_da_compra()
    def deletar_item_da_compra(self):
        itens_deletados = self.valores['-LISTA_COMPRA-']
        for row in itens_deletados:
            self.lista_compra.pop(row)
        self.elemento_lista_compras.update(self.lista_compra)
        self.atualizar_total()
    def limpar(self):
        self.lista_compra = []
        self.elemento_lista_compras.update(self.lista_compra)
        self.atualizar_total()
        self.window.Element('pesquisa').update('',select=False)
        self.preencher_lista_pesquisa()
    def vender(self):
        if self.lista_compra:
            self.vender_itens()
    def vender_itens(self):
        str_lista_compra = copy.deepcopy(self.lista_compra)
        self.atualizar_total()
        historico().add_venda(str_lista_compra,self.valor)

        for item in self.lista_compra:
            self.estoque.mudar_quantidade_venda(item[0],item[1])
        self.limpar()
    def validar_numero_int(self,str_numero):
        try:
            numero= int(str_numero)
            return numero
        except:
            pass
    
    def atualizar_total(self):
        self.valor = 0
        for row in self.lista_compra:
            self.valor += row[3].valor_total
        self.window.Element('total').update(self.valor)


































































