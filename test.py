from src.infa_banco.conexao_sqlite import ConexaoSqlite


csqlite = ConexaoSqlite()
csqlite.conectar_banco()
csqlite.inserir_dados(
    tabela='SITE',
    valores=[1, 'GLOBO'],
    colunas=('ID_SITE', 'NOME_SITE')
)
csqlite.fechar_conexao()
