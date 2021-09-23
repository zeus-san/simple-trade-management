import PySimpleGUI as sg
import sistema
#sg.theme('DarkAmber')   # Adicione um toque de cor
# Todas as coisas dentro da sua janela.
#############################################
def c(a):#pegar so o id#Coletor de ID
    return int(a[-1])
#############################################
def processar_venda(lista):
    #print('evento 2.1')
    for i in lista:
        sistem.venda(c(i[0]),1)
#############################################
def pesquisa_posi(valor,lista):
    for posicao,i in enumerate(lista):
        if valor in i:
            return posicao
#############################################
def processar_evento(event,values,window):
    lista_exibicao_produtos = formatar(sistem.todos_produtos())
    global venda_list
    #pesquisa
    if bool(values[0]):
        print('evento0')
        pesquisa = []
        for i in lista_exibicao_produtos:
            if values[0] in i[1]:
                pesquisa.append(i)
        window.Element('-LIST-').update(pesquisa)
    else:
        window.Element('-LIST-').update(lista_exibicao_produtos)
    

    if bool(values['-LIST-']):
        #print('evento1')
        #atualizar lista de produtos da venda //passivo
        venda_list.append((lista_exibicao_produtos[values['-LIST-'][0]][0],lista_exibicao_produtos[values['-LIST-'][0]][1]))
        window.Element('-VENDA-').update(venda_list)
        window.Element('AVISO').update('')
    if event == 'Vender' and bool(venda_list):
        #print('evento2')
        #relizar uma venda
        window.Element('AVISO').update('venda realizada')
        processar_venda(venda_list)
        venda_list = []
        window.Element('-VENDA-').update(venda_list)
    elif not bool(venda_list) and event == 'Vender':
        print('evento3')
        #avisar caso o usuario tente realizar uma venda sem nenhum produto
        window.Element('AVISO').update('Adicione produtor para fazer uma venda')
    elif event == 'Casdastrar_pdt':
        #chamar a funçao tela de cadastro
        tela_cadastrar()
    elif event == 'Deletar' and bool(values['-VENDA-']):
        #remover um item da lista de compra
        index=pesquisa_posi(values['-VENDA-'][0][1],venda_list)
        #print(index)
        venda_list.pop(index)
        window.Element('-VENDA-').update(venda_list)
    elif event == 'Atualizar_pdt':
        #chamar a funçao de atualizar
        tela_atualizar()
    elif event == 'Limpa':
        #limpar lista de compra
        venda_list = []
        window.Element('-VENDA-').update(venda_list)
        window.Element('AVISO').update('Lista Limpa')
#############################################
def gui_deletar():
    layout = [
        [sg.Text('Digite o id do produto'),sg.Input(size=20,key='id'),sg.Button('Pesuisar',expand_x=True)],
        [sg.Text(text_color='black',background_color='grey83',key='produto',expand_x=True)],
        [sg.Button('Deletar')]
        ]
    return layout

#############################################
def tela_deletar():
    layout = gui_deletar()
    # Aqui eu esntacio
    exist_pdt = False
    window = sg.Window('Titulo da Janela', layout,size=(400,200))
    # Loop de eventos para processar "eventos" e obter os "valores" das entradas
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancelar': # se o usuário fechar a janela ou clicar em cancelar
            break
        elif event == 'Pesuisar':
            valores=sistem.consulta_id(int(values['id']))
            if valores:
                valores = valores[0]
                window.Element('produto').update(valores)
                exist_pdt = True
            else:
                window.Element('produto').update('')
                sg.popup('Produto não encontrado')
                exist_pdt = False
        elif event == 'Deletar' and not exist_pdt :
            sg.popup('Id invalido\ndigite um id valido')
        elif event == 'Deletar' and bool(values['id']):
            a=sg.popup_yes_no('Voce quer mesmo apagar esse produto?')
            if a == 'Yes':
                sistem.deletar_produto(int(values['id']))
                sg.popup('Produto deletado')
                break
            
    window.close()
#############################################
def gui_atualizar():
    layout = [
        [sg.Text('Digite o id do Produto'),sg.Input(key='identi'),sg.Button('Pesquisar',key='B_pesquisa')],
        [sg.Text('Nome do produto')],
        [sg.Input(expand_x=True,key='nome')],
        [sg.Text('Tipo do produto'),sg.Input('Void',key='tipo')],
        [sg.Text('Grupo do produto'),sg.Input('Void',key='grupo')],
        [sg.Text('Quantidade'),sg.Input(0,size=5,key='quantidade'),
         sg.Text('Key'),sg.Input('Void',size=5,key='key'),
         sg.Text('Validade'),sg.Input('00-00-0000',size=10,key='validade')],
        [sg.Text('Codigo barra'),sg.Input('00000000000000000000000000',key='cod_barra')],
        [sg.Button('Atualizar'),sg.Button('Cancelar',focus=True)],
        ]
    return layout
#############################################
def tela_atualizar():
    layout = gui_atualizar()
    # Aqui eu esntacio
    window = sg.Window('Titulo da Janela', layout)
    # Loop de eventos para processar "eventos" e obter os "valores" das entradas
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancelar': # se o usuário fechar a janela ou clicar em cancelar
            break
        elif bool(values['identi']) and event == 'B_pesquisa':
            valores=sistem.consulta_id(int(values['identi']))
            if valores:
                valores = valores[0]
                window.Element('nome').update(valores[1])
                window.Element('tipo').update(valores[2])
                window.Element('grupo').update(valores[3])
                window.Element('quantidade').update(valores[4])
                window.Element('validade').update(valores[5])
                window.Element('key').update(valores[6])
                window.Element('cod_barra').update(valores[7])
            else:
                sg.popup('Produto não encontrado')
        elif event == 'Atualizar' and bool(values['identi']):
            sistem.atualizar_produto(**values)
            break
    window.close()
#############################################    
def gui_cadastrar():
    #sg.popup('num sei','lala')
    #sg.popup_get_text('mds')
    
    layout = [
        [sg.Text('Nome do produto')],
        [sg.Input(expand_x=True,key='nome')],
        [sg.Text('Tipo do produto'),sg.Input('Void',key='tipo')],
        [sg.Text('Grupo do produto'),sg.Input('Void',key='grupo')],
        [sg.Text('Quantidade'),sg.Input(0,size=5,key='quantidade'),
         sg.Text('Key'),sg.Input('Void',size=5,key='key'),
         sg.Text('Validade'),sg.Input('00-00-0000',size=10,key='validade')],
        [sg.Text('Codigo barra'),sg.Input('00000000000000000000000000',key='cod_barra')],
        [sg.Button('Cadastrar'),sg.Button('Cancelar',focus=True)],
        ]
    return layout
#############################################
def tela_cadastrar(Primeiro_uso=False):
    
    layout = gui_cadastrar()
    # Aqui eu esntacio
    window = sg.Window('Titulo da Janela', layout,size=(400,200))
    # Loop de eventos para processar "eventos" e obter os "valores" das entradas
    while True:
        if Primeiro_uso:
            sg.popup()
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancelar': # se o usuário fechar a janela ou clicar em cancelar
            break
        elif event == 'Cadastrar' and len(values['nome']) == 0:
            print('alo')
            sg.popup('O produto precisa ter um nome')
        else:
            sistem.add_produto(**values)
            sg.popup('Produto cadastrado com sucesso')
            break
    window.close()
#############################################
def gui_principal():
    global venda,venda_list
    titulos = ['id','nome','tipo','grupo','quantidade','validade','key','cod_barra']
    venda = []
    venda_list = []
    colunaButtao = [
                [sg.Button('Cadatrar\nProduto',size=(10,2),key='Casdastrar_pdt')],
                [sg.Button('Excluir\nproduto',size=(10,2),key='Deletar_pdt')],
                [sg.Button('Atualizar\nproduto',size=(10,2),key='Atualizar_pdt')]
                    ]
    colunaMeio = [
            [sg.Input(enable_events=True),sg.Button('Atualizar',key='atualizar_list')],
            [sg.Table(lista_exibicao_produtos,headings=titulos,key='-LIST-',expand_x = True,enable_events=True)],
            [sg.Listbox(venda,size=(124,10),key='-VENDA-',expand_x = True,enable_events=True)],
            [sg.Button('Vender'),sg.Text('',size=(20,1),key='AVISO'),sg.Button('Deletar'),sg.Text('',size=(20,1)),sg.Button('Limpar', key='Limpa')]
              ]
    layout = [
            [sg.Column(colunaButtao),sg.Column(colunaMeio,justification='center')],
            [sg.Button('OK',tooltip='Aperte aqui'), sg.Button('Cancelar')]
            ]
    return layout
#############################################
def formatar(lista):
    novalista=[]
    for bruta in lista:
        #print(bruta)
        formatada = ('%03d' % bruta[0],bruta[1],bruta[2],bruta[3],bruta[4],bruta[5],bruta[6],bruta[7])
        #print(formatada)
        novalista.append(formatada)
    return novalista
#############################################
def tela_principal():
    layout = gui_principal()
    
    # Aqui eu esntacio
    window = sg.Window('Titulo da Janela', layout,size=(900,750))
    # Loop de eventos para processar "eventos" e obter os "valores" das entradas

    while True:

        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Cancelar': # se o usuário fechar a janela ou clicar em cancelar
            break
        
        processar_evento(event,values,window)

        #print('Voce digitou ', values[0])

    window.close()
#############################################

sistem = sistema.FuncoesDb()
lista_bruta_produtos=sistem.todos_produtos()
lista_exibicao_produtos = formatar(lista_bruta_produtos)
#if len(lista_exibicao_produtos) == 0:
   # tela_cadastrar(True)
tela_principal()
#else:
    #tela_principal()
#tela_atualizar()

#tela_deletar()





