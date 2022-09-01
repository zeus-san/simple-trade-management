import Estoque
from produto import Produto
class cadastrar:
    def iniciar(self,window,event,values):
        self.window = window
        self.event = event
        self.values = values
        self.valor_venda_elemnt = self.window.Element('valor_venda')
        self.valor_compra_elemnt = self.window.Element('valor_compra')
        self.rodando = True
        self.tratar()
        
    def tratar(self):
        
        if self.event == "valor_compra":
            self.valor_compra_events()
        elif self.event == "valor_venda":
            self.valor_venda_events()

        self.mais_tratamentos()

    def valor_compra_events(self):
        self.somente_entrar_real()
       
        if self.converter_para_numero(self.values[self.event]):
            self.sugerir_valor_venda()

    def somente_entrar_real(self):
        chave = self.event
        self.values[chave] = self.values[chave].replace(',','.')
        if bool(self.values[self.event]) and self.values[chave][-1] not in '0123456789.' or self.values[chave].count('.') > 1:
            self.window.Element(chave).update(self.values[chave][:-1])
            self.values[chave] = self.values[chave][:-1]


            
            
           
              
    def sugerir_valor_venda(self):
        valor_produto = float(self.values[self.event])
        lucro_porcetangem = 0.3
        lucro_liquido = valor_produto * lucro_porcetangem
        valor_produto_final = valor_produto + lucro_liquido
        self.valor_venda_elemnt.update(f'{valor_produto_final:.2f}')

    def valor_venda_events(self):

        self.somente_entrar_real()

    def converter_para_numero(self,str_numero):
        try:
            float(str_numero)
            return True
        except:
            return False

    def validacoes(self):
        # Campos Obrigatorios #
        # Nome
        # Valor Venda
        # Quantidade
        aux = self.verificar_valor_compra()
        condicao1 = bool(self.verificar_nome()) and self.verificar_valor_venda()
        condicao2 = self.verificar_quantidade() and aux
        if condicao1 and condicao2:
            return True
            
        else: 
            
            return False

    def verificar_nome(self):
        nome = self.values['nome']
        
        if nome.isspace() or nome.isnumeric() or not bool(nome):
            self.window.Element('nome').update(background_color='#BF0010')
        else:
            self.window.Element('nome').update(background_color='#F0F4F5')
            return True
        
    def verificar_valor_venda(self):
        valor_venda = self.values['valor_venda']
        if not self.converter_para_numero(valor_venda)  or not bool(valor_venda):
            self.window.Element('valor_venda').update(background_color='#BF0010')
            
        else:
            self.window.Element('valor_venda').update(background_color='#F0F4F5')
            return True
        
    def verificar_quantidade(self):
        quantidade = self.values['quantidade']
        if not self.converter_para_numero(quantidade):
            pass
        else:
            
            return True

    def verificar_valor_compra(self):
        valor_compra = self.values['valor_compra']
        
        if not self.converter_para_numero(valor_compra):
            pass
        else:
           
            return True

    def mais_tratamentos(self):
        print(self.event,self.values)
        if self.event == 'finalizar':
            print('evento entrado')
            if self.validacoes():
                print('cadastro')
                self.cadastrar_produto()
        
    def cadastrar_produto(self):
        args = self.values
        args['valor_venda'] = float(args['valor_venda'].replace(',','.'))
        args['quantidade'] = float(args['quantidade'])
        args['valor_compra'] = float(args['valor_compra'].replace(',','.'))
        produto = Produto(**args)
        estoque = Estoque.Estoque()
        estoque.add_produto(produto)
        self.rodando = False
        


        