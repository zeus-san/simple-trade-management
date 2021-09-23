import sqlite3
from sqlite3 import Error
import os,os.path
class conexaodb():
    def conexao(self):
        #print('Conexão bem sucedida')
        caminho = 'C:\\Users\\ZEUS\\Documents\\projetos_python\\sistema para a banca\\produtos.db'
        try:
            conex = sqlite3.connect(caminho)
        except Error as erro:
            print(erro)
        return conex
    def executar(self,sql):
        cone = self.conexao()
        try:
            c=cone.cursor()
            c.execute(sql)
            cone.commit()
        except Error as erro:
            print(erro)

        else:
            #print('Sucesso')
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
    
    def __enter__(self):
        self.con = self.conexao()
        
    def __exit__(self,type,value,traceback):
        self.con.close()
vsql3 = 'DELETE FROM SQLITE_SEQUENCE WHERE name="tb_produtos";'
vsql2='''SELECT * FROM tb_produtos'''    
vsql='''INSERT INTO tb_produtos (T_NOME_PRODUTO,
            T_TIPO,
            T_GRUPO,
            N_QUANTIDADE,
            N_VALIDADE) VALUES ('testenome','testetipo','testegrupo',10,'00-00-0000')'''
vsql0="""CREATE TABLE tb_produtos(
            N_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            T_NOME_PRODUTO VARCHAR(45),
            T_TIPO VARCHAR(10),
            T_GRUPO VARCHAR(10),
            N_QUANTIDADE INTEGER,
            N_VALIDADE DATE,
            T_KEY VARCHAR(15),
            N_COD_BARRA INTEGER
);"""
a = conexaodb()
#a.executar(vsql0)
#print(conexaodb().executar(vsql3))
class FuncoesDb:
    def __init__(self):
        self.consulta = conexaodb().consultar
        self.execut = conexaodb().executar
    def consulta_id(self,identi):
        vsql = f'SELECT * FROM tb_produtos WHERE N_ID={identi}'
        return self.consulta(vsql)
    def consulta_nome(self,nome):
        vsql = f"SELECT * FROM tb_produtos WHERE T_NOME_PRODUTO LIKE '%{nome}%'"
        return self.consulta(vsql)
    def todos_produtos(self):
        vsql='SELECT * FROM tb_produtos'
        return self.consulta(vsql)
    def nomes_produtos(self):
        vsql='SELECT N_ID,T_NOME_PRODUTO FROM tb_produtos'
        return self.consulta(vsql)
    def venda(self,identi,q):
        vsql = f'UPDATE tb_produtos SET N_QUANTIDADE=N_QUANTIDADE-{q} WHERE N_ID={identi}'
        self.execut(vsql)
    def add_estoque(self,identi,q):
        vsql = f'UPDATE tb_produtos SET N_QUANTIDADE=N_QUANTIDADE+{q} WHERE N_ID={identi}'
        self.execut(vsql)
    def add_produto(self,nome,tipo='Void',grupo='Void',quantidade=0,validade='Void',key='Void',cod_barra='Void'):
        vsql = f"""INSERT INTO tb_produtos (T_NOME_PRODUTO,T_TIPO,T_GRUPO,N_QUANTIDADE,N_VALIDADE,T_KEY,N_COD_BARRA)
        VALUES ('{nome}','{tipo}','{grupo}',{quantidade},'{validade}','{key}','{cod_barra}')"""
        self.execut(vsql)
    def deletar_produto(self,identi):
        vsql=f'DELETE FROM tb_produtos WHERE N_ID={identi}'
        self.execut(vsql)
    def atualizar_produto(self,identi,nome='',tipo='',grupo='',quantidade=0,validade='',key='',cod_barra=''):
        valores_novos = [nome,tipo,grupo,quantidade,validade,key,cod_barra]
        valores_antigo = self.consulta_id(identi)[0][1:]
        for p,i in enumerate(valores_novos):
            if not i:
                valores_novos[p]=valores_antigo[p]
            
        
        if True:
            vsql = f"""UPDATE tb_produtos SET
                        T_NOME_PRODUTO='{valores_novos[0]}',
                        T_TIPO='{valores_novos[1]}',
                        T_GRUPO='{valores_novos[2]}',
                        N_QUANTIDADE={valores_novos[3]},
                        N_VALIDADE='{valores_novos[4]}',
                        T_KEY='{valores_novos[5]}',
                        N_COD_BARRA='{valores_novos[6]}'
                    WHERE N_ID={identi}"""
            self.execut(vsql)


#FuncoesDb().atualizar_produto(1,grupo='perecivel')
#print(FuncoesDb().todos_produtos())
vsql4 = "SELECT name FROM sqlite_master WHERE type='table' AND name='tb_produtos';"
tabelas = a.consultar(vsql4)
if not tabelas:
    a.executar(vsql0)
    a.executar(vsql)
print()


