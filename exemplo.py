import streamlit as st

# Função para exibir as notícias de um site específico


def exibir_noticias_por_site(noticias, nome_site):
    with st.container():
        st.header(f"Notícias de {nome_site}")
        for noticia in noticias:
            st.subheader(noticia['titulo'])
            st.write(f"**Data de publicação:** {noticia['data_publicacao']}")
            st.write(f"**Categoria:** {noticia['categoria']}")
            st.write(f"**Descrição:** {noticia['descricao']}")
            st.write(f"[Leia mais]({noticia['url_noticia']})")

            if noticia.get('url_imagem'):
                st.image(noticia['url_imagem'], width=400)

            st.markdown("---")


# Exemplo de dados que podem vir de várias fontes (RSS de G1, UOL, etc.)
noticias = {
    'G1': [
        {
            'titulo': 'Título da Notícia do G1 - TAB1',
            'url_noticia': 'https://g1.globo.com/noticia1',
            'url_imagem': 'https://g1.globo.com/imagem1.jpg',
            'descricao': 'Descrição da notícia do G1 na TAB1.',
            'data_publicacao': '01-01-2024',
            'categoria': 'Brasil'
        },
        {
            'titulo': 'Título da Notícia do G1 - TAB2',
            'url_noticia': 'https://g1.globo.com/noticia2',
            'url_imagem': 'https://g1.globo.com/imagem2.jpg',
            'descricao': 'Descrição da notícia do G1 na TAB2.',
            'data_publicacao': '02-01-2024',
            'categoria': 'Economia'
        }
    ],
    'UOL': [
        {
            'titulo': 'Título da Notícia do UOL',
            'url_noticia': 'https://www.uol.com.br',
            'url_imagem': None,
            'descricao': 'Descrição da notícia do UOL.',
            'data_publicacao': '02-01-2024',
            'categoria': 'Mundo'
        }
    ],
    'Notícias ao Minuto': [
        {
            'titulo': 'Título da Notícia do Notícias ao Minuto',
            'url_noticia': 'https://www.noticiasaominuto.com.br',
            'url_imagem': 'https://www.noticiasaominuto.com.br/imagem.jpg',
            'descricao': 'Descrição da notícia do Notícias ao Minuto.',
            'data_publicacao': '03-01-2024',
            'categoria': 'Última Hora'
        }
    ]
}

# Layout com abas para separar as notícias por site
st.title("Agregador de Notícias")

abas = st.tabs(list(noticias.keys()))

# Exibir as notícias separadas por site em cada aba
for i, nome_site in enumerate(noticias.keys()):
    with abas[i]:
        if nome_site == 'G1':
            # Criação das abas internas para o G1 (TAB1 e TAB2)
            abas_g1 = st.tabs(["TAB1", "TAB2"])

            # Conteúdo para a aba TAB1
            with abas_g1[0]:
                st.write("Notícias da TAB1 do G1")
                # Filtra notícias de TAB1
                noticias_g1_tab1 = [
                    noticia for noticia in noticias['G1'] if "TAB1" in noticia['titulo']]
                exibir_noticias_por_site(noticias_g1_tab1, nome_site)

            # Conteúdo para a aba TAB2
            with abas_g1[1]:
                st.write("Notícias da TAB2 do G1")
                # Filtra notícias de TAB2
                noticias_g1_tab2 = [
                    noticia for noticia in noticias['G1'] if "TAB2" in noticia['titulo']]
                exibir_noticias_por_site(noticias_g1_tab2, nome_site)
        else:
            # Para os demais sites (UOL, Notícias ao Minuto), exibir normalmente
            exibir_noticias_por_site(noticias[nome_site], nome_site)
