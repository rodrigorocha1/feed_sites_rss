from src.painel.controller.noticias_controller import NoticasControler
from src.painel.view.noticias_view import NoticiasView
import streamlit as st


def estilizar_abas():
    st.markdown(
        """
        <style>
        .stMarkdownContainer {
            font-size: 40px;  /* Ajuste o tamanho da fonte conforme necessário */
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def tela():

    estilizar_abas()
    controller = NoticasControler()
    view = NoticiasView(controller=controller)
    view.exibir_tela()


tela()
