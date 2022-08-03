from curses import window
import PySimpleGUI as sg
import config
class Menu_config:
    def __init__(self):
        self.default_valores()
        self.dados = config.config.ler_dados()
    def iniciar(self):
        self.execucao_tela_config()
    def layout_tela(self):
        # "c" de checkbox, gambiarra para diminuir a manuntenção
        valores_check = [[sg.Checkbox(self.valores[valor],key=valor,default=self.valor_checkbox(valor))] for valor in self.valores]
        layout = [
            [sg.Text("texto",key="text")],
            [sg.Column(valores_check)],
            [sg.Button('Confirmar'),sg.Button('Cancelar')]
        ]
        return layout
    def execucao_tela_config(self):
        layout = self.layout_tela()

        window = sg.Window("Configuracoes",layout=layout,size=(400,600),keep_on_top=True)

        tratar = Tratar_events()
        while True:
            event , values = window.read()
            if event == sg.WIN_CLOSED or event == "Cancelar":
                break
            tratar.iniciar(window,event,values)
            
          
    def default_valores(self):
        self.valores = {
                   'quantidade':'Quantidade',
                   'genero':'Genero',
                   'categoria':'Categoria',
                   'cod':'Codig Barra',
                   'valor_compra':'Valor de Custo'}
    def valor_checkbox(self,valor):
        if valor in self.dados['campos']:
            return True
        else:
            return False
    
class Tratar_events:
    def iniciar(self,window,event,values):
        self.window = window
        self.event = event
        self.values = values
        self.dados = config.config.ler_dados()
        self.tratar()

    def tratar(self):
        if self.event == "Confirmar":
            self.gravar_dados()

    def gravar_dados(self):
        campos = ['quantidade','genero','categoria','cod','valor_compra']
        for chave in self.values:
            if chave in campos:#separar as chaves dos resto dos valores
             
                if chave in self.dados["campos"]:#se a chave esta selecionada
                
                    if not self.values[chave]:#remover ou manter
                      
                        self.dados["campos"].remove(chave)#se ja estiver remova
                        
                        
                else:
                    
                    if self.values[chave]:
                     
                        self.dados['campos'].append(chave)
       
        config.config.gravar_dados(self.dados)                

                

