import PySimpleGUI as sg
from Estoque import Estoque
def pesquisa():
    colunas_select = ['id','nome','quantidade','valor_venda']
    titulos_colunas = ['Id','Nome','Qtds','Valor']
    def produto_linha(lista_produtos):
        colunas = colunas_select
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
    estoque = Estoque()
    res_estoque = estoque.consulta_todos_produtos()
    pradonizado = produto_linha(res_estoque)
    titulo = "Selecionar Produto"
    layout = [
        [sg.Text('Nome'),sg.Input(size=(20,0),key='nome_input',enable_events=True)],
        [sg.Table(pradonizado,titulos_colunas,select_mode=sg.TABLE_SELECT_MODE_BROWSE,expand_x = True,key='lista_pdt',col_widths=(3,3,25,4),)],
    
        [sg.Button('Salvar'),sg.Text('',size=(10,0)),sg.Button('Cancelar')],
    ]
    window = sg.Window(titulo,layout=layout,size=(800,500),element_justification='c',font='arial 23')
    valido = False
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit','Cancelar'):
            
            break
        print(event,values)
        
        if event == 'nome_input' and values['nome_input']:
            res_estoque=estoque.consulta_nome(values['nome_input'])
            padronizado = produto_linha(res_estoque)
            window.Element('lista_pdt').update(padronizado)
        if  event == 'nome_input' and not values['nome_input']:
            res_estoque = estoque.consulta_todos_produtos()
            padronizado = produto_linha(res_estoque)
            window.Element('lista_pdt').update(padronizado)
        if event == 'Salvar' and values['lista_pdt']:
            valido = True
            break

    window.close()     
    if valido:
        
        return pradonizado[values['lista_pdt'][0]][0]

