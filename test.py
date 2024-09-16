import streamlit as st

# Exemplo de dados de notícias
noticias = [
    {
        "NOME_SITE": "Site 1",
        "CATEGORIA": "Tecnologia",
        "TITULO_NOTICIA": "Título da Notícia 1",
        "DESCRICAO": "Descrição curta da notícia 1.",
        "URL_NOTICIA": "https://exemplo.com/noticia1",
        "URL_IMG": "https://via.placeholder.com/150"
    },
    {
        "NOME_SITE": "Site 2",
        "CATEGORIA": "Política",
        "TITULO_NOTICIA": "Título da Notícia 2",
        "DESCRICAO": "Descrição curta da notícia 2.",
        "URL_NOTICIA": "https://exemplo.com/noticia2",
        "URL_IMG": "https://via.placeholder.com/150"
    },
    {
        "NOME_SITE": "Site 3",
        "CATEGORIA": "Esportes",
        "TITULO_NOTICIA": "Título da Notícia 3",
        "DESCRICAO": "Descrição curta da notícia 3.",
        "URL_NOTICIA": "https://exemplo.com/noticia3",
        "URL_IMG": "https://via.placeholder.com/150"
    }
]

# Layout no Streamlit para exibição das notícias
st.title("Feed de Notícias")

for noticia in noticias:
    st.image(noticia["URL_IMG"], width=150)
    st.subheader(noticia["TITULO_NOTICIA"])
    st.write(
        f"**Fonte:** {noticia['NOME_SITE']} | **Categoria:** {noticia['CATEGORIA']}")
    st.write(noticia["DESCRICAO"])
    st.markdown(f"[Leia mais]({noticia['URL_NOTICIA']})")
    st.markdown("---")
