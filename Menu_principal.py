import PySimpleGUI as sg
import Estoque
from Menu_cadastro import Menu_cadastro
from Menu_config import Menu_config
from Menu_atualizar import Menu_atualizar
import Tratar_eventos
import config
class Menu_principal:
    def init(self):
        self.titulos = []
        self.titulos_compra = []
        self.lista_pesquisa = []
        self.lista_compra = []
        self.colunas = config.COLUNAS
        self.colunas_compra = ['id','nome','valor_venda','quantidade']
        self.estoque = Estoque.Estoque()
        self.produto_linha = Tratar_eventos.principal().produto_linha
        self.iniciar_lista_pesquisa()
        self.colunas_lista(self.colunas,self.titulos)
        self.colunas_lista(self.colunas_compra,self.titulos_compra)
        self.execucao_tela_principal()


    def layout_tela(self):
        #layout da tela
        colunaButtao = [
                    [sg.Button('Cadatrar\nProduto',size=(10,2),key='Casdastrar_pdt')],
                    [sg.Button('Excluir\nproduto',size=(10,2),key='Deletar_pdt')],
                    [sg.Button('Atualizar\nproduto',size=(10,2),key='Atualizar_pdt')]
                        ]
        colunaMeio = [
                [sg.Input(enable_events=True,key='pesquisa'),sg.Button('Atualizar',key='atualizar_list')],
                [sg.Table(self.lista_pesquisa,headings=self.titulos,key='-LISTA_PESQUISA-',size=(45,15),expand_x = True,enable_events=True)],#lista produtos
                [sg.Table([],headings=self.titulos_compra,size=(45,15),key='-LISTA_COMPRA-',expand_x = True,enable_events=True)],#lista compra
                [
                 sg.Button('Vender',focus=True),
                 sg.Text('',size=(20,1),key='AVISO'),
                 sg.Button('Deletar'),
                 sg.Text('',size=(20,1)),
                 sg.Button('Limpar', key='Limpa')
                 ]
                ]
        coluna_price = [
                [sg.Text("Total:",background_color=None)],
                [sg.Text()],
                [sg.Text()]
        
        
        
                ]
        
        layout = [
                [
                 sg.Column(colunaButtao),
                 sg.Column(colunaMeio,justification='center'),
                 sg.Column(coluna_price,background_color='#DCDCDC',size=(50,50))],
                [
                 sg.Button('OK',tooltip='Aperte aqui'), 
                 sg.Button("Fechar",key='Cancelar'),
                 sg.Button("Configurações",key='Configurar_pdt')]
                ]
        return layout
    def execucao_tela_principal(self):
        layout = self.layout_tela()
        
        # Aqui eu esntacio
        self.window = sg.Window('Titulo da Janela', layout,size=(900,750))
        # Loop de eventos para processar "eventos" e obter os "valores" das entradas
        tratador_de_eventos_principal = Tratar_eventos.principal()
        event = None
        butoes_especiais = {'Casdastrar_pdt':Menu_cadastro().iniciar,
                            'Atualizar_pdt':Menu_atualizar().iniciar,
                            'Configurar_pdt':Menu_config().iniciar }
        while True:

      

            event, values = self.window.read()
 
            if event == sg.WIN_CLOSED or event == 'Cancelar': # se o usuário fechar a janela ou clicar em cancelar
                break
            if event in butoes_especiais:
                butoes_especiais[event]()
                


            tratador_de_eventos_principal.iniciar(self.window,event,values,self.colunas)


            #print('Voce digitou ', values[0])
        self.window.close()
    def colunas_lista(self,colunas,titulos_das_colunas):
        #definir os titulos das colunas que irao aparecer na tela
        textos_titulo_coluna = {'id':'id',
                   'nome':'Nome',
                   'valor_venda':'Valor',
                   'quantidade':'Quantidade',
                   'genero':'Genero',
                   'categoria':'Categoria',
                   'cod':'Codig Barra',
                   'valor_compra':'Valor Custo'}

        for row in colunas:
            titulo = textos_titulo_coluna[row]
            titulos_das_colunas.append(titulo)



    def iniciar_lista_pesquisa(self):
        self.lista_pesquisa = self.produto_linha(self.estoque.consulta_todos_produtos(),self.colunas)



Menu_principal().init()