from conexaodb import conexaodb
from produto import Produto
class Estoque:
    def __init__(self):
        conexao_db = conexaodb()
        self.consulta = conexao_db.consultar
        self.execut = conexao_db.executar
    def consulta_id(self,identi):#read
        #consulta um id
        vsql = f'SELECT * FROM tb_produtos WHERE N_ID={identi}'
        produtos_database=self.consulta(vsql)
        produto = Produto()
        print(produtos_database,len(produtos_database),'estoque alert')
        if len(produtos_database) == 0:
            produto = ''
        else:
            produto.preencher_dados(produtos_database[0])
        return produto
    def consulta_nome(self,nome):#read
        vsql = f"SELECT * FROM tb_produtos WHERE T_NOME_PRODUTO LIKE '%{nome}%'"
        lista_produtos = []
        for row in self.consulta(vsql):
            produto = Produto()
            produto.preencher_dados(row)
            lista_produtos.append(produto)
        return lista_produtos
    def consulta_todos_produtos(self):#read
        vsql='SELECT * FROM tb_produtos'
        lista_produtos = []
        for row in self.consulta(vsql):
            produto = Produto()
            produto.preencher_dados(row)
            lista_produtos.append(produto)
        return lista_produtos
    def mudar_quantidade_venda(self,produto_id:int,quantidade:int):
        vsql = f'UPDATE tb_produtos SET N_QUANTIDADE=N_QUANTIDADE-{quantidade} WHERE N_ID={produto_id}'
        self.execut(vsql)
    def mudar_quantidade(self,produto,q):#update
        vsql = f'UPDATE tb_produtos SET N_QUANTIDADE={q} WHERE N_ID={produto.id}'
        self.execut(vsql)
    def add_produto(self,produto):#create
        dados = produto.dadosback()
        vsql = f"""INSERT INTO tb_produtos (
            T_NOME_PRODUTO,
            N_VALOR_VENDA100,
            N_QUANTIDADE,
            T_GENERO,
            T_CATEGORIA,
            N_COD_BARRA,
            N_VALOR_COMPRA100)
        VALUES ('{dados['nome']}',
                '{dados['valor_venda']}',
                '{dados['quantidade']}',
                '{dados['genero']}',
                '{dados['categoria']}',
                '{dados['cod']}',
                '{dados['valor_compra']}')"""
        self.execut(vsql)
    def atualizar_produto(self,produto):
        dados = produto.dadosback()
        
        vsql = f"""UPDATE tb_produtos SET
            T_NOME_PRODUTO='{dados['nome']}',
            N_VALOR_VENDA100='{dados['valor_venda']}',
            N_QUANTIDADE='{dados['quantidade']}',
            T_GENERO = '{dados['genero']}',
            T_CATEGORIA='{dados['categoria']}',
            N_COD_BARRA='{dados['cod']}',
            N_VALOR_COMPRA100 = '{dados['valor_compra']}'
        WHERE N_ID={dados['id']}"""

        self.execut(vsql)

