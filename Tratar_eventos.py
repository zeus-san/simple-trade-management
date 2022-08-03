from copy import copy
from historico import historico
import Estoque
from produto import Produto
import copy
class principal:
    def __init__(self):
        self.lista_compra = []
    def iniciar(self,janela,evento,valores,colunas):
        self.window = janela
        self.evento = evento
        self.valores = valores
        self.estoque = Estoque.Estoque()
        self.elemento_lista_pesquisa = self.window.Element('-LISTA_PESQUISA-')
        self.elemento_lista_compras = self.window.Element('-LISTA_COMPRA-')
        self.colunas = colunas
        self.tem_separador = "*" in self.valores['pesquisa']
        self.tratar()
    def tratar(self):
        todos_eventos = {
            'pesquisa':self.pesquisa,
            '-LISTA_PESQUISA-': self.adcionar_a_compra,
            'Deletar':self.deletar,
            'Limpa':self.limpar,
            'Vender':self.vender
        }
     
        if self.evento in todos_eventos:
            todos_eventos[self.evento]()

    def pesquisa(self):
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
        if self.nao_esta_na_lista_compra(produto_escolhido):
            produto_escolhido[3] = 0
            produto_escolhido[3] = self.definir_quantidade_do_produto()
            self.lista_compra.append(produto_escolhido)
            self.elemento_lista_compras.update(self.lista_compra)
            self.preencher_lista_pesquisa()
    def definir_quantidade_do_produto(self):
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
        self.lista_compra
        itens_deletados = self.valores['-LISTA_COMPRA-']
        # for row in itens_deletados:
        #     for p,row2 in enumerate(self.lista_compra):
        #         if row2[0] == row[0]:
        #             self.lista_compra.pop(p)
        for row in itens_deletados:
            self.lista_compra.pop(row)
        self.elemento_lista_compras.update(self.lista_compra)
    def limpar(self):
        self.lista_compra = []
        self.elemento_lista_compras.update(self.lista_compra)
        self.window.Element('pesquisa').update('',select=False)
        self.preencher_lista_pesquisa()
    def vender(self):
        self.vender_itens()
    def vender_itens(self):
        str_lista_compra = copy.deepcopy(self.lista_compra)
        historico().add_venda(str_lista_compra)

        for item in self.lista_compra:
            self.estoque.mudar_quantidade_venda(item[1],item[3])
        self.limpar()
    def validar_numero_int(self,str_numero):
        try:
            numero= int(str_numero)
            return numero
        except:
            pass
        
class cadastrar:
    def iniciar(self,window,event,values):
        self.window = window
        self.event = event
        self.values = values
        self.validacao = 'Pendente'
        self.tratar()
    def tratar(self):
        if self.event == "Cadastrar":

            self.validacoes()

            if self.validacao == "Aprovado":
                
                self.cadastrar_produto()

    def validacoes(self):
        entradas_valida = True
        quantidade_valida = False
        valor_valido = False
        valor_compra_valido = False
      
        self.validacao = ''
        if not bool(self.values['nome']):
            self.validacao += "Nome Invalido: nome nao pode estar vazio\n"
            entradas_valida = False
        if self.values['nome'].isdigit():
            self.validacao += "Nome Invalido: nome nao pode ser composto so de numeros\n"
            entradas_valida = False
        if not bool(self.values['valor_venda']):
            self.validacao += "Valor Invalido: o valor nao pode estar vazio\n"
            entradas_valida = False
        try:
            valor_aux = self.values['valor_venda'].replace(',','.')
            float(valor_aux)
            valor_aux = float(valor_aux)
            valor_valido = True
        except:
            self.validacao += "Valor Invalido: insira um valor valido\n"
            entradas_valida = False
        
        if valor_aux < 0 and valor_valido:
            self.validacao += "Valor Invalido: valor não pode ser negativo\n"
            entradas_valida = False
        
        try:
            quantida_aux = self.values['quantidade']
            float(quantida_aux)
            quantida_aux = float(quantida_aux)
            quantidade_valida = True
        except:
            self.validacao += "Quantidade Invalida: insira uma quantidade valida\n"
            entradas_valida = False

        if quantida_aux < 0 and quantidade_valida:
            self.validacao += "Quantidade Invalida: Quantidade não pode ser negativa\n"
            entradas_valida = False


        if quantida_aux%1 != 0 and quantidade_valida and quantida_aux != 0:
            self.validacao += "Quantidade Invalida: Quantidade é um numero inteiro"
            entradas_valida = False


        if not bool(self.values['valor_compra']):
            self.validacao += "Valor Compra Invalido: o valor nao pode estar vazio\n"
            entradas_valida = False
        try:
            valor_compra_aux = self.values['valor_compra'].replace(',','.')
            float(valor_compra_aux)
            valor_compra_aux = float(valor_compra_aux)
            valor_compra_valido = True
        except:
            self.validacao += "Valor Compra Invalido: insira um valor valido\n"
            entradas_valida = False
        
        if valor_compra_aux < 0 and valor_compra_valido:
            self.validacao += "Valor Compra Invalido: valor não pode ser negativo\n"
            entradas_valida = False

        if entradas_valida == True:
            self.validacao = "Aprovado"
    def cadastrar_produto(self):
        args = self.values
        args['valor_venda'] = float(args['valor_venda'].replace(',','.'))
        args['quantidade'] = float(args['quantidade'])
        args['valor_compra'] = float(args['valor_compra'].replace(',','.'))
        produto = Produto(**args)
        estoque = Estoque.Estoque()
        estoque.add_produto(produto)
        self.validacao += "\n Produto adcionado"
            
class atualizar(cadastrar):
    def __init__(self):
        self.produto = None
        cadastrar.__init__(self)
        self.validacao = ''
        self.pesquisado = False
    def iniciar(self,window,event,values):
        self.window = window
        self.event = event
        self.values = values
        self.estoque = Estoque.Estoque()
        self.tratar()
    def tratar(self):
     
        if self.event == "pesquisa":
            self.encontrar_produto()
        if self.event == 'Atualizar':
            self.atulizar_produto()
    def encontrar_produto(self):
        if not bool(self.values['identi']):
            self.validacao = "Digite um id"
        elif not self.values['identi'].isdigit():
            self.validacao = "id é um numero"
        else:
            self.pesquisar_produto_no_estoque()

    def pesquisar_produto_no_estoque(self):
        consulta_produto = self.estoque.consulta_id(int(self.values['identi']))
        if bool(consulta_produto):
            self.produto = consulta_produto
            self.validacao = "Produto encontrado"
            self.atualizar_elementos()
            self.pesquisado = True
        else:
            self.pesquisado = False
            self.validacao = "Produto nao encontrado"
    def atualizar_elementos(self):
        dados=self.produto.dadosfront()
     
        self.window.Element('nome').update(dados['nome'])

        elementos_genero = self.window.find_element('genero').Values
        if dados['genero'] in elementos_genero:
            index_genero_produto = elementos_genero.index(dados['genero'])
            self.window.Element('genero').update(set_to_index=index_genero_produto)

        elementos_categoria = self.window.find_element('categoria').Values
        if dados['categoria'] in elementos_categoria:
            index_categoria_produto = elementos_categoria.index(dados['categoria'])
            self.window.Element('categoria').update(set_to_index=index_categoria_produto)

        self.window.Element('valor_venda').update(dados['valor_venda'])

        self.window.Element('quantidade').update(dados['quantidade'])

        self.window.Element('valor_compra').update(dados['valor_compra'])

        self.window.Element('cod').update(dados['cod'])
    def atulizar_produto(self):
        if self.pesquisado:
            self.validacao_atualizacao_produto()
        else:
            self.validacao = "Pesquise um produto"
    def validacao_atualizacao_produto(self):
        self.validacoes()
        if self.validacao == "Aprovado":
            self.atualizar_produto_no_estoque()
    def atualizar_produto_no_estoque(self):
        args = self.values
        args['id'] = args.pop('identi')
        args['valor_venda'] = float(args['valor_venda'].replace(',','.'))
        args['quantidade'] = float(args['quantidade'])
        args['valor_compra'] = float(args['valor_compra'].replace(',','.'))
        produto = Produto(**args)
        self.estoque.atualizar_produto(produto)
        self.validacao += "\n Produto Atualizado"

































































