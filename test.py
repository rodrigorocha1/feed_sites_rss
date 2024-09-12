from src.infa_banco.conexao_sqlite import ConexaoSqlite


csqlite = ConexaoSqlite()
csqlite.conectar_banco()
csqlite.inserir_dados(
    tabela='SITE',
    valores=[2, 'SBT'],
    colunas=('ID_SITE', 'NOME_SITE')
)
csqlite.fechar_conexao()
