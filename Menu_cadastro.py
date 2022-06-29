import PySimpleGUI as sg
import Tratar_eventos
import config
class Menu_cadastro:
    def iniciar(self):
        self.execucao_tela_cadastrar()
        
    def layout_tela(self):
        layout = [
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
             ],
            [
             sg.Text('Codigo barra'),
             sg.Input('00000000000000000000000000',key='cod')
             ],
            [
             sg.Button('Cadastrar'),
             sg.Button('Cancelar',focus=True)],
            ]  
        return layout
    def execucao_tela_cadastrar(self):
        
        layout = self.layout_tela()
        # Aqui eu esntacio
        window = sg.Window('Titulo da Janela', layout,size=(400,200),keep_on_top=True)
        # Loop de eventos para processar "eventos" e obter os "valores" das entradas
        
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar': # se o usuário fechar a janela ou clicar em cancelar
                break
            tratar = Tratar_eventos.cadastrar()
            tratar.iniciar(window,event,values)
            sg.popup(tratar.validacao,keep_on_top=True,title="Situação")
            
        window.close()

