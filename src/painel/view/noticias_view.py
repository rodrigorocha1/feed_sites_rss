import streamlit as st
from src.painel.controller.noticias_controller import NoticasControler
import textwrap


class NoticiasView():

    def __init__(self, controller: NoticasControler) -> None:
        self.__controler = controller

    def exibir_tela(self):

        st.title(f'Feed de Noticias')
        tab_g1, tab_gazeta_povo, tab_noticas_minuto = st.tabs(
            ['G1', 'Gazeta Povo', 'Noticias Minuto']
        )

        with tab_g1:
            st.write('Tab G1')
            opt_categoria = st.radio(
                'Escolha a categoria', [
                    'tecnologia',
                    'turismo-e-viagem',
                    'planeta-bizarro',
                    'para',
                    'ribeirao-preto-franca'
                ], horizontal=True, index=4)
            site = 'G1'
            noticias = self.__controler.obter_noticias(
                site=site, categoria=opt_categoria)

            for noticia in noticias.itertuples(index=False):

                col1, col2 = st.columns([2, 4])
                with col1:
                    try:
                        st.image(noticia.URL_IMG, width=200)
                    except:
                        st.text('Sem imagem')

                with col2:
                    titulo_quebrado = textwrap.fill(
                        noticia.TITULO_NOTICIA, width=60)
                    st.write(titulo_quebrado)
                    st.write(noticia.URL_NOTICIA)
                    st.write(noticia.DESCRICAO)

                st.markdown("---" * 20)
        with tab_gazeta_povo:
            st.write('Tab Gazeta Povo')
        with tab_noticas_minuto:
            st.write('Tab notícias minuto')
