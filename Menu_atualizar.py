import PySimpleGUI as sg
from Tratar_eventos import atualizar
import config
class Menu_atualizar:
    def iniciar(self):
        self.execucao_tela_atualizar()
    def layout_tela(self):
        layout = [
            [
             sg.Text('Digite o id do Produto'),
             sg.Input(key='identi'),
             sg.Button('Pesquisar',key='pesquisa')
             ],
            [sg.Text('Nome do produto')],
            [sg.Input(expand_x=True,key='nome')],
            [
             sg.Text('Genero'),
             sg.Combo(['Perecivel','Nao Perecivel'],key='genero',default_value='Perecivel',expand_x=True,readonly=True)
            ],
            [
             sg.Text('Categoria'),
             sg.Combo(config.CATEGORIAS,key='categoria',default_value=config.CATEGORIAS[0],expand_x=True,readonly=True)
             ],
             [
             sg.Text('Valor'),
             sg.Input(0,size=5,key='valor_venda'),
             sg.Text('Quantidade'),
             sg.Input(0,size=5,key='quantidade'),
             sg.Text('Valor Compra'),
             sg.Input(0,size=5,key='valor_compra'),
             ]
            ,
            [sg.Text('Codigo barra'),sg.Input('00000000000000000000000000',key='cod')],
            [sg.Button('Atualizar'),sg.Button('Cancelar',focus=True)],
            ]
        return layout
    def execucao_tela_atualizar(self):
        layout = self.layout_tela()
        # Aqui eu esntacio
        window = sg.Window('Titulo da Janela', layout)
        # Loop de eventos para processar "eventos" e obter os "valores" das entradas
        tratar = atualizar()
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar': # se o usuário fechar a janela ou clicar em cancelar
                break
            tratar.iniciar(window,event,values)
            sg.popup(tratar.validacao,keep_on_top=True,title="Situação")
            
        window.close()
