import sqlite3
from sqlite3 import Error
import os,os.path
import sql_comands

class conexaodb:
    def __init__(self):
        self.coletar_caminho()
        self.executar(sql_comands.CRIAR_TABELA)

    def conexao(self):
        #Conectar ao banco de dados
        caminho = self.caminho_db
        try:
            conex = sqlite3.connect(caminho)
        except Error as erro:
            print(erro)
        return conex

    def executar(self,sql):
        #executar comandos sqls
        cone = self.conexao()
        try:
            c=cone.cursor()
            c.execute(sql)
            cone.commit()
        except Error as erro:
            print(erro)

        else:
            
            pass
        finally:
            cone.close()
    def consultar(self,sql):
        cone = self.conexao()
        try:
            c=cone.cursor()
            c.execute(sql)
            res = c.fetchall()
        except Error as erro:
            print(erro)

        else:
            pass
            #print('Sucesso')
        finally:
            cone.close()
            return res
    def coletar_caminho(self):
        self.caminho_diretori = os.path.dirname(os.path.abspath(__file__))
        self.caminho_db = os.path.join(self.caminho_diretori,'produtos2.db')