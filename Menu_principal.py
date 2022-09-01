
import PySimpleGUI as sg
import Estoque
from Menu_cadastro import Menu_cadastro
from Menu_config import Menu_config
from Menu_atualizar import Menu_atualizar
import tratamento_principal
import config
class Menu_principal:
    def init(self):
        self.titulos = []
        self.titulos_compra = []
        self.lista_pesquisa = []
        self.lista_compra = []
        self.colunas = config.COLUNAS
        self.colunas_compra = ['id','unidades','quantidade','nome','valor_venda']
        self.estoque = Estoque.Estoque()
        self.produto_linha = tratamento_principal.principal().produto_linha
        self.iniciar_lista_pesquisa()
        self.estilizacao_dos_titulos_colunas(self.colunas,self.titulos)
        self.estilizacao_dos_titulos_colunas(self.colunas_compra,self.titulos_compra)
        self.execucao_tela_principal()


    def layout_tela(self):
        #layout da tela
        colunaButtao = [
                    [sg.Button('Cadatrar\nProduto',size=(10,2),key='Casdastrar_pdt')],
                    [sg.Button('Excluir\nproduto',size=(10,2),key='Deletar_pdt')],
                    [sg.Button('Atualizar\nproduto',size=(10,2),key='Atualizar_pdt')]
                        ]
        colunaMeio = [
                [sg.Input(enable_events=True,key='pesquisa'),
                 sg.Button('Atualizar',key='atualizar_list'),
                 sg.Button('Fracionado',key='fracionado')
                ],
                [sg.Table(self.lista_pesquisa,headings=self.titulos,key='-LISTA_PESQUISA-',size=(45,15),expand_x = True,enable_events=True)],#lista produtos
                
                [ #Tabela com a lista de itens sendo comprados
                 sg.Table(
                     [],
                     headings=self.titulos_compra,size=(45,15),
                     key='-LISTA_COMPRA-',
                     expand_x = True,
                     auto_size_columns = False,
                     max_col_width=2,
                     select_mode=sg.TABLE_SELECT_MODE_BROWSE,
                     col_widths=(4,4,4,25,4),
                     justification='center',
                     #enable_events=True,
                     right_click_menu=['Unusedi', ['Editar', 'Apagar::lista_compra_rig_click_menu', 'Cancelar::lista_compra_rig_click_menu', ]],
                     )
                ],
                
                [#
                 sg.Frame('Total',[
                        [sg.T('',)],
                        [sg.Text(' 00 ',key='total',justification='rigth',expand_x=True,font=('arial 15'))],],
                        expand_x=True,
                        )
                ],
                
                [
                 sg.Button('Vender',focus=True),
                 sg.Text('',size=(20,1),key='AVISO'),
                 sg.Button('Deletar'),
                 sg.Text('',size=(20,1)),
                 sg.Button('Limpar', key='Limpa')
                 ]
                ]
        coluna_price = [
                [sg.Button("Fechar",key='Cancelar')],
                [ sg.Button("Configurações",key='Configurar_pdt')],
                [sg.Text()]
        
        
        
                ]
        
        layout = [
                [
                 sg.Column(colunaButtao),
                 sg.Column(colunaMeio,justification='center'),
                 sg.Column(coluna_price)],
               
                ]
        return layout
    def execucao_tela_principal(self):
        layout = self.layout_tela()
        
        # Aqui eu esntacio
        self.window = sg.Window('Titulo da Janela', layout,font='arial 16')
        # Loop de eventos para processar "eventos" e obter os "valores" das entradas
        tratador_de_eventos_principal = tratamento_principal.principal()
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
    def estilizacao_dos_titulos_colunas(self,colunas,titulos_das_colunas):
        #definir os titulos das colunas que irao aparecer na tela
        textos_titulo_coluna = {'id':'Id',
                   'nome':'Nome',
                   'valor_venda':'Valor',
                   'quantidade':'Quant',
                   'genero':'Genero',
                   'categoria':'Categoria',
                   'cod':'Codig Barra',
                   'valor_compra':'Valor Custo',
                   'unidades':'Unid'}

        for row in colunas:
            titulo = textos_titulo_coluna[row]
            titulos_das_colunas.append(titulo)

    def iniciar_lista_pesquisa(self):
        self.lista_pesquisa = self.produto_linha(self.estoque.consulta_todos_produtos(),self.colunas)



Menu_principal().init()