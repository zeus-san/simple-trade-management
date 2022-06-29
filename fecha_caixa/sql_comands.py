#CASO a tabela nao exista executar esse comando
CRIAR_TABELA="""CREATE TABLE IF NOT EXISTS tb_produtos(
            N_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            T_NOME_PRODUTO VARCHAR(45),
            N_VALOR_VENDA100 INTEGER,
            N_QUANTIDADE INTEGER,
            T_GENERO VARCHAR(10),
            T_CATEGORIA VARCHAR(10),
            N_COD_BARRA VARCHAR(15),
            N_VALOR_COMPRA100 INTEGER
);"""
#modelo de inseir na tabela
M_INSER = '''INSERT INTO tb_produtos (T_NOME_PRODUTO,
            T_TIPO,
            T_GRUPO,
            N_QUANTIDADE,
            N_VALIDADE) VALUES ('testenome','testetipo','testegrupo',10,'00-00-0000')'''
#Seleciona os nomes da tabela
SElE_NAMES = "SELECT name FROM sqlite_master WHERE type='table' AND name='tb_produtos';"

#deleta tabela
DEL_DB = 'DELETE FROM SQLITE_SEQUENCE WHERE name="tb_produtos";'

#selecionar todos da tabela
SELE_ALL='''SELECT * FROM tb_produtos'''  

SElE_PRODUT = "SELECT name FROM sqlite_master WHERE type='table' AND name='tb_produtos';"
