from src.painel.controller.noticias_controller import NoticasControler
from src.painel.view.noticias_view import NoticiasView
import streamlit as st


def configurar_navegacao():
    st.set_page_config(page_title='Feed de Nóticias', layout='wide')


def tela():
    configurar_navegacao()
    controller = NoticasControler
    view = NoticiasView(controller=controller)
    view.exibir_tela()


tela()
