from tratamento_cadastrar import cadastrar
from produto import Produto
import Estoque
import Menu_pesquisa
class atualizar(cadastrar):
    def __init__(self):
        self.produto = None
        self.estoque = Estoque.Estoque()
        cadastrar.__init__(self)
        self.pesquisado = False
        
    def mais_tratamentos(self):
        if self.event == 'pesquisar':
            self.pesquisar()
            self.pesquisar_produto_no_estoque()
            self.atualizar_elementos()
        elif self.event == 'atualizar':
            self.event_atualizar()


    def pesquisar(self):
        res = Menu_pesquisa.pesquisa()
        if res:
            self.window.Element('identi').update(res)

    def pesquisar_produto_no_estoque(self):
        id_produto = self.window.Element('identi').get()
        consulta_produto = self.estoque.consulta_id(int(id_produto))
        self.produto = consulta_produto
        #self.atualizar_elementos()

    def atualizar_elementos(self):
        dados = self.produto.dadosfront()

        for row in ['genero','categoria']:
            elementos_janela = self.window.find_element(row).Values
            if dados[row] in elementos_janela:
                index_genero_produto = elementos_janela.index(dados[row])
                self.window.Element(row).update(set_to_index=index_genero_produto)

        for row in ['nome','valor_venda','quantidade','valor_compra','cod']:
            self.window.Element(row).update(dados[row])

    def event_atualizar(self):
        if self.validacoes() and self.values['identi']:
            self.atualizar_produto_no_estoque()
        else:
            pass
        
    def atualizar_produto_no_estoque(self):
        args = self.values
        args['id'] = args.pop('identi')
        args['valor_venda'] = float(args['valor_venda'].replace(',','.'))
        args['quantidade'] = float(args['quantidade'])
        args['valor_compra'] = float(args['valor_compra'].replace(',','.'))
        
        produto = Produto(**args)
        self.estoque.atualizar_produto(produto)
        self.rodando = False


    