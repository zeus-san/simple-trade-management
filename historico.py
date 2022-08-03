import os
from datetime import datetime
class historico:
    def criar_arquivo(self):
        self.nome_arquivo = 'historico.txt'
        if not os.path.exists(self.nome_arquivo):
            arquivo = open(self.nome_arquivo, 'w')
            arquivo.close()
            
            
    def add_venda(self,lista):
        self.criar_arquivo()
        texto_inserir = ''
        texto_inserir += '+-+-+'*15+'\n'
        dados_data = datetime.now().strftime('%H:%M %d/%m')
        texto_inserir += f"    Venda {dados_data} \n"
        venda = ''
        for row in lista:

            lista_str = f'QUANTIDADE = {row[3]} NOME="{row[1]}" VALOR={row[2]} ID={row[0]}'
            lista_str += '\n'
            venda += lista_str
        texto_inserir += venda
        texto_inserir += '+-+-+'*15+'\n'
        self.inserir_no_arquivo(texto_inserir)


        rodape = '\n'
    def add_texto(self,texto):
        self.criar_arquivo()
        texto_especial = "="*15+'\n'+texto+'\n'+"="*15
        self.inserir_no_arquivo(texto_especial +'\n')
    def inserir_no_arquivo(self,texto):
        arquivo = open(self.nome_arquivo, 'r') # Abra o arquivo (leitura)
        conteudo = arquivo.readlines()
        conteudo.append(texto)   # insira seu conteúdo
        arquivo = open(self.nome_arquivo, 'w') # Abre novamente o arquivo (escrita)
        arquivo.writelines(conteudo)    # escreva o conteúdo criado anteriormente nele.
        arquivo.close()
        

