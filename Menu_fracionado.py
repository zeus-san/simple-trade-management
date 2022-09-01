from logging import exception
import PySimpleGUI as sg
import Menu_pesquisa
def convert_str(str_numero):
    try:
        fl_numero=float(str_numero)
        return fl_numero
    except:
        pass

titulo = "Frios"
layout = [
    [sg.Text('Id'),sg.Input(size=(20,0),key='id_input'),sg.Button('selecionar'),sg.Button("Pesquisa",size=(8,0),key='pesquisa_bt')],
    [sg.Text('',key='-Nome_Pdt-'),sg.Text(13,key='-valor_pdt-')],
    [sg.Input(size=(10,1),key='gramas_input',enable_events=True,do_not_clear=True),sg.Text('g'),
        sg.Text('x',font='Arial 20',text_color='black'),
    sg.Text('R$'),sg.Input(size=(10,1),key='valor_input',enable_events=True)],
 
    [sg.Button('Salvar'),sg.Button('Cancelar')],
]
largura = 400
altura = 200

tamanho_janela = (largura,altura)


window = sg.Window("Nova tela",layout=layout,element_justification='c')

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    print(event,values,'-> 1')

    valor_kg = int(window.Element('-valor_pdt-').get())

    # ---- Bloquear entrada de caracteres que nao sao numero---- #
    if event in ('gramas_input','id_input'):
        chave = event
        if values[event] and values[chave][-1] not in '0123456789':
            window.Element(chave).update(values[chave][:-1])
            values[chave] = values[chave][:-1]

    # ---- Bloquear caracteres que nao sao numero, ou ponto ---- #
    if event == 'valor_input':
        chave = event
        values[chave] = values[chave].replace(',','.')
        if bool(values[event]) and values[chave][-1] not in '0123456789.' or values[chave].count('.') > 1:
            window.Element(chave).update(values[chave][:-1])
            values[chave] = values[chave][:-1]
            print(values[chave])
    
    # --- Alterar o valor com base na quantidades de gramas inseridas --- #
    if event == 'gramas_input' and values['gramas_input'] and convert_str(values['gramas_input']):
        gramas = int(values['gramas_input'])
        valor = valor_kg/1000
        window.Element('valor_input').update(f'{valor*gramas:.2f}')
    

    

    # ---- Alterar as gramas com base no valor especificado -- #
    if event == 'valor_input' and values['valor_input'] and convert_str(values['valor_input']):
        valor = float(values['valor_input'])
        
        valor_final = (valor*100)/valor_kg*10
        window.Element('gramas_input').update(f'{valor_final:.0f}')
    
    # --- chamar tela de pesquisa de produto --- #
    if event == 'pesquisa_bt':
        res = Menu_pesquisa.pesquisa()
        if res:
            window.Element('id_input').update(res)
            



    
